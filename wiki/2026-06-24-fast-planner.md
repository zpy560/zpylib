---
id: "20260624-fast-planner"
title: "Fast-Planner"
type: "entity"
source: "raw/2026-06-24-fast-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-fast-planner-quadrotor-fast-flight-planning.md
  - wiki/2026-06-24-ego-planner.md
  - wiki/2026-06-24-mav-trajectory-generation.md
---

# Fast-Planner

## 基本信息

- 类型：四旋翼快速飞行规划框架
- 官方仓库：https://github.com/HKUST-Aerial-Robotics/Fast-Planner
- 快照分支：`master`
- 快照提交：`41be219fe4ecc43bf0e0c2b42a523f8755ccc0bd`
- 快照日期：2026-06-24

## 当前结论

Fast-Planner 是无人机复杂未知环境规划的重要参考，适合研究局部重规划和轨迹优化。

## 核心依据

- README 明确面向 quadrotor fast flight。
- 支撑 ego-planner、FUEL、RACER 等项目。
- ROS Melodic/Noetic 测试说明明确。

## 不同观点与冲突

- 作为无人机规划框架：优先级高。
- 作为地面车规划控制：不适用。

## 关联笔记

- `notes/2026-06-24-fast-planner-quadrotor-fast-flight-planning.md`
- `wiki/2026-06-24-ego-planner.md`
- `wiki/2026-06-24-mav-trajectory-generation.md`

## 待补资料

- 细读 B-spline trajectory optimization 与 topological path 部分。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `41be219` 首次建档。

