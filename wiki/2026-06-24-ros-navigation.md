---
id: "20260624-ros-navigation"
title: "ROS Navigation"
type: "entity"
source: "raw/2026-06-24-ros-navigation-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-ros-navigation-ros1-2d-navigation-stack.md
  - wiki/2026-06-13-navigation2.md
---

# ROS Navigation

## 基本信息

- 类型：ROS1 二维移动机器人导航栈
- 官方仓库：https://github.com/ros-planning/navigation
- 快照提交：`f44bb1fc2810399165115cc98b530fe4b9397c18`
- 快照日期：2026-06-24

## 当前结论

ROS Navigation 是 Nav2 的历史参照物，适合理解 ROS1 `move_base` 架构和二维导航插件体系。

## 核心依据

- README 明确为 2D navigation stack。
- 输入 odometry、sensor streams、goal pose，输出 safe velocity commands。

## 不同观点与冲突

- 作为 ROS1 导航基线：优先级高。
- 作为 ROS2 新项目首选：不适用。

## 关联笔记

- `notes/2026-06-24-ros-navigation-ros1-2d-navigation-stack.md`
- `wiki/2026-06-13-navigation2.md`

## 待补资料

- 对比 ROS Navigation `move_base` 与 Nav2 BT Navigator/Planner Server/Controller Server。

## 更新记录

- 2026-06-24：基于远端 HEAD `f44bb1f` 首次建档。

