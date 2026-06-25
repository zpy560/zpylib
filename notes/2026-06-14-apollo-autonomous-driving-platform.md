---
id: "20260614-apollo-autonomous-driving-platform"
title: "Apollo：插件化自动驾驶平台与规划控制主链"
type: "note"
source: "raw/2026-06-14-apollo-local-repository-snapshot.md"
created_at: "2026-06-14"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
  - notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md
  - notes/2026-06-15-dig-into-apollo-source-reading-archive.md
  - notes/2026-06-24-apollo-current-status-refresh.md
  - notes/2026-06-24-openpilot-driver-assistance-operating-system.md
  - wiki/2026-06-14-apollo.md
---

# Apollo：插件化自动驾驶平台与规划控制主链

## 一句话结论

Apollo 的核心价值不是某个规划或控制算法，而是以 Cyber RT、统一消息、配置流水线和插件接口把感知到执行的完整自动驾驶闭环组织起来；其规划采用 `Planner → Scenario → Stage → Task` 的分层状态机，控制采用输入检查、控制器任务和后处理链，但安全能力是否真正生效高度依赖部署配置。

## 原文要点

### 系统闭环

```text
传感器
→ 定位 / 感知 / 预测
→ PlanningComponent
→ ADCTrajectory
→ ControlComponent
→ ControlCommand
→ Guardian（可配置）
→ Canbus
→ 车辆
```

任务入口由 External Command、Planning Command、Routing 和地图约束提供。Cyber RT 负责组件调度和通信，PluginManager 负责运行时算法装载。

### 规划是两层状态机加任务流水线

```text
OnLanePlanning
→ PublicRoadPlanner
→ ScenarioManager
→ Scenario
→ Stage
→ Task
```

- Scenario 表达红绿灯、停车、靠边、代客泊车等业务状态。
- Stage 表达场景内部的阶段迁移。
- Task 承载路径生成、决策、速度边界和优化算法。
- 场景、阶段和任务都通过插件与配置组合。
- Task 失败后执行 fallback task，再尝试合成可执行轨迹。

Lane Follow 的默认任务链先处理路径，再构建 ST 约束并优化速度。这种组织方式把业务状态、运动约束和数值优化放在不同层级。

### 控制支持单体和子模块两种部署

默认控制器流水线为：

```text
LQR 横向控制
→ PID 纵向控制
```

控制器通过 `ControlTask` 插件加载，也可以替换为 MPC 或其他任务。控制还能拆成预处理、控制核心和后处理三个 Cyber 组件，便于隔离职责和独立部署。

### 失败不是单点处理

- 规划状态无效：生成停止轨迹。
- Task 失败：执行轨迹 fallback task。
- 规划失败：可发布 EStop。
- 控制输入无效或超时：软急停。
- Monitor 检测关键模块异常：进入 safety mode。
- Guardian：按配置旁路或覆盖控制命令。
- Canbus：检查命令超时和底盘通信故障。

## 我的判断

### 最值得借鉴的是“变化频率分层”

Apollo 把不同变化频率的内容拆开：

1. Cyber Component 解决稳定的进程和通信边界。
2. Planner、Scenario、Stage、Task、ControlTask 解决算法替换。
3. protobuf 和配置文件解决运行组合。
4. Frame、ReferenceLineInfo、PlanningContext 和 DependencyInjector 解决周期内数据共享。

这比把全部逻辑写入一个 Planning 主循环更适合多人、多车型和多场景协作。

### Scenario 机制适合道路业务，但复杂度会转移到配置

`Scenario → Stage → Task` 能清晰表达交通灯、停车、泊车等道路语义，也能让算法插件复用。但复杂度没有消失，而是分散到：

- 场景切换条件
- 配置顺序和优先级
- Stage 迁移
- Task 读写同一 Frame 的隐式契约
- 插件名称、路径和配置文件

因此评审 Apollo 规划问题时，不能只读算法实现，必须同时读取 scenario pipeline、task config、gflags 和 launch。

### 安全链必须按“实际启用路径”审计

源码包含 Planning EStop、Control 软急停、Monitor、Guardian 和 Canbus 超时保护，但本地默认 `canbus.conf` 不接收 Guardian，且 Guardian 当前临时忽略超声波判定。

工程结论是：模块存在不等于安全目标达成。安全评审必须追踪最终车辆配置中的真实 Topic 链和 flag，而不是根据目录名或发布说明判断。

### 当前快照有三项值得修复的静态问题

1. `version.json` 与 Git 标签和发布文档不一致。
2. 控制子模块预处理按值遍历轨迹点，低速归零修改不会写回。
3. Guardian 显式清除超声波故障和障碍判断，相关紧急制动逻辑当前不生效。

这些结论来自静态源码，不代表已经通过运行测试复现。

### Apollo 与 Navigation2 的核心差异

两者都使用组件化和插件化，但抽象中心不同：

| 维度 | Apollo | Navigation2 |
|---|---|---|
| 主要领域 | 开放道路与功能型自动驾驶 | 移动机器人导航 |
| 策略编排 | Scenario / Stage 状态机 | Behavior Tree |
| 环境表达 | HD Map、Reference Line、障碍预测 | Costmap、TF、Path |
| 运动输出 | 时空轨迹 `ADCTrajectory` | 路径与速度指令 |
| 控制 | LQR、PID、MPC 等车辆控制器 | 局部控制器输出 `cmd_vel` |
| 安全末端 | Control、Guardian、Canbus | Velocity Smoother、Collision Monitor |

Apollo 更强调道路语义、轨迹时空约束和车辆执行闭环；Nav2 更强调通用任务编排、服务器边界和机器人导航恢复。

## 可复用内容

### 规划控制系统的四层扩展骨架

```text
运行时组件层
→ 业务状态层
→ 算法任务层
→ 安全执行层
```

### 评审 Apollo 二次开发的检查顺序

1. 确认 Git 提交、标签和部署包版本。
2. 确认实际加载的 DAG、launch、flag 和 pipeline。
3. 从 Topic 输入追踪到最终车辆命令。
4. 检查 Scenario、Stage、Task 的插件和配置。
5. 检查 fallback、EStop、Guardian 和命令超时是否真实启用。
6. 最后再评审具体算法和参数。

## 疑问与冲突

- `version.json` 为什么仍停留在 9.0.0，需要结合发布和打包流程确认。
- Guardian 超声波临时屏蔽是否由其他 Safety Manager 替代，需要检查目标部署的实际配置。
- 控制子模块模式的按值遍历问题需要单元测试或回放验证影响。
- 本次未编译和运行 Apollo，实时性能、插件加载完整性和配置可用性不在结论范围内。

## 原料

- `raw/2026-06-14-apollo-local-repository-snapshot.md`

## 延伸阅读

- `notes/2026-06-15-dig-into-apollo-source-reading-archive.md`：跨 Apollo 2.0 至 6.0 的中文源码阅读档案，适合定位历史调用链；涉及当前 Apollo 11 的结论仍以本地源码快照为准。
