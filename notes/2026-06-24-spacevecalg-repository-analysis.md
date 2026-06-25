---
id: "20260624-212220-spacevecalg-note"
title: "SpaceVecAlg：Spatial Vector Algebra 库"
type: "note"
source: "raw/2026-06-24-spacevecalg-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-spacevecalg.md
---

# SpaceVecAlg：Spatial Vector Algebra 库

## 结论

SpaceVecAlg 值得加入控制/规划知识库。适合刚体动力学、全身控制和 Featherstone 空间向量代数基础。

## 事实摘录

- 远端仓库：`jrl-umi3218/SpaceVecAlg`
- 当前核对 HEAD：`4f53563b3f37630c4716b90ddbdf5a0576acef5f`
- README 定位为用 Eigen3 实现 Spatial Vector Algebra，基于 Featherstone 书籍 Appendix A。

## 对规划控制的意义

- 可作为 Spatial Vector Algebra 库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
