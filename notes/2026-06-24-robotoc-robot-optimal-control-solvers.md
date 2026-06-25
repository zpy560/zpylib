---
id: "20260624-211023-robotoc-note"
title: "robotoc：机器人最优控制求解器"
type: "note"
source: "raw/2026-06-24-robotoc-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-robotoc.md
---

# robotoc：机器人最优控制求解器

## 结论

`robotoc` 是面向机器人系统的最优控制求解器，特别值得用于研究接触切换、lifted contact dynamics、inverse dynamics 和 MPC。它比通用优化库更贴近腿式/接触机器人控制问题。

## 事实摘录

- 远端仓库：`mayataka/robotoc`
- 当前核对 HEAD：`d30d404942835f3804161cda43e0845f653cac09`
- README 定位：efficient ROBOT Optimal Control solvers。
- 特性包括 direct multiple shooting、lifted contact dynamics、inverse dynamics、switching time optimization、pure-state equality constraints、primal-dual interior point method。
- 使用 Pinocchio 计算刚体动力学和敏感度。

## 对规划控制的意义

- 对腿式机器人：接触序列和切换时间优化是核心难点。
- 对 MPC：它提供了结构化机器人 OCP 求解思路，而不是只给通用 NLP 接口。
- 对知识链：可与 OCS2、Crocoddyl、TSID、Pinocchio 形成对照。

## 使用建议

优先看示例和 MPC demos，再回到 solver 内部。新项目选型时要比较维护状态、Python/C++ 接口、实时性能和机器人模型复杂度。

