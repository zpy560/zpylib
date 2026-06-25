---
id: "20260624-212211-cartographer-note"
title: "Cartographer：实时 2D/3D SLAM 系统"
type: "note"
source: "raw/2026-06-24-cartographer-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-cartographer.md
---

# Cartographer：实时 2D/3D SLAM 系统

## 结论

Cartographer 值得加入控制/规划知识库。适合多传感器 SLAM、定位建图和导航地图生成历史基线。

## 事实摘录

- 远端仓库：`cartographer-project/cartographer`
- 当前核对 HEAD：`877157a0d91788a7700221d87232d412cb3c1ef4`
- README 定位为 real-time simultaneous localization and mapping in 2D and 3D across multiple platforms and sensor configurations。

## 对规划控制的意义

- 可作为 实时 2D/3D SLAM 系统 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
