---
id: "20260624-fast-planner-quadrotor-fast-flight-planning"
title: "Fast-Planner：复杂未知环境四旋翼快速飞行规划"
type: "note"
source: "raw/2026-06-24-fast-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-24-fast-planner.md
  - notes/2026-06-24-ego-planner-esdf-free-local-planner.md
  - notes/2026-06-24-mav-trajectory-generation-polynomial-trajectories.md
---

# Fast-Planner：复杂未知环境四旋翼快速飞行规划

## 一句话结论

Fast-Planner 是四旋翼在复杂未知环境中快速飞行的规划框架，适合研究无人机局部重规划、轨迹优化和探索；它不是地面车规划控制库。

## 原文要点

- README 明确目标是 quadrotor fast flight in complex unknown environments。
- 包含 carefully designed planning algorithms。
- 支撑 ego-planner、FUEL、RACER 等开源无人机项目。
- 测试环境为 Ubuntu 18.04/20.04 和 ROS Melodic/Noetic。
- 依赖 `nlopt v2.7.1`。

## 我的判断

它是无人机规划方向的关键工程参考，尤其适合和 EGO-Planner 对照：Fast-Planner 更像基础框架和算法集合，EGO-Planner 更突出 ESDF-free 的快速局部规划。

## 可复用内容

- 四旋翼未知环境快速重规划。
- B-spline/拓扑路径/轨迹优化思路。
- ROS1 无人机规划框架组织。

## 疑问与冲突

- 依赖和 ROS 版本偏旧。
- 需要具体读取算法目录才能区分各论文实现边界。

## 原料

- `raw/2026-06-24-fast-planner-repository-snapshot.md`

