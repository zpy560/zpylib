---
id: "20260624-211011-sbpl-note"
title: "SBPL：Search-Based Planning Library"
type: "note"
source: "raw/2026-06-24-sbpl-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-sbpl.md
---

# SBPL：Search-Based Planning Library

## 结论

SBPL 是搜索式规划和 lattice planning 的经典资料，适合保留。它的工程年代较早，但 ARA*、AD*、R*、xytheta lattice、motion primitives 等内容对理解自动驾驶/移动机器人搜索规划仍有价值。

## 事实摘录

- 远端仓库：`sbpl/sbpl`
- 当前核对 HEAD：`4d654845aa3b92aa1b4282a342e9011bac95aeb9`
- README 定位：standalone software library。
- 依赖：除 C/C++ 标准库外无其他依赖。
- 示例入口：`src/test/main.cpp`。
- 示例环境：2D、xytheta、robot arm 等 `.cfg`。
- 源码中包含 `araplanner`、`adplanner`、`rstarplanner`、`mhaplanner`、`ANAplanner` 等。

## 对规划控制的意义

- 对路径搜索：提供 anytime/incremental/heuristic search 的经典实现入口。
- 对车辆规划：motion primitive 和 xytheta lattice 是理解状态格规划的重要基础。
- 对 ROS 历史：很多 ROS1 导航和机械臂规划资料都曾引用 SBPL。

## 使用建议

把 SBPL 当算法参考和历史基线，不要直接当现代 ROS 2 planner。读源码时先从 environment abstraction、heuristic、planner base 和 motion primitive 文件开始。

