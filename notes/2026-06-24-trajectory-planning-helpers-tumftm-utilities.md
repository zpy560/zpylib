---
id: "20260624-trajectory-planning-helpers-tumftm-utilities"
title: "trajectory_planning_helpers：TUM FTM 轨迹规划工具函数库"
type: "note"
source: "raw/2026-06-24-trajectory-planning-helpers-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-trajectory-planning-helpers.md
---

# trajectory_planning_helpers：TUM FTM 轨迹规划工具函数库

## 一句话结论

trajectory_planning_helpers 是车辆轨迹规划中的工具函数库，适合复用几何、轨迹处理和规划辅助逻辑；它不是完整规划器。

## 原文要点

- 仓库来自 TUMFTM。
- README 以 Description 开头。
- 当前 `master` HEAD 为 `aa950f6`。

## 我的判断

这类 helper 库很适合补齐工程算法里的“胶水层”：坐标、曲线、插值、轨迹检查和辅助计算。它的价值不在单个大算法，而在减少重复实现。

## 可复用内容

- 车辆轨迹规划辅助函数组织方式。
- 轨迹几何处理工具。
- 自动驾驶规划中可复用的小函数边界。

## 疑问与冲突

- 需要继续读具体函数列表，才能判断覆盖哪些规划子问题。
- 不是系统框架，也不负责控制闭环。

## 原料

- `raw/2026-06-24-trajectory-planning-helpers-repository-snapshot.md`

