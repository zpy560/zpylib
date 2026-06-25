---
id: "20260624-212204-fcl-note"
title: "FCL：Flexible Collision Library"
type: "note"
source: "raw/2026-06-24-fcl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-fcl.md
---

# FCL：Flexible Collision Library

## 结论

FCL 值得加入控制/规划知识库。适合运动规划中的碰撞检测、距离查询和连续碰撞检测。

## 事实摘录

- 远端仓库：`flexible-collision-library/fcl`
- 当前核对 HEAD：`e5efcc41b57b2d0da3bf183480f1298a6d531f44`
- README 描述 FCL 支持 collision detection、distance computation、tolerance verification、continuous collision detection 和 contact information。

## 对规划控制的意义

- 可作为 Flexible Collision Library 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
