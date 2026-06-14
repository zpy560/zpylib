# Apollo 本地仓库源码快照

> 本文件记录 2026-06-14 对本地 Apollo 仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 本地仓库：`/home/zpy/Documents/codex_ws/apollo`
- 分支：`master`
- 提交：`d53aa3da47a06a08e6d0cd175d5623a34fa0d6aa`
- 提交时间：`2026-04-16T20:24:44+08:00`
- 提交标题：`docs: fix README - remove invalid build status badges`
- Git 描述：`v11.0.0-10-gd53aa3da47`
- 网络访问：未使用
- 分析方式：源码、配置和文档静态检查；未编译、未启动、未进行车辆或仿真验证

仓库存在未跟踪目录 `.codegraph/` 与 `ros2_planning_ws/`，本次分析未将其作为 Apollo 源码证据。

## 版本标识

- `git describe` 表明当前提交位于 `v11.0.0` 之后 10 个提交。
- `README.md` 和 `RELEASE.md` 包含 Apollo 11.0 的说明。
- 根目录 `version.json` 仍写为 `9.0.0`。

因此本快照使用 Git 提交和标签描述作为版本依据，并保留 `version.json` 不一致这一事实。

## 系统主链

从模块目录、消息类型和组件输入输出可还原主要闭环：

```text
传感器
→ 定位 / 感知
→ 预测
→ 规划 ADCTrajectory
→ 控制 ControlCommand
→ Guardian（按配置启用）
→ Canbus
→ 车辆执行器
```

任务和地图约束从侧面进入规划：

```text
External Command / Planning Command / Routing
→ ReferenceLineProvider / PncMap
→ Planner / Scenario / Stage / Task
```

Cyber RT 负责组件加载、Topic 通信、定时触发和插件管理。规划是三输入 `Component`，控制和 Guardian 是 10 ms 周期的 `TimerComponent`。

## 规划主链

### 组件入口

`PlanningComponent` 由以下三路主输入触发：

- `/apollo/prediction`
- `/apollo/canbus/chassis`
- `/apollo/localization/pose`

它还异步读取 Planning Command、Traffic Light Detection、Pad Message、Storytelling、Control Interactive Message，以及导航模式下的 Relative Map。

处理完成后发布 `/apollo/planning` 的 `ADCTrajectory` 和命令执行状态。

### OnLanePlanning

默认主链为：

```text
PlanningComponent::Proc
→ OnLanePlanning::RunOnce
→ 更新 VehicleState
→ 轨迹拼接
→ 创建 Frame
→ 生成和裁剪 ReferenceLine
→ TrafficDecider
→ PublicRoadPlanner::Plan
→ 填充并发布 ADCTrajectory
```

关键行为：

- 车辆状态无效时生成零速停止轨迹。
- 新任务到达时重置参考线、历史、PlanningContext 和 Planner。
- `TrajectoryStitcher` 连接上一周期轨迹，必要时触发重规划。
- `Frame` 聚合参考线、障碍物、车辆状态和场景上下文。
- 交通规则在 Planner 前逐条作用于候选参考线。
- 道路规划和开放空间规划使用不同的轨迹导出路径。

### Planner、Scenario、Stage、Task

默认 Planner 为 `PublicRoadPlanner`。执行层级为：

```text
PublicRoadPlanner
→ ScenarioManager
→ Scenario
→ Stage
→ Task 列表
→ Path 与 Speed 合成
```

- `ScenarioManager` 按配置顺序加载场景插件。
- 当前场景处于处理中时保持优先，不切换到其他场景。
- 场景通过 `IsTransferable()` 决定是否接管。
- Scenario 根据 `pipeline.pb.txt` 创建 Stage。
- Stage 根据配置动态创建 Task，并按顺序执行。
- 任一 Task 失败后执行 fallback task。
- 路径和速度成功后由 `CombinePathAndSpeedProfile()` 合成为轨迹。

公共道路配置包含 Emergency Pull Over、Emergency Stop、Valet Parking、Bare Intersection、Stop Sign、Yield Sign、三类 Traffic Light、Pull Over、Park And Go 和 Lane Follow 共 12 个场景。

Lane Follow 的默认 Task 顺序体现了“先路径、后速度”的串行流水线：

```text
Lane Change Path
→ Lane Follow Path
→ Lane Borrow Path
→ Fallback Path
→ Path Decider
→ Rule Based Stop Decider
→ Speed Bounds
→ Path-Time Heuristic
→ Speed Decider
→ Final Speed Bounds
→ Piecewise Jerk Speed
```

## 控制主链

### 单组件模式

`ControlComponent` 每 10 ms 执行一次，读取 Chassis、ADCTrajectory、Localization、Planning Command Status 和 Pad Message。

主链为：

```text
采集最新输入
→ CheckInput
→ CheckTimestamp
→ 急停与挡位保护
→ ControlTaskAgent
→ 控制器插件串行执行
→ ControlCommand
```

默认 `pipeline.pb.txt` 配置：

```text
LatController（LQR 横向）
→ LonController（PID 纵向）
```

仓库同时提供 MPC、增强版 LQR/PID、坡道防溜和重规划交互等控制任务插件。

### 子模块模式

配置还支持把控制拆成：

```text
ControlComponent
→ LocalView
→ PreprocessorSubmodule
→ LatLonControllerSubmodule 或 MPCControllerSubmodule
→ PostprocessorSubmodule
→ ControlCommand
```

该模式把输入检查、控制核心和命令后处理拆成独立 Cyber 组件。

### 控制兜底

以下情况会阻止正常控制计算或触发软急停：

- 输入消息无效。
- Localization、Chassis 或 Planning 超时。
- Planning 显式发布 EStop。
- Planning 轨迹为空。
- 前进挡轨迹首点速度为负。
- 控制器计算返回错误。

软急停命令设置零速度、零油门、制动和保持上一转向目标。

## 安全链

代码中存在三层安全处理：

1. Planning 在状态异常或规划失败时生成停止轨迹，或按配置发布 EStop。
2. Control 检查输入、时间戳、规划 EStop 和控制器状态，异常时生成软急停命令。
3. Monitor 可设置 `safety_mode_trigger_time` 和 `require_emergency_stop`，Guardian 据此旁路或改写 ControlCommand，再由 Canbus 接收。

Guardian 的设计链路是：

```text
Monitor SystemStatus + Chassis + ControlCommand
→ GuardianCommand
→ Canbus
```

当前默认配置需要注意：

- `guardian_conf.pb.txt` 中 `guardian_enable: true`。
- `canbus.conf` 中存在 `--noreceive_guardian`，Canbus 默认直接读取 ControlCommand。
- `canbus.conf` 中 `--use_guardian_cmd_check=false`，Guardian 命令超时检查默认关闭。
- `GuardianComponent::TriggerSafetyMode()` 计算超声波故障和障碍物后，又把两个布尔量强制改为 `false`，代码注释说明当前临时忽略超声波输出。

因此仅看到 Guardian 模块存在，不能推断整车运行配置已经启用了完整 Guardian 安全链。

## 静态代码风险

### 1. 版本元数据不一致

`version.json` 为 `9.0.0`，Git 标签关系和发布文档为 11.0 系列。依赖 `version.json` 的工具可能得到错误版本。

### 2. 控制子模块预处理的轨迹修正不生效

`PreprocessorSubmodule::CheckInput()` 使用按值循环：

```cpp
for (auto trajectory_point : local_view->trajectory().trajectory_point())
```

循环内对低速点执行的 `set_v(0.0)` 和 `set_a(0.0)` 只修改副本，不会写回 `LocalView`。单组件模式使用可变引用，不存在同样问题。

### 3. Guardian 临时关闭超声波判定

`GuardianComponent::TriggerSafetyMode()` 在完成超声波故障和障碍物判断后，显式把结果重置为 `false`。当前代码下，超声波结果不会决定紧急制动分支。

### 4. 安全能力依赖部署配置

Guardian、命令超时检查和安全重规划任务均可配置或插拔。源码中的能力不等于目标部署已经启用，必须结合实际 launch、flag、pipeline 和车辆配置审计。

## 本次检查的关键文件

- `README.md`
- `RELEASE.md`
- `version.json`
- `modules/planning/planning_component/planning_component.{h,cc}`
- `modules/planning/planning_component/on_lane_planning.cc`
- `modules/planning/planning_component/conf/planning_config.pb.txt`
- `modules/planning/planning_component/conf/public_road_planner_config.pb.txt`
- `modules/planning/planners/public_road/public_road_planner.cc`
- `modules/planning/planners/public_road/scenario_manager.cc`
- `modules/planning/planning_interface_base/scenario_base/{scenario,stage}.cc`
- `modules/planning/planning_interface_base/task_base/task.cc`
- `modules/planning/scenarios/lane_follow/conf/pipeline.pb.txt`
- `modules/control/control_component/control_component.{h,cc}`
- `modules/control/control_component/controller_task_base/control_task_agent.cc`
- `modules/control/control_component/submodules/{preprocessor,postprocessor}_submodule.cc`
- `modules/control/control_component/conf/pipeline.pb.txt`
- `modules/control/control_component/dag/*.dag`
- `modules/control/controllers/*/plugins.xml`
- `modules/control/controllers/replan_control_task/replan_control_task.cc`
- `modules/monitor/software/functional_safety_monitor.cc`
- `modules/guardian/guardian_component.cc`
- `modules/guardian/conf/guardian_conf.pb.txt`
- `modules/canbus/canbus_component.cc`
- `modules/canbus/conf/canbus.conf`
