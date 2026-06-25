---
id: "20260624-212217-robotics-toolbox-python-note"
title: "Robotics Toolbox for Python：Python 机器人学工具箱"
type: "note"
source: "raw/2026-06-24-robotics-toolbox-python-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-robotics-toolbox-python.md
---

# Robotics Toolbox for Python：Python 机器人学工具箱

## 结论

Robotics Toolbox for Python 值得加入控制/规划知识库。适合机械臂建模、运动学、动力学、轨迹和机器人教学/原型。

## 事实摘录

- 远端仓库：`petercorke/robotics-toolbox-python`
- 当前核对 HEAD：`a9ed8d45e92aa221f85955406825e6a272151ece`
- README 定位为 Robotics Toolbox for MATLAB 的 Python implementation，提供 PyPI/conda 包、文档和 ICRA paper。

## 对规划控制的意义

- 可作为 Python 机器人学工具箱 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
