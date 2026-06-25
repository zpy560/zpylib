---
id: "20260624-mav-trajectory-generation"
title: "mav_trajectory_generation"
type: "entity"
source: "raw/2026-06-24-mav-trajectory-generation-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-mav-trajectory-generation-polynomial-trajectories.md
  - wiki/2026-06-24-fast-planner.md
  - wiki/2026-06-24-rpg-quadrotor-control.md
---

# mav_trajectory_generation

## 基本信息

- 类型：MAV 多项式轨迹生成与优化工具
- 官方仓库：https://github.com/ethz-asl/mav_trajectory_generation
- 快照分支：`master`
- 快照提交：`7aeebd9f819217502fd1c5489da49efadf90d411`
- 快照日期：2026-06-24

## 当前结论

mav_trajectory_generation 是无人机轨迹生成层工具，适合研究多项式轨迹和 MAV 轨迹优化。

## 核心依据

- README 明确是 polynomial trajectory generation and optimization。
- 特别适合 rotary-wing MAVs。
- 引用 aggressive quadrotor flight 相关论文。

## 不同观点与冲突

- 作为轨迹生成工具：优先级高。
- 作为完整规划系统：不适用。

## 关联笔记

- `notes/2026-06-24-mav-trajectory-generation-polynomial-trajectories.md`
- `wiki/2026-06-24-fast-planner.md`

## 待补资料

- 对比 mav_trajectory_generation 与 Ruckig/toppra 在轨迹时间化上的差异。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `7aeebd9` 首次建档。

