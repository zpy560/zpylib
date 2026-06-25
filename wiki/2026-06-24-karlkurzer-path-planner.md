---
id: "20260624-210012-karlkurzer-path-planner-wiki"
title: "karlkurzer/path_planner"
type: "entity"
source: "notes/2026-06-24-karlkurzer-path-planner-hybrid-a-star.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-karlkurzer-path-planner-hybrid-a-star.md
---

# karlkurzer/path_planner

## 定位

这是 KTH Research Concept Vehicle 的 ROS/C++ Hybrid A* 路径规划实现，面向非完整车辆在无结构环境中的实时路径搜索。

## 核心看点

- 3D 状态格：平面位置加航向。
- 启发函数：无障碍非完整启发和有障碍 holonomic 启发结合。
- 解析扩展：Dubins shot。
- 调试方式：ROS topic 与 RViz 交互。

## 使用边界

它适合学习 Hybrid A* 工程结构，不负责完整自动驾驶规划链。实际车端还需要行为决策、动态障碍处理、轨迹平滑、速度规划、控制跟踪和安全仲裁。

## 入库来源

- 单源笔记：../notes/2026-06-24-karlkurzer-path-planner-hybrid-a-star.md
- 仓库：https://github.com/karlkurzer/path_planner

