---
id: "20260624-210039-moveit-ros1-note"
title: "MoveIt ROS1：机械臂运动规划框架"
type: "note"
source: "raw/2026-06-24-moveit-ros1-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-moveit-ros1.md
---

# MoveIt ROS1：机械臂运动规划框架

## 结论

ROS1 MoveIt 仍值得单独入库，因为它是大量机械臂运动规划工程的历史基线。知识库已有 MoveIt 2，本条的重点是 ROS1 版本的包结构、分支策略和与 MoveIt 2 的演进对照。

## 事实摘录

- 远端仓库：`ros-planning/moveit`
- 当前核对 HEAD：`a4febda3cce71b7beae48aa69f0a4c2cadebef45`
- README 定位：MoveIt Motion Planning Framework for ROS。
- README 指向 ROS 2 repository：`moveit/moveit2`。
- README 称其用于 commercial applications、prototyping designs、benchmarking algorithms。
- 包列表涉及 `moveit_core`、`moveit_planners`、`moveit_planners_ompl`、`moveit_ros_planning`、`moveit_ros_move_group`、`moveit_servo`、`moveit_msgs` 等。

## 对规划控制的意义

- 提供机械臂规划场景中的 robot model、planning scene、collision checking、planner plugin、trajectory execution 等完整框架视角。
- 适合和 MoveIt 2 对照，理解 ROS1 到 ROS2 的 API、执行模型和包维护变化。
- 对工业机械臂应用，MoveIt 与 Descartes 的关系值得进一步梳理：一个偏通用 motion planning，一个偏笛卡尔工艺路径。

## 使用建议

新 ROS 2 项目应优先看 MoveIt 2。只有维护 ROS1/Noetic 项目、阅读历史实现或比较架构演进时，才把 `ros-planning/moveit` 作为主要入口。

