---
id: "20260624-210027-acado-note"
title: "ACADO Toolkit：自动控制与动态优化工具箱"
type: "note"
source: "raw/2026-06-24-acado-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-acado.md
---

# ACADO Toolkit：自动控制与动态优化工具箱

## 结论

ACADO 是自动控制和动态优化工具箱，适合放入 MPC/OCP 知识链。它和已入库的 acados 名字接近但不是同一定位：ACADO 更像经典工具箱和算法集合，acados 更偏实时 OCP/NMPC 求解器。

## 事实摘录

- 远端仓库：`acado/acado`
- 当前核对 HEAD：`b8e586639fc714bf3263152637da3b0efce23a32`
- README 定位：Toolkit for Automatic Control and Dynamic Optimization。
- 覆盖 direct optimal control、model predictive control、state and parameter estimation、robust optimization。
- 实现为 self-contained C++，并带 MATLAB interface。

## 对规划控制的意义

- 适合理解 MPC/OCP 工具箱抽象：模型、代价、约束、求解器后端和代码接口。
- 对自动驾驶/机器人轨迹优化，ACADO 可作为历史和概念参考。
- 与 CasADi、acados、do-mpc、OCS2 对照，可以看出建模工具、求解器和实时部署之间的分工。

## 使用建议

新项目不应默认选 ACADO；先确认维护状态、目标平台、实时性要求和接口生态。学习时可重点关注 OCP 表达和 MPC 示例，不必从完整源码开始。

