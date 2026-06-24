---
id: "20260624-do-mpc-python-mpc-toolbox"
title: "do-mpc：Python 非线性与鲁棒 MPC 工具箱"
type: "note"
source: "raw/2026-06-24-do-mpc-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-do-mpc.md
  - notes/2026-06-24-casadi-symbolic-optimization-framework.md
  - notes/2026-06-24-ipopt-large-scale-nonlinear-optimizer.md
  - notes/2026-06-24-acados-real-time-nmpc-solver.md
---

# do-mpc：Python 非线性与鲁棒 MPC 工具箱

## 一句话结论

do-mpc 是 Python 层的 MPC/MHE 建模、仿真和研究工具箱，适合快速搭建 nonlinear MPC、robust multi-stage MPC 和 MHE；工程落地时要再评估求解器、实时性和部署路径。

## 原文要点

- README 定位为 robust MPC 和 MHE 的 open-source toolbox。
- 支持非线性系统、不确定性、时间离散。
- 功能包含 nonlinear/economic MPC、DAE、orthogonal collocation、robust multi-stage MPC、MHE。
- Python 3.x 平台，文档为 `www.do-mpc.com`。

## 我的判断

do-mpc 适合作为 MPC 学习和原型层。它比 acados 更容易上手，比纯 CasADi 更成体系，但默认不等价于嵌入式实时控制内核。

## 可复用内容

- MPC/MHE 问题结构学习。
- 不确定性与 multi-stage MPC 原型。
- 与 CasADi/Ipopt 后端组合。

## 疑问与冲突

- 实车或机器人实时闭环需要进一步做求解时间、失败处理和接口封装。
- 复杂模型下求解稳定性依赖问题缩放和初值。

## 原料

- `raw/2026-06-24-do-mpc-repository-snapshot.md`

