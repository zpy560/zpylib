---
id: "20260624-212209-rbdl-note"
title: "RBDL：Rigid Body Dynamics Library"
type: "note"
source: "raw/2026-06-24-rbdl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-rbdl.md
---

# RBDL：Rigid Body Dynamics Library

## 结论

RBDL 值得加入控制/规划知识库。适合控制和轨迹优化中的 ABA/RNEA/CRBA、Jacobian、约束和闭链模型。

## 事实摘录

- 远端仓库：`rbdl/rbdl`
- 当前核对 HEAD：`e9af3bb013eedf25328332e340027e41da53a6bc`
- README 描述其包含 ABA、RNEA、CRBA、Jacobians、forward/inverse kinematics、contacts/collisions constraints 和 closed-loop models。

## 对规划控制的意义

- 可作为 Rigid Body Dynamics Library 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
