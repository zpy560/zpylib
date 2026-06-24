---
id: "20260624-motionplanning-autonomous-driving-planning-control-demos"
title: "MotionPlanning：自动驾驶规划与跟踪控制 Python 示例"
type: "note"
source: "raw/2026-06-24-motionplanning-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-motionplanning.md
  - notes/2026-06-24-pythonrobotics-robotics-algorithm-textbook.md
  - notes/2026-06-15-hybrid-a-star-ros1-vehicle-path-planner.md
---

# MotionPlanning：自动驾驶规划与跟踪控制 Python 示例

## 一句话结论

MotionPlanning 是更贴近自动驾驶车辆模型的 Python 示例库，重点覆盖 Hybrid A*、Frenet、H-OBCA 雏形以及 Pure Pursuit、Stanley、LQR、MPC 等跟踪控制；适合学习规划控制组合，不适合直接工程复用。

## 原文要点

- README 明确面向 autonomous vehicles 的 common motion planners。
- 规划器包括 Hybrid A*、Frenet Optimal Trajectory、H-OBCA。
- 控制器包括 Pure Pursuit、Rear-Wheel Feedback、Stanley、LQR、Linear MPC。
- 依赖 SciPy、cvxpy、Reeds-Shepp、pycubicspline。

## 我的判断

它比 PythonRobotics 更集中在自动驾驶规划控制链路，适合做算法组合实验：全局/局部路径生成后接跟踪控制器。但 README 已标注 H-OBCA incomplete，工程判断不能把它当完整优化避障实现。

## 可复用内容

- Hybrid A* 与 Reeds-Shepp 的车辆可行路径参考。
- Frenet 局部轨迹生成参考。
- 同一路径下多种横纵向控制器的行为对比。

## 疑问与冲突

- 缺少系统级测试、实时约束和安全后处理。
- H-OBCA 未完成，不能用于证明优化避障可用性。

## 原料

- `raw/2026-06-24-motionplanning-repository-snapshot.md`

