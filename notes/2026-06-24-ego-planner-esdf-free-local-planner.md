---
id: "20260624-ego-planner-esdf-free-local-planner"
title: "EGO-Planner：ESDF-free 四旋翼局部规划器"
type: "note"
source: "raw/2026-06-24-ego-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-ego-planner.md
  - notes/2026-06-24-fast-planner-quadrotor-fast-flight-planning.md
---

# EGO-Planner：ESDF-free 四旋翼局部规划器

## 一句话结论

EGO-Planner 是面向四旋翼的 ESDF-free gradient-based local planner，主打低计算开销和快速局部重规划；但 README 已提示 EGO-Swarm 是更新演进版本，使用时应优先评估 EGO-Swarm。

## 原文要点

- README 称 EGO-Swarm 是 EGO-Planner 的 evolution，更 robust and safe。
- ROS2 支持指向 ego-planner-swarm 的 `ros2_version` 分支。
- EGO-Planner 不需要构建 ESDF。
- README 声称总规划时间约 1 ms。
- 框架基于 Fast-Planner。

## 我的判断

它是 Fast-Planner 生态里“更轻、更快”的局部规划代表，适合学习 ESDF-free 梯度规划思路。工程使用不能忽略 README 对 EGO-Swarm 的推荐。

## 可复用内容

- ESDF-free 局部规划思路。
- 四旋翼局部重规划工程结构。
- Fast-Planner 到 EGO-Planner 的演进关系。

## 疑问与冲突

- 最新推荐已转向 EGO-Swarm。
- ROS1/ROS2 分支和 topic 变化需要按目标版本确认。

## 原料

- `raw/2026-06-24-ego-planner-repository-snapshot.md`

