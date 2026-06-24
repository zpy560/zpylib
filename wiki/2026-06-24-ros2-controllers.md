---
id: "20260624-ros2-controllers"
title: "ros2_controllers"
type: "entity"
source: "https://github.com/ros-controls/ros2_controllers.git"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-ros2-controllers-common-controller-plugins.md
  - wiki/2026-06-24-ros2-control.md
  - wiki/2026-06-24-moveit2.md
  - wiki/2026-06-13-navigation2.md
  - wiki/2026-06-14-autoware.md
---

# ros2_controllers

## 基本信息

- 类型：ros2_control 通用控制器插件集合
- 官方仓库：https://github.com/ros-controls/ros2_controllers.git
- 官方文档：https://control.ros.org/
- 默认分支：`master`
- 主要发行版分支：`humble`、`jazzy`、`kilted`
- 快照提交：`58969bf363185e941da1f6077ad07e9b15079d84`
- 最后提交时间：2026-06-19
- 最后提交标题：`Final test cleanup - call appropriate lifecycle transitions (#2429)`
- 当前包版本：`6.7.0`
- 主要语言：C++、Python、reStructuredText、YAML
- 分析方式：静态源码、文档、package 和 CI 分析；未编译运行

## 当前判断

ros2_controllers 是 ros2_control 的标准控制器集合，适合直接复用或作为自研控制器模板。它覆盖移动底盘、机械臂轨迹、PID、导纳、夹爪、传感器 broadcaster 等执行层能力；不负责导航规划、运动规划、硬件驱动或自动驾驶安全门控。

## 主要内容

### 移动底盘

- `diff_drive_controller`
- `mecanum_drive_controller`
- `omni_wheel_drive_controller`
- `ackermann_steering_controller`
- `bicycle_steering_controller`
- `tricycle_controller`
- `tricycle_steering_controller`
- `steering_controllers_library`

### 机械臂与执行器

- `joint_trajectory_controller`
- `pid_controller`
- `admittance_controller`
- `forward_command_controller`
- `parallel_gripper_controller`
- `motion_primitives_controllers`
- `gpio_controllers`

### Broadcasters

- `joint_state_broadcaster`
- `force_torque_sensor_broadcaster`
- `imu_sensor_broadcaster`
- `gps_sensor_broadcaster`
- `range_sensor_broadcaster`
- `pose_broadcaster`
- `state_interfaces_broadcaster`
- `magnetometer_broadcaster`

## 关键边界

- `diff_drive_controller` 把 body twist 转为 wheel velocity，不做路径规划和避障。
- steering controllers 做运动学逆解和 odometry，不做路径跟踪闭环。
- `joint_trajectory_controller` 执行 joint trajectory，不生成轨迹。
- broadcaster 使用 controller interface，但只发布状态，不发命令。
- 安全门控、急停、功能安全和车辆模式管理必须由上层系统和硬件接口补齐。

## 与现有条目的关系

- `ros2_control`：提供框架、资源管理和硬件接口。
- `ros2_controllers`：提供可加载控制器插件。
- `Navigation2`：可通过底盘控制器把速度命令落到硬件。
- `Autoware`：可借鉴执行层接口管理，但整车命令门控和安全链仍在 Autoware/Apollo 这类系统中。

## 关联笔记

- `notes/2026-06-24-ros2-controllers-common-controller-plugins.md`
- `wiki/2026-06-24-ros2-control.md`
- `wiki/2026-06-13-navigation2.md`
- `wiki/2026-06-14-autoware.md`

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `58969bf` 完成控制器类别、关键接口、工程边界和 ros2_control 关系建档。
