---
id: "20260624-ros2-controllers-common-controller-plugins"
title: "ros2_controllers：ros2_control 的通用控制器插件集合"
type: "note"
source: "raw/2026-06-24-ros2-controllers-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-ros2-controllers.md
  - notes/2026-06-24-ros2-control-hardware-controller-framework.md
  - notes/2026-06-24-moveit2-ros2-manipulation-motion-planning.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
  - notes/2026-06-14-autoware-ros2-autonomous-driving-platform.md
---

# ros2_controllers：ros2_control 的通用控制器插件集合

## 一句话结论

ros2_controllers 是 ros2_control 生态里的通用控制器和 broadcaster 仓库，覆盖差速、全向、Mecanum、Ackermann、Tricycle、关节轨迹、PID、导纳、夹爪、传感器状态发布等常见执行层能力；它提供可复用控制器插件，不提供硬件资源管理、导航规划或自动驾驶安全门控。

## 原文要点

### 与 ros2_control 的分工

```text
ros2_control
→ Controller Manager / Resource Manager / Hardware Interface

ros2_controllers
→ 可加载到 Controller Manager 的通用 controller plugins
```

ros2_control 解决框架和资源管理；ros2_controllers 提供常用控制器实现。README 明确说这些控制器可用于多类机器人、MoveIt2 和 Nav2。

### 控制器覆盖范围

移动底盘：

- 差速底盘。
- Mecanum。
- Omni wheel。
- Bicycle、Tricycle、Ackermann 等 steering 模型。

机械臂和执行器：

- Joint Trajectory Controller。
- PID Controller。
- Admittance Controller。
- Forward Command Controller。
- Parallel Gripper Controller。
- Motion Primitives Controllers。

状态发布：

- Joint state、force torque、IMU、GPS、range、pose、state interfaces、magnetometer broadcasters。

### 控制器共同约束

控制器运行在 Controller Manager 调度下，必须声明 state/command interface。`update_rate` 可以为每个控制器单独设置；`is_async` 可以指定异步更新。

新控制器开发文档强调：`update()` 是实时路径，应避免内存分配和阻塞；接口绑定和检查应放在 `on_activate()`。

## 我的判断

### 它是执行层标准件库

如果说 ros2_control 是底盘/执行器控制框架，ros2_controllers 就是框架上最常用的标准控制器集合。工程上应优先评估这里已有控制器是否满足需求，再决定是否自研。

对移动机器人，`diff_drive_controller`、Mecanum、Omni、Ackermann/Tricycle 系列可以直接承接 Nav2 的速度命令或上层 chainable reference。对机械臂，`joint_trajectory_controller` 是 MoveIt2 等上层规划输出落到关节执行的关键接口。

### 不要把底盘控制器误当局部规划器

`diff_drive_controller` 接收 body twist 并转换成 wheel velocity，带 odometry、速度限制和 timeout 停车。它不做局部避障、路径选择或轨迹优化。Nav2 的 Controller Server/MPPI/DWB/RPP 等解决“该给什么速度”，ros2_controllers 解决“如何把速度命令送到硬件接口并维持执行层约束”。

同理，steering controllers 只做运动学逆解和 odometry，不是车辆轨迹跟踪器。

### JTC 是轨迹执行接口，不是规划器

Joint Trajectory Controller 负责执行已经生成的 joint trajectory，处理插值、action preemption、tolerance、连续关节和 cancel 减速。它不产生轨迹，不替代 MoveIt2 规划器或任务层逻辑。

### 安全仍然依赖部署链

控制器提供 timeout、限制器、tolerance、hold position、decelerate on cancel 等机制，但实际安全取决于：

- controller manager 中实际加载和激活了哪个控制器。
- hardware interface 是否正确实现 read/write 与错误处理。
- command interface 是否被正确声明和独占。
- 上层模式管理、急停和安全门控是否存在。
- 目标硬件是否通过仿真和实机测试。

## 可复用内容

### 选择控制器的粗略规则

- Nav2 差速底盘：优先看 `diff_drive_controller`。
- Mecanum / Omni 底盘：看对应 mobile base controllers。
- Ackermann / Tricycle / Bicycle：看 `steering_controllers_library` 和具体 controller。
- MoveIt2 关节轨迹：看 `joint_trajectory_controller`。
- 简单接口透传：看 `forward_command_controller`。
- 单自由度闭环或串级 PID：看 `pid_controller`。
- 力控柔顺：看 `admittance_controller`。
- 只发布状态：看 broadcaster 系列。

### 自研控制器检查项

1. 是否能用已有 controller 配置解决？
2. command/state interface 是否清楚声明？
3. `on_init` 是否只做参数声明和预分配？
4. `on_activate` 是否完成接口绑定和初值检查？
5. `update` 是否实时安全？
6. 是否提供 plugin XML 和 load test？
7. 是否考虑 timeout、NaN、接口缺失、切换、取消和降级？

## 疑问与冲突

- 本次未执行 `colcon build`，因为本地未确认完整 ROS 2 rolling/ros2_control 依赖环境。
- 控制器具体参数很多，实际使用必须按目标机器人逐项审查 YAML。
- 自动驾驶车辆的安全门控、模式管理、AEB、MRM 不在本仓库职责内。

## 原料

- `raw/2026-06-24-ros2-controllers-repository-snapshot.md`
