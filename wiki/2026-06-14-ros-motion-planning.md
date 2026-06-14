---
id: "20260614-ros-motion-planning"
title: "ROS Motion Planning"
type: "entity"
source: "raw/2026-06-14-ros-motion-planning-repository-snapshot.md"
created_at: "2026-06-14"
tags:
  - planning-control
  - autonomous-driving
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-14-ros-motion-planning-algorithm-workbench.md
  - wiki/2026-06-13-navigation2.md
---

# ROS Motion Planning

## 基本信息

- 类型：ROS1 移动机器人运动规划算法与仿真平台
- 官方仓库：https://github.com/ai-winter/ros_motion_planning
- 目标环境：Ubuntu 20.04、ROS Noetic
- 主要语言：C++、Python、YAML、XML
- 快照分支：`dev`
- 快照提交：`a6f21b0e7a5aa714bab204289f7a4835b2148fa4`
- 快照日期：2026-06-14
- 许可证：GPLv3

## 当前判断

该项目适合学习和比较经典全局规划、局部控制及曲线生成算法。它通过 ROS costmap、`move_base`、Gazebo 和 RViz 提供统一实验外壳，但不应被视为完整导航框架或自动驾驶平台。

## 算法范围

- 图搜索：A*、Dijkstra、JPS、D* 系列、Theta* 系列、Voronoi、Hybrid A*。
- 采样：RRT、RRT*、RRT-Connect、Informed RRT*。
- 进化：ACO、GA、PSO。
- 局部控制：PID、LQR、DWA、APF、RPP、MPC、ORCA。
- 曲线：Polynomial、Bezier、Spline、Dubins、Reeds-Shepp。

## 架构

```text
user_config.yaml
→ 动态生成 launch/world/RViz
→ move_base
→ Global Planner + Local Controller
→ costmap_2d
→ Gazebo / Robot
```

全局规划器共享 `PathPlanner` 基类和碰撞检测；全局与局部入口分别适配 `nav_core::BaseGlobalPlanner` 和 `BaseLocalPlanner`。

## 适用边界

适合：

- 经典运动规划算法学习
- ROS1 `move_base` 插件开发
- 统一地图下的算法可视化比较
- 多机器人和动态行人仿真实验

不等价于：

- ROS2 Navigation2 的生命周期与行为树系统
- 开放道路自动驾驶行为规划
- 具备完整安全、诊断和降级链的生产平台

## 关联笔记

- `notes/2026-06-14-ros-motion-planning-algorithm-workbench.md`
- `wiki/2026-06-13-navigation2.md`

## 更新记录

- 2026-06-14：基于 `dev` 分支提交 `a6f21b0` 首次建档。
