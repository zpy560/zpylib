---
id: "20260624-acados-real-time-nmpc-solver"
title: "acados：实时非线性 MPC 与 OCP 求解器"
type: "note"
source: "raw/2026-06-24-acados-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-acados.md
  - notes/2026-06-24-casadi-symbolic-optimization-framework.md
  - notes/2026-06-24-osqp-operator-splitting-qp-solver.md
  - notes/2026-06-24-ocs2-real-time-optimal-control-toolbox.md
---

# acados：实时非线性 MPC 与 OCP 求解器

## 一句话结论

acados 是面向实时和嵌入式的非线性最优控制求解器工具包，适合 NMPC、MHE 和 OCP 结构问题；它解决“优化问题怎么高频求”，不解决“场景怎么建模、行为怎么决策”。

## 原文要点

- README 定位为 fast and embedded solvers for nonlinear optimal control。
- 核心问题是 OCP 结构的 NLP，常用于 MPC 和 MHE。
- 支持 DAE、多重 shooting、SQP-type solver、积分器、灵敏度等。
- C 实现，提供 Python、MATLAB、Octave 接口。
- 接口中可使用 CasADi 表达非线性函数。

## 我的判断

acados 是规划控制中“实时优化内核”的重要候选。用于车辆或机器人时，价值在高频 NMPC，而不是替代完整局部规划器或安全监控链。

## 可复用内容

- NMPC/MHE 工程求解器选型。
- OCP 问题建模和代码生成接口参考。
- 与 CasADi、HPIPM 等工具链组合使用。

## 疑问与冲突

- 学习门槛和问题建模成本高。
- 是否满足目标实时性取决于模型、约束、离散化、warm start 和硬件平台。

## 原料

- `raw/2026-06-24-acados-repository-snapshot.md`

