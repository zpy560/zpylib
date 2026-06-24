# ros2_controllers 官方仓库源码快照

> 本文件记录 2026-06-24 对官方仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/ros-controls/ros2_controllers.git
- 官方文档：https://control.ros.org/
- 默认分支：`master`
- 发行版分支：`humble`、`jazzy`、`kilted`
- 抓取提交：`58969bf363185e941da1f6077ad07e9b15079d84`
- 提交时间：`2026-06-19 09:11:13 +0200`
- 提交标题：`Final test cleanup - call appropriate lifecycle transitions (#2429)`
- 抓取方式：Git 浅克隆
- 分析方式：静态源码、文档、package 和 CI 配置分析，未在 ROS 2 环境编译运行

## 仓库定位

README 将 ros2_controllers 定位为 ros2_control 框架中常用、通用、可直接用于多类机器人、MoveIt2 和 Nav2 的控制器集合。它是 `ros2_control` 的下游控制器插件库，而不是硬件抽象框架本身。

## 快照规模

- C++ 源文件：103。
- C++ 头文件：66。
- Python 文件：18。
- reStructuredText 文档：61。
- YAML 文件：63。
- XML 文件：52。
- GitHub Actions workflow：53。
- 包含 test 目录的包：26。

## 控制器类别

### 移动机器人

- `diff_drive_controller`：差速底盘控制器。
- `mecanum_drive_controller`：Mecanum 底盘控制器。
- `omni_wheel_drive_controller`：全向轮底盘控制器。
- `steering_controllers_library`：转向底盘通用库。
- `ackermann_steering_controller`：Ackermann 转向。
- `bicycle_steering_controller`：自行车模型转向。
- `tricycle_controller`、`tricycle_steering_controller`：三轮模型。

移动机器人文档覆盖全向与非完整约束底盘的运动学，包括 omni、swerve、unicycle 等模型。

### 机械臂与执行器

- `joint_trajectory_controller`：关节空间轨迹控制器。
- `admittance_controller`：导纳控制器。
- `pid_controller`：基于 `control_toolbox::PidROS` 的 PID 控制器。
- `forward_command_controller`：命令透传控制器。
- `parallel_gripper_controller`：平行夹爪控制器。
- `motion_primitives_controllers`：运动基元控制器。
- `gpio_controllers`：GPIO 控制。

### Broadcaster

文档明确说明 broadcaster 在 ros2_control 中仍然使用 controller interface，但主要职责是从硬件 state interface 发布 ROS topic。

包括：

- `joint_state_broadcaster`
- `force_torque_sensor_broadcaster`
- `imu_sensor_broadcaster`
- `gps_sensor_broadcaster`
- `range_sensor_broadcaster`
- `pose_broadcaster`
- `state_interfaces_broadcaster`
- `magnetometer_broadcaster`

### Filter

- `chained_filter_controller`：chainable controller，用于过滤 state interface 并导出过滤后的 state interface，不直接发布 ROS topic。

## 关键控制器事实

### diff_drive_controller

- 输入：`~/cmd_vel`，类型 `geometry_msgs/msg/TwistStamped`。
- 使用 linear x 和 angular z，忽略其他分量。
- 输出：左右轮 velocity command interface。
- 可用 position 或 velocity 作为 wheel feedback。
- 支持 open loop odometry。
- 发布 `~/odom`、可选 `/tf`、可选 `~/cmd_vel_out`。
- 支持速度、加速度、jerk 限制。
- 支持 command timeout 自动停车。
- 实现 chainable controller，导出 `<controller_name>/linear/velocity` 和 `<controller_name>/angular/velocity` reference interface。

### joint_trajectory_controller

- 执行多关节 joint-space trajectory。
- 接收 `trajectory_msgs/msg/JointTrajectory`。
- 支持 `control_msgs/action/FollowJointTrajectory` action。
- 支持 position、velocity、acceleration、effort 等 command interface 组合。
- 支持连续关节角度 wraparound。
- 支持 action preemption、trajectory replacement、path/goal tolerance。
- 可选 cancel 时按每关节 deceleration 限制平滑停车。
- 文档明确建议需要轨迹插值时使用 JTC；不要把 JTC 当普通单点 PID 使用。

### pid_controller

- 基于 `control_toolbox::PidROS`。
- 可独立接收 reference topic，也可作为 chainable controller 使用。
- 支持 reference/state 的一阶导数，用于二阶 PID 场景。
- 不做轨迹点插值；如果需要时间轨迹插值，应使用 Joint Trajectory Controller。

### admittance_controller

- 用 TCP force 实现导纳控制。
- 实现 `ChainedControllerInterface`，可放在 JointTrajectoryController 等控制器前后。
- 需要外部 kinematics plugin。
- 使用 force-torque semantic component 读取 wrench。

### steering_controllers_library

- 提供 steering drive 控制器共享能力。
- 支持 Bicycle、Tricycle、Ackermann。
- 输入是 stamped twist，使用 linear x 和 angular z。
- 输出 traction wheel velocity 与 steering joint position。
- 只实现运动学逆解和 odometry，不实现路径跟踪闭环。

## 插件开发规范

文档 `writing_new_controller.rst` 给出新控制器开发步骤：

1. 创建 ament_cmake 包。
2. 继承 `controller_interface::ControllerInterface`。
3. 实现 `on_init`、`command_interface_configuration`、`state_interface_configuration`、`on_configure`、`on_activate`、`on_deactivate`、`update`。
4. 在 `on_init` 声明参数并预分配内存。
5. 在 `on_activate` 检查并绑定接口，避免实时路径分配。
6. 在 `update` 中按实时约束写命令。
7. 用 `PLUGINLIB_EXPORT_CLASS` 导出。
8. 写 plugin XML。
9. 添加 load 测试，确认 Controller Manager 能找到插件。

## CI 与测试观察

- GitHub Actions workflow 数量约 53。
- 覆盖 Rolling/Lyrical/Humble/Jazzy/Kilted 的 binary、semi-binary、source、coverage、docs、ABI compatibility、pre-release、downstream 等构建。
- 多数控制器包包含 test 目录，常见 test 依赖包括 `controller_manager`、`hardware_interface_testing` 和 `ros2_control_test_assets`。
- 本次未本地执行 `colcon build` 或测试。

## 工程边界

- ros2_controllers 提供通用控制器，不负责硬件驱动、资源管理和实时主循环；这些由 ros2_control 提供。
- 移动底盘控制器主要是底盘运动学与命令限制，不是 Nav2 的局部路径规划器。
- `steering_controllers_library` 明确不实现路径跟踪闭环。
- JTC 是轨迹执行器，不负责运动规划。
- 具体部署必须检查目标硬件接口类型、joint name、controller manager 参数和 controller switching。
- 使用时必须按目标 ROS 发行版选择对应分支。
