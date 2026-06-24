---
id: "20260624-moveit2-ros2-manipulation-motion-planning"
title: "MoveIt 2：ROS 2 机械臂运动规划框架"
type: "note"
source: "raw/2026-06-24-moveit2-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-moveit2.md
  - notes/2026-06-24-ompl-sampling-based-motion-planning-library.md
  - notes/2026-06-24-ros2-controllers-common-controller-plugins.md
---

# MoveIt 2：ROS 2 机械臂运动规划框架

## 一句话结论

MoveIt 2 是 ROS 2 机械臂运动规划框架，核心价值不只是规划算法，而是把机器人模型、规划场景、碰撞检测、运动规划、执行和 ROS 2 生态连接起来。

## 原文要点

- README 定位为 MoveIt Motion Planning Framework for ROS 2。
- 目标是机器人 manipulation 平台，支持商业应用开发、原型和算法 benchmark。
- 文档入口是 `moveit.picknik.ai`。
- 分支策略区分 `main` 开发分支和 Humble/Jazzy/Kilted 稳定发布分支。
- Buildfarm 包清单显示其包含 core、planners、kinematics、servo、task constructor 等模块。

## 我的判断

MoveIt 2 和 OMPL 是上下游关系：OMPL 更像算法库，MoveIt 2 是机械臂运动规划系统。对自动驾驶算法工程也有架构借鉴价值：规划问题、碰撞环境、执行接口和发行版分支必须分层。

## 可复用内容

- ROS 2 运动规划系统边界设计。
- Planning scene 与 collision checking 的工程组织。
- 版本分支策略：开发分支与 distro 稳定分支分离。

## 疑问与冲突

- MoveIt 2 面向 manipulation，不是车辆轨迹规划或移动机器人导航。
- 实际部署仍需 ros2_control、硬件接口和目标机器人配置配合。

## 原料

- `raw/2026-06-24-moveit2-repository-snapshot.md`

