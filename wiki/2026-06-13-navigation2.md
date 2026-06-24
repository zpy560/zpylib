---
id: "20260613-navigation2"
title: "Navigation2"
type: "entity"
source: "https://github.com/ros-navigation/navigation2"
created_at: "2026-06-13"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
  - wiki/2026-06-24-navigation2-release.md
  - wiki/2026-06-24-navigation2-tutorials.md
  - wiki/2026-06-24-ros2-control.md
  - wiki/2026-06-14-apollo.md
  - wiki/2026-06-14-autoware.md
  - wiki/2026-06-14-ros-motion-planning.md
  - wiki/2026-06-15-rtabmap.md
---

# Navigation2

## 基本信息

- 简称：Nav2
- 类型：ROS 2 移动机器人导航框架
- 官方仓库：https://github.com/ros-navigation/navigation2
- 官方文档：https://docs.nav2.org/
- 发布元数据：https://github.com/ros2-gbp/navigation2-release
- 主要语言：C++、Python、XML、YAML
- 主要机制：ROS 2 Action、Lifecycle、Behavior Tree、pluginlib、Costmap
- 快照提交：`374cd2556640586251b1e49a346f6c8d0cb76224`
- 快照日期：2026-06-13

## 当前判断

Nav2 是研究“模块化导航系统如何工程化”的高价值参考项目。它最值得学习的是任务编排、能力服务器、算法插件、生命周期和末端安全链之间的边界，而不是把它直接移植为乘用车自动驾驶栈。

## 架构总览

```text
NavigateToPose / NavigateThroughPoses
                ↓
          BT Navigator
                ↓
   Planner / Smoother / Controller
                ↓
      Velocity Smoother
                ↓
       Collision Monitor
                ↓
              底盘
```

配套模块：

- AMCL、TF、Odometry：状态估计与坐标关系。
- Global/Local Costmap：环境表达。
- Behavior Server：旋转、后退、等待等恢复行为。
- Route Server：拓扑路线图导航。
- Waypoint Follower：多点任务执行。
- Docking/Following Server：充电对接和动态目标跟随。
- Lifecycle Manager：统一管理系统状态和节点健康。

## 核心扩展点

- Global Planner
- Controller
- Smoother
- Behavior
- Behavior Tree Navigator
- Goal Checker
- Progress Checker
- Path Handler
- Waypoint Task Executor
- Costmap Layer 与 Filter

## 对规划控制的启发

1. 行为策略与运动算法分层。
2. 稳定服务器接口承载可替换算法。
3. 局部故障使用局部恢复，失败再逐级升级。
4. 控制命令经过整形和独立安全监控后才执行。
5. 节点生命周期和健康状态应成为系统协议。
6. 拓扑路线和自由空间路径适合使用不同规划层。

## 适用边界

适合：

- AMR、AGV、服务机器人和工业移动机器人
- ROS 2 导航系统学习与原型开发
- 规划器、控制器、代价地图和行为树插件开发
- 导航架构与恢复机制研究

不等价于：

- 开放道路乘用车行为规划系统
- 多主体预测与交互决策系统
- 量产级功能安全规划控制平台

## 版本与发布

`ros2-gbp/navigation2-release` 记录 Nav2 进入 ROS 发行版的 Bloom 发布元数据。它不是源码仓库，但适合确认 Humble、Jazzy、Kilted 等 distro 的发布版本、包清单和 upstream tag。调试 apt 安装的 Nav2 行为时，不应直接用 `main` 分支判断，应先通过 release 仓库锁定对应版本。

## 关联笔记

- `notes/2026-06-13-navigation2-ros2-navigation-framework.md`
- `wiki/2026-06-24-navigation2-release.md`
- `wiki/2026-06-24-navigation2-tutorials.md`
- `wiki/2026-06-24-ros2-control.md`
- `wiki/2026-06-14-apollo.md`
- `wiki/2026-06-14-autoware.md`
- `wiki/2026-06-14-ros-motion-planning.md`
- `wiki/2026-06-15-rtabmap.md`

## 更新记录

- 2026-06-13：基于官方 `main` 分支提交 `374cd25` 首次建档。
- 2026-06-14：增加 Apollo 架构对比关联。
- 2026-06-14：增加 Autoware 架构对比关联。
- 2026-06-14：增加 ROS Motion Planning 算法工作台关联。
- 2026-06-15：增加 RTAB-Map 建图与定位上游关联。
- 2026-06-24：增加 Navigation2 Tutorials 插件与集成教程代码关联。
- 2026-06-24：增加 ros2_control 执行层控制框架关联。
- 2026-06-24：增加 navigation2-release 发布元数据仓库关联。
