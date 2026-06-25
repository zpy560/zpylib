---
id: "20260624-211027-ros-control-note"
title: "ros_control：ROS1 通用控制框架"
type: "note"
source: "raw/2026-06-24-ros-control-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-ros-control.md
---

# ros_control：ROS1 通用控制框架

## 结论

`ros_control` 是 ROS1 控制框架基线，值得与已入库的 `ros2_control` 对照。它不做高层规划，但决定了机器人硬件接口、控制器加载和控制循环的组织方式。

## 事实摘录

- 远端仓库：`ros-controls/ros_control`
- 当前核对 HEAD：`633c3746a9b109056658b862ff7d765cc85ec9da`
- README 指向 ros.org 上的 `ros_control` 文档。
- 支持分支覆盖 Indigo、Kinetic、Lunar、Melodic、Noetic。
- 论文题目为 `ros_control: A generic and simple control framework for ROS`。

## 对规划控制的意义

- 对 ROS1 机器人：规划输出最终通常通过控制器和 hardware interface 执行。
- 对 ROS2 学习：理解 `ros_control` 有助于理解 `ros2_control` 为什么引入生命周期和新接口设计。
- 对自动驾驶底盘：可借鉴 controller manager 和资源接口思想。

## 使用建议

维护 ROS1 项目时读它；新 ROS2 项目优先读 `ros2_control`。两者对照时关注 hardware interface、controller lifecycle、controller manager 和 realtime loop。

