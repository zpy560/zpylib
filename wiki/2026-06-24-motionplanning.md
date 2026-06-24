---
id: "20260624-motionplanning"
title: "MotionPlanning"
type: "entity"
source: "raw/2026-06-24-motionplanning-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-motionplanning-autonomous-driving-planning-control-demos.md
  - wiki/2026-06-24-pythonrobotics.md
  - wiki/2026-06-15-hybrid-a-star.md
---

# MotionPlanning

## 基本信息

- 类型：自动驾驶规划控制 Python 示例库
- 官方仓库：https://github.com/zhm-real/MotionPlanning
- 快照分支：`master`
- 快照提交：`7a6b43d9c1eecf97ae6bf1aa23bc4d5aaf0e1817`
- 快照日期：2026-06-24

## 当前结论

MotionPlanning 适合作为“规划器 + 控制器”组合学习库。它的价值在车辆规划控制示例集中，不在工程完整性。

## 核心依据

- README 明确列出 Hybrid A*、Frenet、H-OBCA。
- README 同时列出 Pure Pursuit、Stanley、LQR、Linear MPC 等控制器。
- 使用车辆模型而不是纯二维点机器人模型。

## 不同观点与冲突

- 作为车辆规划控制学习：优先级高。
- 作为生产规划器：不适用。
- 作为优化避障参考：H-OBCA 未完成，只能看方向。

## 关联笔记

- `notes/2026-06-24-motionplanning-autonomous-driving-planning-control-demos.md`
- `wiki/2026-06-24-pythonrobotics.md`
- `wiki/2026-06-15-hybrid-a-star.md`

## 待补资料

- 对比 Hybrid A* 与现有 Hybrid A Star ROS1 笔记。
- 抽取 Frenet 与 Linear MPC 示例的变量定义和约束。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `7a6b43d` 首次建档。

