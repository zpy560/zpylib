---
id: "20260624-212106-ifopt-raw"
title: "ifopt repository snapshot"
type: "note"
source: "https://github.com/ethz-adrl/ifopt"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-ifopt-repository-analysis.md
---

# ifopt repository snapshot

- Repository: `ethz-adrl/ifopt`
- URL: https://github.com/ethz-adrl/ifopt
- Checked HEAD: `4d6267bfefbaaa97e079c9aa163ebd477fce064d`

## README / source facts

- README 定位为 modern lightweight Eigen-based C++ interface to nonlinear programming solvers such as Ipopt and Snopt。
- 本次入库只基于远端 HEAD、README 或仓库元信息做单源快照；未做本地编译。

## Local interpretation

适合把机器人优化问题统一表达后交给 Ipopt/Snopt 等 NLP solver。
