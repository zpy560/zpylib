---
id: "20260624-212222-qpsolvers-note"
title: "qpsolvers：Python QP solver 统一接口"
type: "note"
source: "raw/2026-06-24-qpsolvers-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-qpsolvers.md
---

# qpsolvers：Python QP solver 统一接口

## 结论

qpsolvers 值得加入控制/规划知识库。适合快速切换 QP 后端、验证控制/规划优化问题。

## 事实摘录

- 远端仓库：`qpsolvers/qpsolvers`
- 当前核对 HEAD：`679458f48aadf15541ca1658f30d9fee75d3ff52`
- README 提供 solve_qp 函数求解凸二次规划，返回后端 QP solver 的 primal solution 或失败时 None。

## 对规划控制的意义

- 可作为 Python QP solver 统一接口 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
