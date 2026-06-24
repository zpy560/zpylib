---
id: "20260624-ros2-control-hardware-controller-framework"
title: "ros2_control：ROS 2 硬件抽象与控制器管理框架"
type: "note"
source: "raw/2026-06-24-ros2-control-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-ros2-control.md
  - notes/2026-06-24-ros2-controllers-common-controller-plugins.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
  - notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md
---

# ros2_control：ROS 2 硬件抽象与控制器管理框架

## 一句话结论

ros2_control 是 ROS 2 机器人控制的底层框架：Controller Manager 以实时循环执行 `read → update → write`，Resource Manager 管理硬件接口资源，controller/hardware 通过 pluginlib 和 lifecycle 接入；它解决“控制器如何安全地占用接口并驱动硬件”的框架问题，不解决自动驾驶的行为决策、轨迹规划或整车功能安全。

## 原文要点

### 系统主链

ros2_control 的核心运行链路是：

```text
URDF <ros2_control>
→ Resource Manager 加载 hardware plugin
→ Controller Manager 加载 controller plugin
→ controller 声明所需 state/command interface
→ Resource Manager 借出接口
→ 控制线程循环 read → update → write
→ hardware read/write 与真实设备交互
```

`ros2_control_node` 会启动单独控制线程，尝试设置 `SCHED_FIFO`，默认优先级 50，并按 `update_rate` 调度主循环。非仿真时间下还会检测 overrun。

### Controller Manager 是运行中枢

Controller Manager 负责：

- 加载、配置、激活、停用、清理、卸载 controller。
- 读取硬件状态、更新控制器、写入硬件命令。
- 管理 controller switch。
- 管理 hardware component lifecycle。
- 提供 controller/hardware 查询服务。
- 发布 controller 和 hardware 活动状态。

它提供 `LoadController`、`ConfigureController`、`SwitchController`、`ListControllers`、`ListHardwareInterfaces`、`SetHardwareComponentState` 等服务。`SwitchController` 支持 `STRICT`、`BEST_EFFORT`、`AUTO` 和 `FORCE_AUTO`，其中自动模式用于处理链式控制器依赖和互斥接口冲突。

### Hardware Interface 把设备做成插件

硬件组件分为 `Actuator`、`Sensor`、`System`。复杂机器人通常实现 `SystemInterface`，并在生命周期中完成初始化、通信建立、激活、停用、错误处理、读写硬件。

硬件接口通过 URDF `<ros2_control>` 描述 plugin、joint、sensor、gpio、state interface 和 command interface。接口全名通常是：

```text
<joint_name>/<interface_type>
```

例如 `wheel_left_joint/velocity`。

### Resource Manager 管资源所有权

Resource Manager 维护硬件 state/command interface 列表，负责接口 availability 和 claimed 状态。Controller 只能使用自己声明并成功借用的接口。

这点是 ros2_control 的关键价值：它把“哪个控制器此刻能命令哪个硬件接口”变成可查询、可切换、可验证的运行时资源管理问题，而不是让多个节点随意向硬件发命令。

### 支持串级控制

Chainable controller 可以导出 reference interface 和 state interface，其他 controller 可以像使用硬件接口一样使用这些虚拟接口。典型场景是：

```text
上层位置/速度控制器
→ diff drive / kinematics controller
→ wheel PID controllers
→ motor hardware interface
```

激活链式控制器时必须按依赖顺序成组处理，`spawner --activate-as-group` 和 `SwitchController` 的自动模式就是为这个问题服务。

## 我的判断

### 它是 ROS 2 执行层的关键基础设施

Nav2 输出 `cmd_vel`，Autoware 输出车辆控制命令，但真正接近硬件时仍需要解决：

- 硬件驱动如何统一抽象？
- 控制器如何热加载和切换？
- 多个控制器如何避免同时抢同一个 command interface？
- 硬件生命周期和控制器生命周期如何协调？
- 实时循环中如何组织 read、control update 和 write？

ros2_control 正是回答这些问题的框架。它位于规划控制链最靠近执行器的一层。

### 最值得借鉴的是资源边界，而不是某个控制算法

仓库本身没有把 MPC、PID、DiffDrive 等具体控制算法作为重点；这些通常在 `ros2_controllers` 等下游仓库。主仓库的价值在于接口契约：

- controller 声明需要哪些 state/command interface。
- Resource Manager 负责接口借用和 claimed 状态。
- Controller Manager 负责生命周期、切换和主循环。
- hardware plugin 只暴露标准接口，不把设备细节泄漏给上层控制器。

这套边界对自动驾驶底盘接口也有参考价值：最终车辆命令应进入一个明确的资源管理和模式切换层，而不是让规划、控制、安全模块都直接写执行器。

### 实时性不是框架自动保证

源码会尝试配置 `SCHED_FIFO`、内存锁定、CPU affinity，并提示使用实时/低延迟内核。但这只能降低框架层面的抖动风险。真实实时性还取决于：

- 内核和系统权限。
- 硬件驱动 read/write 阻塞行为。
- 控制器 update 是否分配内存或阻塞。
- DDS、日志、参数和诊断是否进入实时路径。
- 目标硬件和总线延迟。

因此不能把“使用 ros2_control”等同于“满足硬实时控制”。

### 安全语义还需要系统工程补齐

文档明确说硬件 INACTIVE 状态下的命令接口安全语义仍有路线图事项；fallback controller、controller switch、chain activation 也都建议先在仿真中验证。

对自动驾驶或工业机器人而言，ros2_control 只能提供框架机制，仍需额外定义：

- 紧急停止与失控降级。
- 命令超时策略。
- 控制器切换前后的命令连续性。
- 硬件错误恢复策略。
- 上层模式管理与安全门控。
- 目标平台上的实时和故障注入测试。

## 可复用内容

### 评审执行层架构的问题

1. 控制器是否显式声明所需 state/command interface？
2. 是否有统一资源管理，避免多个控制器同时命令同一接口？
3. 硬件是否有明确 lifecycle，而不是启动即带电可动？
4. 主循环是否清楚分成 read、update、write？
5. 控制器切换是否有 STRICT/BEST_EFFORT/自动依赖处理策略？
6. 是否能查询当前 controller、hardware、interface 的状态？
7. 是否有实时线程、内存锁定、overrun 检测和运行统计？
8. 硬件错误、控制器错误和 fallback 是否经过仿真与实机验证？

### 写硬件插件的最小清单

1. 在 URDF `<ros2_control>` 中声明 hardware plugin 和 interfaces。
2. 实现 `ActuatorInterface`、`SensorInterface` 或 `SystemInterface`。
3. 在 `on_init` 解析参数并初始化内部状态。
4. 在 `on_configure` 建立通信。
5. 在 `on_activate` 允许硬件运动。
6. 在 `read` 更新 state interfaces。
7. 在 `write` 发送 command interfaces。
8. 在 `on_error`、`on_deactivate`、`on_shutdown` 定义安全退出。
9. 用 pluginlib 导出硬件类。
10. 用 CLI 和 Controller Manager services 验证 lifecycle、interfaces 和 read/write 行为。

### 使用时的版本规则

按目标 ROS 发行版使用对应分支：

- Rolling/Lyrical：`master`
- Kilted：`kilted`
- Jazzy：`jazzy`
- Humble：`humble`

不要把 `master` 的 API 假设直接套到 Humble/Jazzy/Kilted 项目。

## 疑问与冲突

- 本次未执行 `colcon build`，因为本地未确认完整 ROS 2 rolling/ros2_control 依赖环境。
- `joint_limits` 文档中的限制算法细节仍标为 `tba`，实际行为需要读源码和测试验证。
- INACTIVE 状态下命令接口安全语义仍有路线图事项，不能仅靠 lifecycle 状态推断硬件安全。
- ros2_controllers 已补充至 `notes/2026-06-24-ros2-controllers-common-controller-plugins.md`。ros2_control 负责框架和资源管理，ros2_controllers 负责常用控制器实现。

## 原料

- `raw/2026-06-24-ros2-control-repository-snapshot.md`
