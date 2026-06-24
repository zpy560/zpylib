---
id: "20260624-osqp-operator-splitting-qp-solver"
title: "OSQP：Operator Splitting 二次规划求解器"
type: "note"
source: "raw/2026-06-24-osqp-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-osqp.md
  - notes/2026-06-24-acados-real-time-nmpc-solver.md
  - notes/2026-06-24-ipopt-large-scale-nonlinear-optimizer.md
---

# OSQP：Operator Splitting 二次规划求解器

## 一句话结论

OSQP 是规划控制里常用的凸 QP 求解器，适合路径平滑、线性 MPC、约束最小二乘等问题；它只负责求解标准 QP，不负责把车辆、障碍物或行为策略建模成 QP。

## 原文要点

- README 定位为 Operator Splitting Quadratic Program solver。
- 标准形式是二次目标加线性不等式上下界约束。
- 文档入口为 `osqp.org`。
- README 提供 benchmark、issue 和 citation 入口。

## 我的判断

OSQP 应放在“优化工具链”层。它比 Ipopt/acados 更专注于凸 QP，适合工程中需要稳定、快速、可嵌入的 QP 子问题。

## 可复用内容

- 路径平滑 QP。
- 线性 MPC QP。
- 优化问题标准化表达。

## 疑问与冲突

- 非凸、强非线性、整数决策等问题不能直接交给 OSQP。
- 求解结果质量取决于问题缩放、约束建模和 warm start。

## 原料

- `raw/2026-06-24-osqp-repository-snapshot.md`

