---
id: "20260624-211032-ros-controllers-wiki"
title: "ros_controllers"
type: "entity"
source: "notes/2026-06-24-ros-controllers-ros1-controller-plugins.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-ros-controllers-ros1-controller-plugins.md
---

# ros_controllers

## 定位

`ros_controllers` 是 ROS1 的通用控制器插件集合，配套 `ros_control` 使用。

## 适合研究的问题

- 常见 joint/controller 插件如何组织。
- controller plugin 如何接入 `ros_control`。
- ROS1 到 ROS2 控制器集合的接口演进。

## 使用边界

它不是硬件抽象框架，也不是高层 planner。框架看 `ros_control`，ROS2 控制器集合看 `ros2_controllers`。

## 入库来源

- 单源笔记：../notes/2026-06-24-ros-controllers-ros1-controller-plugins.md
- 仓库：https://github.com/ros-controls/ros_controllers

