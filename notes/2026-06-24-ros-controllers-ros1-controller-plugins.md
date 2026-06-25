---
id: "20260624-211031-ros-controllers-note"
title: "ros_controllers：ROS1 控制器插件集合"
type: "note"
source: "raw/2026-06-24-ros-controllers-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-ros-controllers.md
---

# ros_controllers：ROS1 控制器插件集合

## 结论

`ros_controllers` 是 ROS1 控制器插件集合，应和 `ros_control` 成对理解。它不是框架本体，而是框架中可加载的常用控制器实现集合。

## 事实摘录

- 远端仓库：`ros-controls/ros_controllers`
- 当前核对 HEAD：`c2348e85abf35cf33cf654a84d61db206abe9a73`
- README 指向 ros.org 上的 `ros_control` 和 `ros_controllers` 文档。
- 支持分支覆盖 Indigo、Kinetic、Lunar、Melodic、Noetic。
- README 引用 `ros_control` JOSS 论文。

## 对规划控制的意义

- 对 ROS1 执行链：控制器插件是规划轨迹落到关节/底盘命令的关键层。
- 对 ROS2 对照：已入库的 `ros2_controllers` 是它的现代继任参考。
- 对工程学习：应关注 controller interface、joint trajectory controller、effort/position/velocity 控制器等实现。

## 使用建议

维护 ROS1 项目时阅读；新 ROS2 项目看 `ros2_controllers`。对照学习时把 `ros_control` 视为框架，把 `ros_controllers` 视为插件集合。

