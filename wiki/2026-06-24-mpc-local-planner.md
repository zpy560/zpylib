---
id: "20260624-mpc-local-planner"
title: "mpc_local_planner"
type: "entity"
source: "raw/2026-06-24-mpc-local-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-mpc-local-planner-ros-local-mpc.md
  - wiki/2026-06-24-teb-local-planner.md
---

# mpc_local_planner

## 基本信息

- 类型：ROS MPC 局部规划器
- 官方仓库：https://github.com/rst-tu-dortmund/mpc_local_planner
- 快照分支：`master`
- 快照提交：`5b4e465fec718245484e8668e6dd45539ca37983`
- 快照日期：2026-06-24

## 当前结论

mpc_local_planner 是研究 ROS 局部 MPC 的参考仓库，适合和 TEB、Nav2 MPPI、acados 等对照。

## 核心依据

- README 标题明确为 ROS Package。
- 项目边界聚焦 MPC local planner。

## 不同观点与冲突

- 作为局部 MPC 参考：优先级高。
- 作为全局规划或完整系统：不适用。

## 关联笔记

- `notes/2026-06-24-mpc-local-planner-ros-local-mpc.md`
- `wiki/2026-06-24-teb-local-planner.md`

## 待补资料

- 对比 MPC local planner 与 Nav2 MPPI controller 的模型、代价和约束。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `5b4e465` 首次建档。

