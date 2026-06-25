---
id: "20260624-212223-osqp-eigen-note"
title: "osqp-eigen：OSQP 的 Eigen C++ wrapper"
type: "note"
source: "raw/2026-06-24-osqp-eigen-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-osqp-eigen.md
---

# osqp-eigen：OSQP 的 Eigen C++ wrapper

## 结论

osqp-eigen 值得加入控制/规划知识库。适合 C++ 控制/规划代码中接入 OSQP 解凸 QP。

## 事实摘录

- 远端仓库：`robotology/osqp-eigen`
- 当前核对 HEAD：`8b3d4c4be9f4c0e9deb6375ac8e89bc84606d125`
- README 定位为 Simple C++ wrapper for OSQP，依赖 OSQP 和 Eigen3，C++14。

## 对规划控制的意义

- 可作为 OSQP 的 Eigen C++ wrapper 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
