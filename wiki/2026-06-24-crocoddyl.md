---
id: "20260624-crocoddyl"
title: "Crocoddyl"
type: "entity"
source: "raw/2026-06-24-crocoddyl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-crocoddyl-robotics-optimal-control.md
  - wiki/2026-06-24-pinocchio.md
  - wiki/2026-06-24-control-toolbox.md
---

# Crocoddyl

## 基本信息

- 类型：机器人最优控制求解库
- 官方仓库：https://github.com/loco-3d/crocoddyl
- 快照提交：`da3d18068cac75f17719d022a5f79fd2d266dd0a`
- 快照日期：2026-06-24

## 当前结论

Crocoddyl 适合纳入最优控制工具链，重点是机器人动力学系统的轨迹优化和反馈控制问题。

## 核心依据

- loco-3d 生态仓库。
- README 提供完整项目文档入口。
- 适合与 Pinocchio 结合理解。

## 不同观点与冲突

- 作为机器人最优控制库：优先级高。
- 作为通用路径规划器：不适用。

## 关联笔记

- `notes/2026-06-24-crocoddyl-robotics-optimal-control.md`
- `wiki/2026-06-24-pinocchio.md`
- `wiki/2026-06-24-control-toolbox.md`

## 待补资料

- 对比 Crocoddyl、OCS2、Control Toolbox 的 solver abstraction。

## 更新记录

- 2026-06-24：基于远端 HEAD `da3d180` 首次建档。

