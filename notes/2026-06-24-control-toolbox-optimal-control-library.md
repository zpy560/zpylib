---
id: "20260624-control-toolbox-optimal-control-library"
title: "Control Toolbox：机器人控制、估计与轨迹优化 C++ 库"
type: "note"
source: "raw/2026-06-24-control-toolbox-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-control-toolbox.md
  - notes/2026-06-24-crocoddyl-robotics-optimal-control.md
---

# Control Toolbox：机器人控制、估计与轨迹优化 C++ 库

## 一句话结论

Control Toolbox 是 ETH ADRL 的 C++ 控制与最优控制库，覆盖建模、估计、轨迹优化和 MPC；但 README 明确提示维护稀疏，因此更适合学习架构和历史实现，不宜贸然作为新项目核心依赖。

## 原文要点

- README 定位为 efficient C++ library for control, estimation, optimization and motion planning in robotics。
- 支持 iLQR/iLQG、GNMS、DMS 等最优控制算法。
- 接口覆盖 IPOPT、SNOPT、HPIPM 和 Riccati solver。
- 包含自动微分、代码生成和机器人建模工具。
- README 有 2021 年维护稀疏提示。

## 我的判断

它是研究最优控制工程抽象的好材料，但采用前必须评估维护、依赖和现代替代方案。和 OCS2、acados、Crocoddyl 对照价值高。

## 可复用内容

- C++ 最优控制库架构。
- 多 solver interface 设计。
- 自动微分与机器人建模集成思路。

## 疑问与冲突

- 维护状态是主要风险。
- 新项目可优先评估 OCS2、acados、Crocoddyl 等更活跃生态。

## 原料

- `raw/2026-06-24-control-toolbox-repository-snapshot.md`

