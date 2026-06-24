---
id: "20260624-commonroad-drivability-checker"
title: "CommonRoad Drivability Checker"
type: "entity"
source: "raw/2026-06-24-commonroad-drivability-checker-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-commonroad-drivability-checker-validation-toolbox.md
  - wiki/2026-06-24-commonroad-route-planner.md
---

# CommonRoad Drivability Checker

## 基本信息

- 类型：自动驾驶规划轨迹可行性验证工具箱
- 官方仓库：https://github.com/CommonRoad/commonroad-drivability-checker
- 快照分支：`master`
- 快照提交：`7127f2e7f960632b3d7ff7805936a1e91b677569`
- 快照日期：2026-06-24

## 当前结论

CommonRoad Drivability Checker 是规划结果验证层工具，适合检查碰撞、运动学可行性和道路合规性。

## 核心依据

- README 明确说明 collision avoidance、kinematic feasibility、road-compliance checks。
- 兼容 CommonRoad benchmark suite。
- 提供 Python 包和源码构建路径。

## 不同观点与冲突

- 作为验证工具：优先级高。
- 作为规划器或控制器：不适用。

## 关联笔记

- `notes/2026-06-24-commonroad-drivability-checker-validation-toolbox.md`
- `wiki/2026-06-24-commonroad-route-planner.md`

## 待补资料

- 用一个 CommonRoad 场景跑通 route planner + drivability checker 流程。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `7127f2e` 首次建档。

