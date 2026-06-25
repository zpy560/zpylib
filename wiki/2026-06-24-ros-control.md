---
id: "20260624-211028-ros-control-wiki"
title: "ros_control"
type: "entity"
source: "notes/2026-06-24-ros-control-ros1-control-framework.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-ros-control-ros1-control-framework.md
---

# ros_control

## 定位

`ros_control` 是 ROS1 的通用机器人控制框架，负责硬件接口、控制器管理和控制循环组织。

## 适合研究的问题

- ROS1 控制器如何加载、启动、停止和更新。
- 硬件接口如何抽象 joint/state/command resources。
- `ros_control` 到 `ros2_control` 的架构演进。

## 使用边界

它不是 planner，也不是控制算法集合。控制器插件集合应看 `ros_controllers`，ROS2 新工程应优先看 `ros2_control`。

## 入库来源

- 单源笔记：../notes/2026-06-24-ros-control-ros1-control-framework.md
- 仓库：https://github.com/ros-controls/ros_control

