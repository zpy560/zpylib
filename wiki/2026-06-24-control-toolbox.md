---
id: "20260624-control-toolbox"
title: "Control Toolbox"
type: "entity"
source: "raw/2026-06-24-control-toolbox-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-24-control-toolbox-optimal-control-library.md
  - wiki/2026-06-24-crocoddyl.md
---

# Control Toolbox

## 基本信息

- 类型：机器人控制、估计、优化和运动规划 C++ 库
- 官方仓库：https://github.com/ethz-adrl/control-toolbox
- 快照提交：`7d36e42ff665c9f4b6c5f3e4ddce04a0ab41628a`
- 快照日期：2026-06-24

## 当前结论

Control Toolbox 适合研究 C++ 最优控制库设计，但维护状态削弱了作为新项目依赖的优先级。

## 核心依据

- README 覆盖 control、estimation、optimization、motion planning。
- 支持 iLQR/iLQG、GNMS、DMS、MPC 等。
- README 明确提示维护稀疏。

## 不同观点与冲突

- 作为架构参考：有价值。
- 作为新项目生产依赖：需谨慎。

## 关联笔记

- `notes/2026-06-24-control-toolbox-optimal-control-library.md`
- `wiki/2026-06-24-crocoddyl.md`

## 待补资料

- 对照 OCS2 与 Control Toolbox 的 solver interface 和维护状态。

## 更新记录

- 2026-06-24：基于远端 HEAD `7d36e42` 首次建档。

