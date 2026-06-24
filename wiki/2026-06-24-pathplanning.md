---
id: "20260624-pathplanning"
title: "PathPlanning"
type: "entity"
source: "raw/2026-06-24-pathplanning-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-pathplanning-search-sampling-algorithm-demos.md
  - wiki/2026-06-24-motionplanning.md
  - wiki/2026-06-24-pythonrobotics.md
---

# PathPlanning

## 基本信息

- 类型：路径规划算法示例库
- 官方仓库：https://github.com/zhm-real/PathPlanning
- 快照分支：`master`
- 快照提交：`89c200e0ab855010e2f892b6465b50dab002963c`
- 快照日期：2026-06-24

## 当前结论

PathPlanning 适合作为搜索和采样式路径规划算法的教学索引，不是工程导航框架。

## 核心依据

- README 明确覆盖 search-based 和 sampling-based planning。
- 算法列表覆盖 A*、D*、RRT、RRT*、FMT*、BIT* 等。
- 提供动画展示。

## 不同观点与冲突

- 作为路径规划算法地图：优先级高。
- 作为生产规划器：不适用。

## 关联笔记

- `notes/2026-06-24-pathplanning-search-sampling-algorithm-demos.md`
- `wiki/2026-06-24-motionplanning.md`
- `wiki/2026-06-24-pythonrobotics.md`

## 待补资料

- 对比 PathPlanning、PythonRobotics、OMPL 中 RRT 系列实现差异。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `89c200e` 首次建档。

