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

EGO-Planner 是面向四旋翼的 ROS 1、ESDF-free 梯度局部规划器，核心价值是用局部占据栅格、A* 初始化和 B-spline 优化实现快速重规划；它适合算法学习和源码对照，不应作为 2026 年新项目的默认工程基线，官方 README 已明确推荐 EGO-Swarm。

## 原文要点

- README 称 EGO-Swarm 是 EGO-Planner 的 evolution，更 robust and safe。
- ROS2 支持指向 ego-planner-swarm 的 `ros2_version` 分支。
- EGO-Planner 不需要构建 ESDF。
- README 声称总规划时间约 1 ms。
- 框架基于 Fast-Planner。
- 2026-07-13 核对时，远端 `master` 仍为 `bfda512`，最近提交日期为 2025-03-08。
- 工程使用 ROS 1 catkin，README 列出的测试环境为 Ubuntu 16.04、18.04、20.04，构建命令为 `catkin_make`。
- 源码包分为 `plan_env`、`path_searching`、`bspline_opt`、`plan_manage`、`traj_utils`，并内置四旋翼仿真相关包。
- `plan_env` 接收深度图或点云并维护局部占据栅格；`path_searching` 提供 A*；`bspline_opt` 负责均匀 B-spline 与梯度优化；`plan_manage` 用 FSM 管理目标、重规划、碰撞检查和急停。
- 优化器引用轻量级 `LBFGS-Lite`；仿真侧依赖 Armadillo，`local_sensing` 可选 CUDA 渲染模拟深度。
- 仓库根许可证为 GPLv3，但部分内嵌 ROS 包的 `package.xml` 仍写有 `TODO` 或不同许可证，二次分发需逐文件核对。

## 我的判断

它是 Fast-Planner 生态里更轻量的局部重规划代表，最值得复用的是规划链路和模块边界，而不是整仓直接迁移。README 的约 1 ms 是作者项目描述，不等于不同平台、地图分辨率和约束规模下的通用实时性保证。

对自动驾驶地面车而言，它没有道路拓扑、交通规则、车辆非完整约束和行为决策层，不能直接替代 Nav2、Apollo 或 Autoware 的规划器；可借鉴的是局部地图更新、轨迹碰撞检测、重规划 FSM 和优化式轨迹生成。

## 可复用内容

- ESDF-free 局部规划思路。
- 「局部占据栅格 → A* 初始化 → B-spline 优化 → FSM 执行与碰撞检查」工程结构。
- Fast-Planner 到 EGO-Planner 的演进关系。
- 深度图与点云两种局部地图输入，以及规划失败后的急停处理入口。

## 疑问与冲突

- 最新推荐已转向 EGO-Swarm。
- 本仓库是 ROS 1；ROS 2 支持指向 EGO-Swarm 的 `ros2_version` 分支，topic 和节点接口不能直接照搬。
- 依赖环境偏旧，尤其是修改版 RealSense 驱动绑定 librealsense2 2.30.0 和 D435/D435i 时代配置。
- 未在当前环境执行 Ubuntu/ROS 兼容性构建或仿真，工程可运行性仍待目标平台验证。

## 原料

- `raw/2026-06-24-ego-planner-repository-snapshot.md`
