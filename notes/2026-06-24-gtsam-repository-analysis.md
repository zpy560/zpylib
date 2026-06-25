---
id: "20260624-212202-gtsam-note"
title: "GTSAM：因子图平滑与建图库"
type: "note"
source: "raw/2026-06-24-gtsam-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-gtsam.md
---

# GTSAM：因子图平滑与建图库

## 结论

GTSAM 值得加入控制/规划知识库。适合 SLAM、定位、传感器融合和轨迹估计中的 factor graph 建模。

## 事实摘录

- 远端仓库：`borglab/gtsam`
- 当前核对 HEAD：`f633c9183f488d3a9471e57ac032bde11ab68857`
- README 定位为 Georgia Tech Smoothing and Mapping library，使用 Factor Graphs 和 Bayes Networks 作为计算范式。

## 对规划控制的意义

- 可作为 因子图平滑与建图库 的源码或架构参考。
- 适合与知识库中已有的 Nav2、MoveIt、ros2_control、Pinocchio、OCS2、Crocoddyl、OSQP、Ipopt 等条目横向对照。
- 使用前应确认目标 ROS/系统版本、许可证、维护状态和实时性边界。

## 使用建议

先从 README、examples/tests、核心 include/src 入口和文档页切入。对优化/控制库重点看问题表达、约束形式和求解器接口；对规划/地图库重点看数据结构、输入输出和与 planner/controller 的连接点。
