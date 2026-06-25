---
id: "20260624-212206-ifopt-note"
title: "ifopt：Eigen-based 非线性规划接口"
type: "note"
source: "raw/2026-06-24-ifopt-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-ifopt.md
---

# ifopt：Eigen-based 非线性规划接口

## 结论

ifopt 值得加入控制/规划知识库。适合把机器人优化问题统一表达后交给 Ipopt/Snopt 等 NLP solver。

## 事实摘录

- 远端仓库：`ethz-adrl/ifopt`
- 当前核对 HEAD：`4d6267bfefbaaa97e079c9aa163ebd477fce064d`
- README 定位为 modern lightweight Eigen-based C++ interface to nonlinear programming solvers such as Ipopt and Snopt。

## 对规划控制的意义

- 可作为 Eigen-based 非线性规划接口 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
