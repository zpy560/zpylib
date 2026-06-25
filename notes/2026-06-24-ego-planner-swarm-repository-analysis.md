---
id: "20260624-212213-ego-planner-swarm-note"
title: "EGO-Swarm：去中心化四旋翼 swarm navigation"
type: "note"
source: "raw/2026-06-24-ego-planner-swarm-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-ego-planner-swarm.md
---

# EGO-Swarm：去中心化四旋翼 swarm navigation

## 结论

EGO-Swarm 值得加入控制/规划知识库。适合多机器人未知障碍环境自主导航、分布式避障和 swarm 规划。

## 事实摘录

- 远端仓库：`ZJU-FAST-Lab/ego-planner-swarm`
- 当前核对 HEAD：`92fe9f7227b2da819133eb8e0e8c7fc000f6ae20`
- README 说明它从 EGO-Planner 扩展到 swarm navigation，是 decentralized and asynchronous quadrotor swarm system。

## 对规划控制的意义

- 可作为 去中心化四旋翼 swarm navigation 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
