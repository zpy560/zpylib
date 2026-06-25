---
id: "20260624-212214-racer-note"
title: "RACER：去中心化多 UAV 协同探索"
type: "note"
source: "raw/2026-06-24-racer-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-racer.md
---

# RACER：去中心化多 UAV 协同探索

## 结论

RACER 值得加入控制/规划知识库。适合通信受限多机探索、coverage allocation 和鲁棒协同规划。

## 事实摘录

- 远端仓库：`SYSU-STAR/RACER`
- 当前核对 HEAD：`049c332e3634ef72d8beb155b4c13dc91ca52916`
- README 定位为 Rapid Collaborative Exploration using decentralized UAVs，异步有限通信、无需中心控制，并优化 coverage paths 和 workload allocations。

## 对规划控制的意义

- 可作为 去中心化多 UAV 协同探索 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
