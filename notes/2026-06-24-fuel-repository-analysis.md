---
id: "20260624-212212-fuel-note"
title: "FUEL：Fast UAV Exploration 框架"
type: "note"
source: "raw/2026-06-24-fuel-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-fuel.md
---

# FUEL：Fast UAV Exploration 框架

## 结论

FUEL 值得加入控制/规划知识库。适合无人机主动探索、frontier information structure、层级规划和最小时间轨迹。

## 事实摘录

- 远端仓库：`HKUST-Aerial-Robotics/FUEL`
- 当前核对 HEAD：`662dd23c7b52b258d3c4a0155ff6632118e8984f`
- README 定位为 Fast UAV Exploration framework，使用 FIS 增量维护探索信息，层级 planner 规划 frontier coverage、viewpoints 和 minimum-time trajectories。

## 对规划控制的意义

- 可作为 Fast UAV Exploration 框架 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
