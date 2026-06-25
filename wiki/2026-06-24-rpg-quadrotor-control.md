---
id: "20260624-rpg-quadrotor-control"
title: "RPG Quadrotor Control"
type: "entity"
source: "raw/2026-06-24-rpg-quadrotor-control-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-rpg-quadrotor-control-aggressive-flight.md
  - wiki/2026-06-24-mav-trajectory-generation.md
  - wiki/2026-06-24-px4-autopilot.md
---

# RPG Quadrotor Control

## 基本信息

- 类型：四旋翼轨迹跟踪与飞行控制研究框架
- 官方仓库：https://github.com/uzh-rpg/rpg_quadrotor_control
- 快照分支：`master`
- 快照提交：`22b55b085546a3322c302a68c2b67108a092a298`
- 快照日期：2026-06-24

## 当前结论

RPG Quadrotor Control 是四旋翼控制层参考，适合研究高速轨迹跟踪，不是通用规划库。

## 核心依据

- README 明确是 ROS research code。
- 包含完整 quadrotor flying framework。
- 理论对应 RA-L 2017/2018 论文。

## 不同观点与冲突

- 作为四旋翼控制参考：优先级高。
- 作为生产飞控：不适用。

## 关联笔记

- `notes/2026-06-24-rpg-quadrotor-control-aggressive-flight.md`
- `wiki/2026-06-24-mav-trajectory-generation.md`

## 待补资料

- 对比 PX4 控制链和 RPG 控制框架。

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `22b55b0` 首次建档。

