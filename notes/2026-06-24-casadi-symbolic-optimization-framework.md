---
id: "20260624-casadi-symbolic-optimization-framework"
title: "CasADi：符号建模与优化工具链"
type: "note"
source: "raw/2026-06-24-casadi-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-casadi.md
  - notes/2026-06-24-ipopt-large-scale-nonlinear-optimizer.md
  - notes/2026-06-24-do-mpc-python-mpc-toolbox.md
  - notes/2026-06-24-acados-real-time-nmpc-solver.md
---

# CasADi：符号建模与优化工具链

## 一句话结论

CasADi 是规划控制优化链路中的符号建模和自动微分工具，适合构建 NLP/OCP/MPC 问题并连接 Ipopt、acados、do-mpc 等求解生态；它不是直接控制器。

## 原文要点

- README 指向 CasADi homepage 与 install instructions。
- acados README 明确提到接口可通过 CasADi symbolic software framework 指定非线性表达。
- do-mpc README 提醒使用 do-mpc 时也要引用 CasADi、Ipopt 等依赖软件。

## 我的判断

CasADi 是优化问题从数学表达走向可求解程序的关键桥梁。对于自动驾驶和机器人 MPC，CasADi 的价值在快速建模、自动微分和调用 NLP 后端。

## 可复用内容

- 轨迹优化和 MPC 原型建模。
- 自动微分与雅可比/海森矩阵生成。
- 连接 Ipopt、acados 等后端。

## 疑问与冲突

- CasADi 原型不等于实时控制实现。
- 代码生成、求解器选择和部署闭环仍需单独验证。

## 原料

- `raw/2026-06-24-casadi-repository-snapshot.md`

