---
id: "20260624-teb-local-planner"
title: "teb_local_planner"
type: "entity"
source: "raw/2026-06-24-teb-local-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-teb-local-planner-timed-elastic-band.md
  - wiki/2026-06-24-mpc-local-planner.md
---

# teb_local_planner

## 基本信息

- 类型：ROS Timed Elastic Band 局部规划器
- 官方仓库：https://github.com/rst-tu-dortmund/teb_local_planner
- 快照提交：`8f429538601d7c4102aa345e8b5ba8dfae989c00`
- 快照日期：2026-06-24

## 当前结论

teb_local_planner 是局部轨迹优化的重要参考，适合研究时间化局部规划，不替代全局导航框架。

## 核心依据

- README 标题明确为 ROS Package。
- 项目边界聚焦局部规划。

## 不同观点与冲突

- 作为局部规划算法参考：优先级高。
- 作为完整导航系统：不适用。

## 关联笔记

- `notes/2026-06-24-teb-local-planner-timed-elastic-band.md`
- `wiki/2026-06-24-mpc-local-planner.md`

## 待补资料

- 对比 TEB 与 MPC local planner 的优化变量和约束表达。

## 更新记录

- 2026-06-24：基于远端 HEAD `8f42953` 首次建档。

