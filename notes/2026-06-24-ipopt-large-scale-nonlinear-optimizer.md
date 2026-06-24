---
id: "20260624-ipopt-large-scale-nonlinear-optimizer"
title: "Ipopt：大规模非线性优化求解器"
type: "note"
source: "raw/2026-06-24-ipopt-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-ipopt.md
  - notes/2026-06-24-casadi-symbolic-optimization-framework.md
  - notes/2026-06-24-do-mpc-python-mpc-toolbox.md
  - notes/2026-06-24-osqp-operator-splitting-qp-solver.md
---

# Ipopt：大规模非线性优化求解器

## 一句话结论

Ipopt 是大规模光滑非线性优化的经典求解器，适合轨迹优化、非线性 MPC 原型和 CasADi/do-mpc 后端；它求局部解，不负责全局搜索或系统安全兜底。

## 原文要点

- README 定位为 large-scale nonlinear optimization package。
- 支持非线性目标和非线性约束上下界。
- 问题可以非凸，但函数应二阶连续可微。
- C++ 实现，属于 COIN-OR，EPL 许可证。
- 依赖稀疏线性求解器和 BLAS/LAPACK。

## 我的判断

Ipopt 是优化建模生态的基础件。用它做规划控制时，关键不是“能不能求”，而是问题是否光滑、初值是否合理、约束是否尺度良好、局部解是否满足安全需求。

## 可复用内容

- 轨迹优化 NLP 后端。
- CasADi/do-mpc 原型求解器。
- 非线性约束问题的工程边界参考。

## 疑问与冲突

- 非凸问题只保证局部解。
- 实时控制场景通常需要更强的 warm start、结构利用或专用求解器。

## 原料

- `raw/2026-06-24-ipopt-repository-snapshot.md`

