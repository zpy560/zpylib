---
id: "20260624-212207-qpoases-note"
title: "qpOASES：在线 active-set QP 求解器"
type: "note"
source: "raw/2026-06-24-qpoases-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-qpoases.md
---

# qpOASES：在线 active-set QP 求解器

## 结论

qpOASES 值得加入控制/规划知识库。适合 MPC、实时控制和参数化 QP 的历史/工程参考。

## 事实摘录

- 远端仓库：`coin-or/qpOASES`
- 当前核对 HEAD：`9e40af7d170f440b7887fc4f9cf162f3f3ae24e8`
- README.txt 定位为 open-source C++ implementation of the online active set strategy，源自 parametric quadratic programming。

## 对规划控制的意义

- 可作为 在线 active-set QP 求解器 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
