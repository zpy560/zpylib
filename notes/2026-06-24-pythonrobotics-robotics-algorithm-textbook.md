---
id: "20260624-pythonrobotics-robotics-algorithm-textbook"
title: "PythonRobotics：机器人规划控制算法教材式代码库"
type: "note"
source: "raw/2026-06-24-pythonrobotics-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-pythonrobotics.md
  - notes/2026-06-24-motionplanning-autonomous-driving-planning-control-demos.md
  - notes/2026-06-15-cpprobotics-cpp-robotics-algorithm-demos.md
---

# PythonRobotics：机器人规划控制算法教材式代码库

## 一句话结论

PythonRobotics 是规划控制算法的高质量学习索引，覆盖从 A*/RRT/Frenet 到 Stanley/LQR/MPC 的大量最小实现；适合用来理解算法流程和快速验证想法，不适合直接作为生产算法库。

## 原文要点

- README 明确定位为 robotics algorithms 的 Python code collection 和 textbook。
- 路径规划覆盖图搜索、采样规划、状态格、Frenet、Reeds-Shepp、覆盖路径等。
- 路径跟踪覆盖 Stanley、rear-wheel feedback、LQR、MPC、C-GMRES 等。
- 还包含定位、建图、SLAM、机械臂、无人机和双足示例。

## 我的判断

推荐优先级很高，因为它把规划控制经典算法按可运行示例组织起来，适合做“算法地图”。工程使用时应把它当作伪代码和实验基线，再迁移到 C++、ROS 或目标系统。

## 可复用内容

- 用来横向比较算法类别。
- 用作新算法实现前的流程参考。
- 用作 CppRobotics、MotionPlanning 等 C++/车辆示例的上游对照。

## 疑问与冲突

- 示例级代码不等于实时、鲁棒、可测试的工程模块。
- 车辆动力学、约束处理和安全验证需要另行补齐。

## 原料

- `raw/2026-06-24-pythonrobotics-repository-snapshot.md`

