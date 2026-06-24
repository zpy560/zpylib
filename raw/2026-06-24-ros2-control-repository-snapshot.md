# ros2_control 官方仓库源码快照

> 本文件记录 2026-06-24 对官方仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/ros-controls/ros2_control.git
- 官方文档：https://control.ros.org/
- 默认分支：`master`
- 发行版分支：`humble`、`jazzy`、`kilted`，以及旧版 `foxy`、`galactic`、`iron` 等
- 抓取提交：`4f9692862234f260684fa27d04ff5b773fa1ef76`
- 提交时间：`2026-06-22 14:34:24 +0200`
- 提交标题：`Bump actions/checkout from 6 to 7 (#3402)`
- 抓取方式：Git 浅克隆
- 分析方式：静态源码、文档、package、消息服务和 CI 配置分析，未在 ROS 2 环境编译运行

## 仓库定位

ros2_control 是 ROS 2 的控制框架核心。它不提供某一个具体机器人控制算法，而是提供：

- 控制器生命周期与插件加载。
- 硬件抽象和硬件生命周期。
- Command/State interface 管理。
- 控制器与硬件接口资源声明、借用和切换。
- 实时主循环 `read → update → write`。
- joint limits 与 transmission 基础设施。
- controller manager service、CLI 和 rqt 图形前端。

## 快照规模

- C++ 源文件：84。
- C++ 头文件：95。
- Python 文件：38。
- reStructuredText 文档：32。
- GitHub Actions workflow：57。
- ROS package：11 个。
- service 定义：11。
- message 定义：6。

## 包结构

| 包 | 职责 |
|---|---|
| `ros2_control` | 元包，聚合核心包 |
| `controller_manager` | 主运行入口，管理控制器、硬件资源和服务接口 |
| `controller_interface` | 控制器基类，包含普通控制器和 chainable controller 抽象 |
| `controller_manager_msgs` | Controller Manager 的消息和服务定义 |
| `hardware_interface` | Actuator/Sensor/System 硬件抽象、Resource Manager 和 URDF 解析 |
| `hardware_interface_testing` | 硬件接口测试 fixture |
| `joint_limits` | joint limit 数据结构和限制器 |
| `transmission_interface` | actuator/joint 空间传动关系建模 |
| `ros2_control_test_assets` | 测试 URDF 与共享资源 |
| `ros2controlcli` | `ros2 control` 命令行扩展 |
| `rqt_controller_manager` | controller manager 图形前端 |

版本字段多数为 `6.7.1`。许可证主要为 Apache License 2.0，`controller_manager_msgs` 标为 BSD。

## 核心主循环

`controller_manager/src/ros2_control_node.cpp` 创建 `ControllerManager` 和 `MultiThreadedExecutor`，再启动单独控制线程。

控制线程：

1. 可配置 CPU affinity。
2. 尝试将线程设为 `SCHED_FIFO`，默认优先级 50。
3. 等待 ROS clock 启动。
4. 按 `update_rate` 计算周期。
5. 循环执行：

```text
cm->read(time, measured_period)
cm->update(time, measured_period)
cm->write(time, measured_period)
```

如果不使用 sim time，则用 steady clock 睡眠到下一周期；启用 overrun 管理时，会检测并打印错过周期。

Controller Manager 文档还建议为实时控制配置 realtime 用户组、`rtprio`、`memlock`，并说明普通 Linux 内核不适合低抖动硬件控制，建议实时或 lowlatency 内核。

## Controller Manager

`controller_manager` 是 ros2_control 主组件，职责包括：

- 从 `robot_description` 读取 URDF。
- 初始化 `ResourceManager`。
- 加载 controller plugin。
- 配置、激活、停用、清理、卸载 controller。
- 读硬件、更新控制器、写硬件。
- 管理 controller switch。
- 管理 controller chaining。
- 发布 controller/hardware 活动状态。
- 提供 controller 和 hardware 查询服务。

关键服务包括：

- `LoadController`
- `ConfigureController`
- `SwitchController`
- `UnloadController`
- `CleanupController`
- `ListControllers`
- `ListControllerTypes`
- `ListHardwareInterfaces`
- `ListHardwareComponents`
- `SetHardwareComponentState`
- `ReloadControllerLibraries`

`SwitchController` 支持 `BEST_EFFORT`、`STRICT`、`AUTO`、`FORCE_AUTO`。其中 `AUTO` 与 `FORCE_AUTO` 用于根据 controller chain 和互斥 joint interface 原则自动处理依赖或冲突。

## Hardware Interface

硬件组件分三类：

- `Actuator`
- `Sensor`
- `System`

`SystemInterface` 用于多关节系统、工业机器人、人形机器人等复杂系统。硬件生命周期语义：

- `UNCONFIGURED`：已初始化，但未启动通信，接口未导入 Resource Manager。
- `INACTIVE`：通信已建立，状态可读，运动命令接口的安全语义仍依赖硬件实现。
- `ACTIVE`：硬件可运动，命令接口可用。
- `FINALIZED`：准备卸载和销毁。

文档明确指出，当前 INACTIVE 状态下命令接口处理仍有安全相关待完善事项，安全关键接口计划仍在路线图中。

硬件实现通常需要：

- `on_init`
- `on_configure`
- `on_cleanup`
- `on_shutdown`
- `on_activate`
- `on_deactivate`
- `on_error`
- `read`
- `write`
- 可选 `prepare_command_mode_switch`
- 可选 `perform_command_mode_switch`

硬件插件通过 pluginlib 动态加载。URDF 的 `<ros2_control>` 标签描述硬件 plugin、joint、sensor、gpio、state interface 和 command interface。

## Resource Manager

`hardware_interface::ResourceManager` 负责：

- 从 URDF 加载并初始化硬件组件。
- 通过 pluginlib 创建硬件实例。
- 维护 state/command interface 列表。
- 提供 `claim_state_interface()` 和 command interface 借用。
- 导入 controller 导出的 state/reference interface，用于 controller chaining。
- 管理 hardware component lifecycle。
- 处理 read/write 错误，并触发硬件 `on_error`。
- 导入 joint limiters。

接口全名通常为：

```text
<joint_name>/<interface_type>
```

如 `joint1/position`、`joint1/velocity`。

## Controller Interface 与 Chaining

普通控制器实现 `ControllerInterface`，声明需要的 command/state interface，由 Controller Manager 负责借用资源并调用 update。

Chainable controller 可以导出：

- reference interface：作为后续控制器的输入命令。
- state interface：作为其他控制器可读取状态。

Controller Manager 将 controller 导出的 reference/state interface 纳入 Resource Manager 管理。串级控制激活规则是：

- 激活时，必须先激活 following controllers，再激活 preceding controller。
- 停用时，必须先停用 preceding controllers，再停用 following controller。
- `spawner --activate-as-group` 可用于成组激活链式控制器。

该机制支持类似：

```text
position tracking
→ diff drive controller
→ wheel PID controllers
→ hardware command interfaces
```

也支持 odom、sensor fusion、localization 等 controller 间状态接口连接。

## Joint Limits 与 Transmission

`joint_limits` 支持从 URDF 或 `<ros2_control>` 配置中启用/关闭 joint limit。全局参数 `enforce_command_limits` 可控制是否在 Controller Manager 层强制命令限制。

限制信息覆盖 position、velocity、acceleration、deceleration、jerk、effort、wraparound 等字段。文档中算法细节仍标为 `tba`。

`transmission_interface` 表示 actuator 与 joint 空间之间的机械传动关系，用于在 actuator command/state 和 joint command/state 间传播数据。

## CLI 与可观测性

`ros2controlcli` 提供 `ros2 control` 子命令，覆盖：

- list controller types
- list controllers
- list hardware interfaces
- list hardware components
- load/configure/cleanup/unload controller
- switch controllers
- set hardware component state
- view controller chains
- view hardware status

`view_controller_chains` 使用 pygraphviz 生成 controller/interface 链路图。`view_hardware_status` 订阅 `control_msgs/msg/HardwareStatus`，可按 hardware id 或 device id 过滤。

Controller Manager 发布 `~/activity`，消息类型为 `ControllerManagerActivity`，包含 controllers 和 hardware components 的 lifecycle state，QoS 使用 transient local。

## CI 与测试观察

仓库 CI 覆盖很宽：

- Rolling/Lyrical/Humble/Jazzy/Kilted 分支或兼容构建。
- binary、semi-binary、source、Debian、RHEL、Windows、coverage、pre-commit、docs、ABI compatibility、pre-release、downstream build。
- 多个 workflow 使用 `ros-controls/ros2_control_ci` 复用工作流。

源码包含大量 C++/Python 测试目录和共享 test assets。本次未执行本地构建或测试，因为本地没有确认完整 ROS 2 rolling/ros2_control 依赖环境。

## 工程边界

- ros2_control 是控制框架，不是自动驾驶决策、规划或安全栈。
- 具体控制器实现主要在 `ros2_controllers` 等下游仓库，本仓库提供控制器和硬件的框架接口。
- 实时性依赖内核、权限、内存锁定、CPU affinity、硬件驱动和控制器实现；框架尝试配置实时调度不等于系统已经满足实时控制。
- INACTIVE 状态下运动命令接口的安全语义仍需硬件实现和部署策略保证。
- Controller switching、chainable controller 和 fallback controller 必须在仿真和目标硬件上验证。
- 使用时必须按目标 ROS 发行版选择对应分支，不能直接把 `master` 代码套到 Humble/Jazzy/Kilted 项目。
