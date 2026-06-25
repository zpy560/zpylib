---
id: "20260624-210035-nlopt-note"
title: "NLopt：非线性局部与全局优化算法库"
type: "note"
source: "raw/2026-06-24-nlopt-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-nlopt.md
---

# NLopt：非线性局部与全局优化算法库

## 结论

NLopt 是通用非线性优化算法库，适合作为规划控制问题中的优化后端候选。它不是机器人专用 OCP/MPC 框架，所以价值在于算法集合和统一接口，而不是完整建模与实时控制链。

## 事实摘录

- 远端仓库：`stevengj/nlopt`
- 当前核对 HEAD：`6e6593f131ba3a38bc9edbed0a357bc01526e54b`
- README 定位：nonlinear local and global optimization library。
- 支持有梯度和无梯度函数。
- README 声称它统一封装多个 free/open-source nonlinear optimization libraries。
- 语言接口覆盖 C/C++/Fortran/Python/Matlab/Rust/Julia/Java 等。

## 对规划控制的意义

- 可用于参数优化、轨迹优化子问题、标定和无梯度调参。
- 与 Ipopt、OSQP、CasADi、acados 的差异在于：NLopt 更通用，缺少机器人 OCP 的专用建模语义。
- 对实时 MPC 场景，必须单独验证收敛时间、约束表达能力和 warm start 支持。

## 使用建议

当问题是一般非线性优化或 derivative-free tuning 时考虑 NLopt；当问题是结构化 OCP/NMPC 时，优先比较 acados、CasADi、OCS2、do-mpc、Ipopt。

