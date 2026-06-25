---
id: "20260624-212218-tasks-note"
title: "Tasks：实时约束优化机器人控制任务库"
type: "note"
source: "raw/2026-06-24-tasks-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-tasks.md
---

# Tasks：实时约束优化机器人控制任务库

## 结论

Tasks 值得加入控制/规划知识库。适合 humanoid/whole-body control 中任务、约束、接触和碰撞规避建模。

## 事实摘录

- 远端仓库：`jrl-umi3218/Tasks`
- 当前核对 HEAD：`72bac026d5eaa8efa8b170d722f287d7d2b7b04f`
- README 定位为 real time control of robots and kinematic trees using constrained optimization；特性包括 dynamics、friction cones、static contacts、limits、collision avoidance、multi-robot contact。

## 对规划控制的意义

- 可作为 实时约束优化机器人控制任务库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
