---
id: "20260624-212122-qpsolvers-raw"
title: "qpsolvers repository snapshot"
type: "note"
source: "https://github.com/qpsolvers/qpsolvers"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-qpsolvers-repository-analysis.md
---

# qpsolvers repository snapshot

- Repository: `qpsolvers/qpsolvers`
- URL: https://github.com/qpsolvers/qpsolvers
- Checked HEAD: `679458f48aadf15541ca1658f30d9fee75d3ff52`

## README / source facts

- README 提供 solve_qp 函数求解凸二次规划，返回后端 QP solver 的 primal solution 或失败时 None。
- 本次入库只基于远端 HEAD、README 或仓库元信息做单源快照；未做本地编译。

## Local interpretation

适合快速切换 QP 后端、验证控制/规划优化问题。
