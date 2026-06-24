---
id: "20260624-pinocchio"
title: "Pinocchio"
type: "entity"
source: "raw/2026-06-24-pinocchio-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-pinocchio-robot-dynamics-library.md
  - wiki/2026-06-24-crocoddyl.md
---

# Pinocchio

## 基本信息

- 类型：机器人运动学与动力学库
- 官方仓库：https://github.com/stack-of-tasks/pinocchio
- 快照提交：`893ed4dab1eba0cf3e488a9446a0e1d5f714522c`
- 快照日期：2026-06-24

## 当前结论

Pinocchio 是机器人控制和轨迹优化的模型计算基础库，不是独立规划控制系统。

## 核心依据

- stack-of-tasks 生态仓库。
- README 提供完整文档入口。
- 常作为最优控制和机器人动力学计算依赖。

## 不同观点与冲突

- 作为动力学基础设施：优先级高。
- 作为路径规划器：不适用。

## 关联笔记

- `notes/2026-06-24-pinocchio-robot-dynamics-library.md`
- `wiki/2026-06-24-crocoddyl.md`

## 待补资料

- 对比 Pinocchio 与 Drake 在多体动力学建模上的边界。

## 更新记录

- 2026-06-24：基于远端 HEAD `893ed4d` 首次建档。

