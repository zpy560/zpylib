---
id: "20260624-ego-planner"
title: "EGO-Planner"
type: "entity"
source: "raw/2026-06-24-ego-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-ego-planner-esdf-free-local-planner.md
  - wiki/2026-06-24-fast-planner.md
---

# EGO-Planner

## 基本信息

- 类型：四旋翼 ESDF-free 局部规划器
- 官方仓库：https://github.com/ZJU-FAST-Lab/ego-planner
- 快照分支：`master`
- 快照提交：`bfda51284c8c1b476043255a8145ef925a3778a5`
- 首次快照日期：2026-06-24
- 最近核对日期：2026-07-13

## 当前结论

EGO-Planner 是四旋翼 ESDF-free 局部重规划的经典源码参考，核心链路为「局部占据栅格 → A* 初始化 → B-spline 梯度优化 → FSM 重规划与碰撞检查」。它更适合算法学习和旧 ROS 1 系统对照；2026 年新项目应优先评估 EGO-Swarm，而不是直接以本仓库为工程基线。

## 核心依据

- README 明确称为 ESDF-free gradient-based local planner。
- README 声称规划时间约 1 ms。
- README 明确推荐 EGO-Swarm 作为演进版本。
- 2026-07-13 核对时，`master` 仍停在 `bfda512`，最近提交日期为 2025-03-08。
- 源码模块包含局部地图、A*、B-spline 优化、重规划管理和四旋翼仿真，属于 ROS 1 catkin 工程。

## 不同观点与冲突

- 作为无人机局部规划算法参考：优先级高。
- 作为当前最推荐版本：需看 EGO-Swarm。
- 作为地面车规划：不适用。
- 作为现代 ROS 2 工程基线：不合适；官方将 ROS 2 支持指向 EGO-Swarm 分支。
- 作为可直接商用的整仓依赖：需谨慎；根许可证为 GPLv3，且内嵌包许可证声明并不完全一致。

## 关联笔记

- `notes/2026-06-24-ego-planner-esdf-free-local-planner.md`
- `wiki/2026-06-24-fast-planner.md`

## 待补资料

- 在目标 Ubuntu／ROS 环境做一次可重复构建和仿真验证。
- 若用于地面车研究，只抽取局部地图、重规划 FSM 和轨迹优化思想，不直接迁移整套四旋翼模型。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `bfda512` 首次建档。
- 2026-07-13：重新核对官方仓库和源码结构，补充模块链路、维护状态、ROS 版本、许可与适用边界；远端提交未变化。
