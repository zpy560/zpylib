---
id: "20260624-commonroad-route-planner"
title: "CommonRoad Route Planner"
type: "entity"
source: "raw/2026-06-24-commonroad-route-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-commonroad-route-planner-reference-path.md
  - wiki/2026-06-24-commonroad-drivability-checker.md
---

# CommonRoad Route Planner

## 基本信息

- 类型：CommonRoad 路线与参考路径规划器
- 官方仓库：https://github.com/CommonRoad/commonroad-route-planner
- 快照提交：`53b284e4c5cc4a63087f897618c127349a6e1218`
- 快照日期：2026-06-24

## 当前结论

CommonRoad Route Planner 是 CommonRoad 生态里的路线/参考路径工具，适合自动驾驶规划算法评估前处理。

## 核心依据

- README 明确定位为 route and reference path planner。
- 面向 CommonRoad 项目。
- 提供 PyPI 包和文档入口。

## 不同观点与冲突

- 作为参考路径生成器：有价值。
- 作为完整规划控制栈：不适用。

## 关联笔记

- `notes/2026-06-24-commonroad-route-planner-reference-path.md`
- `wiki/2026-06-24-commonroad-drivability-checker.md`

## 待补资料

- 与 CommonRoad Drivability Checker 建立场景生成和验证流程。

## 更新记录

- 2026-06-24：基于远端 HEAD `53b284e` 首次建档。

