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
- 快照日期：2026-06-24

## 当前结论

EGO-Planner 是四旋翼快速局部规划参考，重点是 ESDF-free 梯度规划。新项目应同时评估 EGO-Swarm。

## 核心依据

- README 明确称为 ESDF-free gradient-based local planner。
- README 声称规划时间约 1 ms。
- README 明确推荐 EGO-Swarm 作为演进版本。

## 不同观点与冲突

- 作为无人机局部规划算法参考：优先级高。
- 作为当前最推荐版本：需看 EGO-Swarm。
- 作为地面车规划：不适用。

## 关联笔记

- `notes/2026-06-24-ego-planner-esdf-free-local-planner.md`
- `wiki/2026-06-24-fast-planner.md`

## 待补资料

- 后续应单独分析 EGO-Swarm。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `bfda512` 首次建档。

