---
id: "20260624-212203-octomap-note"
title: "OctoMap：基于八叉树的概率三维地图框架"
type: "note"
source: "raw/2026-06-24-octomap-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-octomap.md
---

# OctoMap：基于八叉树的概率三维地图框架

## 结论

OctoMap 值得加入控制/规划知识库。适合三维占据地图、避障和机器人环境建模。

## 事实摘录

- 远端仓库：`octomap/octomap`
- 当前核对 HEAD：`f012f5f0a4f58cad19501833f9c0ea9d864427b6`
- README 定位为 Efficient Probabilistic 3D Mapping Framework Based on Octrees；octomap 使用 New BSD，octovis 相关库使用 GPL。

## 对规划控制的意义

- 可作为 基于八叉树的概率三维地图框架 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
