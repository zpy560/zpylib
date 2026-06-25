---
id: "20260624-240000-mobile-chassis-planning-control-github-resources-batch-2"
title: "移动底盘规划控制 GitHub 资源精选（二）"
type: "topic"
source: ""
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-24-turtlebot3-planning-control-git-resource.md
  - notes/2026-06-24-turtlebot3-simulations-planning-control-git-resource.md
  - notes/2026-06-24-turtlebot3-autorace-planning-control-git-resource.md
  - notes/2026-06-24-move-base-flex-planning-control-git-resource.md
  - notes/2026-06-24-sbpl-planning-control-git-resource.md
  - notes/2026-06-24-octomap-planning-control-git-resource.md
  - notes/2026-06-24-slam-toolbox-planning-control-git-resource.md
  - notes/2026-06-24-slam-gmapping-planning-control-git-resource.md
  - notes/2026-06-24-commonroad-io-planning-control-git-resource.md
  - notes/2026-06-24-commonroad-scenario-designer-planning-control-git-resource.md
  - notes/2026-06-24-commonroad-crime-planning-control-git-resource.md
  - notes/2026-06-24-global-racetrajectory-optimization-planning-control-git-resource.md
  - notes/2026-06-24-graph-based-local-trajectory-planner-planning-control-git-resource.md
  - notes/2026-06-24-mod-vehicle-dynamics-control-planning-control-git-resource.md
  - notes/2026-06-24-forzaeth-race-stack-planning-control-git-resource.md
  - notes/2026-06-24-f1tenth-gym-planning-control-git-resource.md
  - notes/2026-06-24-f1tenth-gym-ros-planning-control-git-resource.md
  - notes/2026-06-24-f1tenth-system-planning-control-git-resource.md
  - notes/2026-06-24-f1tenth-vesc-planning-control-git-resource.md
  - notes/2026-06-24-highway-env-planning-control-git-resource.md
  - notes/2026-06-24-acado-planning-control-git-resource.md
  - notes/2026-06-24-qpoases-planning-control-git-resource.md
  - notes/2026-06-24-ifopt-planning-control-git-resource.md
  - notes/2026-06-24-kindr-planning-control-git-resource.md
  - notes/2026-06-24-kindr-ros-planning-control-git-resource.md
  - notes/2026-06-24-autoware-launch-planning-control-git-resource.md
  - notes/2026-06-24-sample-vehicle-launch-planning-control-git-resource.md
  - notes/2026-06-24-sample-sensor-kit-launch-planning-control-git-resource.md
  - notes/2026-06-24-autoware-core-planning-control-git-resource.md
  - notes/2026-06-24-gazebo-ros-pkgs-planning-control-git-resource.md
  - notes/2026-06-24-gazebo-ros2-control-planning-control-git-resource.md
  - notes/2026-06-24-ackermann-msgs-planning-control-git-resource.md
  - notes/2026-06-24-duckietown-dt-core-planning-control-git-resource.md
  - notes/2026-06-24-rmf-ros2-planning-control-git-resource.md
  - notes/2026-06-24-clearpath-common-planning-control-git-resource.md
  - notes/2026-06-24-gtsam-planning-control-git-resource.md
  - notes/2026-06-24-cartographer-planning-control-git-resource.md
  - notes/2026-06-24-cartographer-ros-planning-control-git-resource.md
  - notes/2026-06-24-mrpt-planning-control-git-resource.md
  - notes/2026-06-24-rmf-traffic-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（二）

## 当前判断

本页是第二批 40 个当前知识库未记录过的 GitHub 资源。相比第一批，本批更偏移动机器人平台、ROS 导航/SLAM、CommonRoad/TUM/F1TENTH 自动驾驶规划控制、Autoware 装配配置、ROS 控制仿真、多机器人交通和定位建图基础设施。

## 取舍边界

- 本批继续排除已入库 Git URL，包括第一批新增的 CARLA、AirSim、ArduPilot、MAVROS、grid_map、Isaac Lab、Unitree、MuJoCo、EGO-Swarm 等。
- 不是所有仓库都是 planner/controller：移动底盘闭环还依赖地图、定位、仿真、消息接口、控制器管理、solver 和 fleet traffic 层。
- star/fork 是筛选信号，不是质量结论；后续真正使用前要看代码、许可证、维护状态和接口假设。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [ROBOTIS-GIT/turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3) | AMR 教学与导航底盘 | 2k / 1.2k | ROS packages for TurtleBot3，包含 bringup、description、navigation2、Cartographer、teleop 等包。 |
| 2 | [ROBOTIS-GIT/turtlebot3_simulations](https://github.com/ROBOTIS-GIT/turtlebot3_simulations) | AMR 仿真 | 1k+ / 900+ | TurtleBot3 simulation packages for Gazebo/RViz workflows. |
| 3 | [ROBOTIS-GIT/turtlebot3_autorace](https://github.com/ROBOTIS-GIT/turtlebot3_autorace) | 小车自动驾驶竞赛 | 300+ / 300+ | TurtleBot3 AutoRace 相关 ROS 包，覆盖车道、交通灯、路标、交叉路口等任务。 |
| 4 | [naturerobots/move_base_flex](https://github.com/naturerobots/move_base_flex) | ROS 导航框架 | 600+ / 300+ | Move Base Flex: A highly flexible navigation framework. |
| 5 | [sbpl/sbpl](https://github.com/sbpl/sbpl) | 搜索式规划库 | 700+ / 400+ | Search-Based Planning Library. |
| 6 | [octomap/octomap](https://github.com/octomap/octomap) | 三维占据地图 | 1.8k+ / 800+ | An efficient probabilistic 3D mapping framework based on octrees. |
| 7 | [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) | ROS2 SLAM/定位 | 2.5k / 691 | ROS2 支持的 2D SLAM、长期建图和定位工具箱。 |
| 8 | [ros-perception/slam_gmapping](https://github.com/ros-perception/slam_gmapping) | ROS1 SLAM | 700+ / 500+ | ROS wrapper for OpenSlam GMapping. |
| 9 | [CommonRoad/commonroad-io](https://github.com/CommonRoad/commonroad-io) | 自动驾驶规划 benchmark IO | 19 / 1 | 读写、可视化 CommonRoad 场景与 planning problems，并作为其他 CommonRoad 工具基础。 |
| 10 | [CommonRoad/commonroad-scenario-designer](https://github.com/CommonRoad/commonroad-scenario-designer) | 自动驾驶场景生成 | 120+ / 30+ | Toolbox for map conversion and scenario creation for autonomous vehicles. |
| 11 | [CommonRoad/commonroad-crime](https://github.com/CommonRoad/commonroad-crime) | 自动驾驶风险评估 | 60+ / 10+ | Toolbox to compute criticality measures for automated vehicles. |
| 12 | [TUMFTM/global_racetrajectory_optimization](https://github.com/TUMFTM/global_racetrajectory_optimization) | 自动赛车全局轨迹优化 | 600+ / 200+ | Multiple approaches for generating global race trajectories. |
| 13 | [TUMFTM/GraphBasedLocalTrajectoryPlanner](https://github.com/TUMFTM/GraphBasedLocalTrajectoryPlanner) | 自动赛车局部轨迹规划 | 265 / 59 | Multilayer graph-based local trajectory planner for autonomous race vehicles. |
| 14 | [TUMFTM/mod_vehicle_dynamics_control](https://github.com/TUMFTM/mod_vehicle_dynamics_control) | 车辆动力学控制 | 200+ / 70+ | TUM Roborace path tracking, velocity control, curvature control and state estimation. |
| 15 | [ForzaETH/race_stack](https://github.com/ForzaETH/race_stack) | 自动赛车软件栈 | 300+ / 80+ | The autonomous racing stack for the ForzaETH team. |
| 16 | [f1tenth/f1tenth_gym](https://github.com/f1tenth/f1tenth_gym) | F1TENTH 仿真环境 | 243 / 181 | F1TENTH Gym environment for continuous control and reinforcement learning. |
| 17 | [f1tenth/f1tenth_gym_ros](https://github.com/f1tenth/f1tenth_gym_ros) | F1TENTH ROS 桥 | 160+ / 110+ | Containerized ROS communication bridge for F1TENTH gym environment. |
| 18 | [f1tenth/f1tenth_system](https://github.com/f1tenth/f1tenth_system) | F1TENTH 实车系统 | 300+ / 250+ | Drivers and system-level code for F1TENTH vehicles. |
| 19 | [f1tenth/vesc](https://github.com/f1tenth/vesc) | 小车电调接口 | 180+ / 160+ | Repository for the VESC Controller for ROS1 and ROS2. |
| 20 | [Farama-Foundation/HighwayEnv](https://github.com/Farama-Foundation/HighwayEnv) | 自动驾驶决策环境 | 3k+ / 900+ | Minimalist environment for decision-making in autonomous driving. |
| 21 | [acado/acado](https://github.com/acado/acado) | 最优控制/MPC | 1k+ / 500+ | Software environment and algorithms for automatic control and dynamic optimization. |
| 22 | [coin-or/qpOASES](https://github.com/coin-or/qpOASES) | QP/MPC 求解器 | 540 / 151 | Online active set QP solver particularly suited for MPC applications. |
| 23 | [ethz-adrl/ifopt](https://github.com/ethz-adrl/ifopt) | 非线性优化接口 | 700+ / 150+ | Eigen-based lightweight C++ interface to nonlinear programming solvers. |
| 24 | [ANYbotics/kindr](https://github.com/ANYbotics/kindr) | 机器人运动学动力学 | 500+ / 170+ | Kinematics and Dynamics for Robotics. |
| 25 | [ANYbotics/kindr_ros](https://github.com/ANYbotics/kindr_ros) | 机器人运动学 ROS 接口 | 150+ / 80+ | ROS integration utilities for kindr. |
| 26 | [autowarefoundation/autoware_launch](https://github.com/autowarefoundation/autoware_launch) | Autoware 启动配置 | 56 / 461 | Autoware launch configuration repository containing node configurations and parameters. |
| 27 | [autowarefoundation/sample_vehicle_launch](https://github.com/autowarefoundation/sample_vehicle_launch) | Autoware 车辆接口样例 | 30+ / 200+ | Autoware sample vehicle launch configuration. |
| 28 | [autowarefoundation/sample_sensor_kit_launch](https://github.com/autowarefoundation/sample_sensor_kit_launch) | Autoware 传感器配置样例 | 30+ / 200+ | Autoware sample sensor kit launch configuration. |
| 29 | [autowarefoundation/autoware_core](https://github.com/autowarefoundation/autoware_core) | Autoware 核心包 | 200+ / 300+ | Autoware core packages separated from universe. |
| 30 | [ros-simulation/gazebo_ros_pkgs](https://github.com/ros-simulation/gazebo_ros_pkgs) | ROS Gazebo 仿真接口 | 700+ / 700+ | Wrappers, tools and APIs for using ROS with Gazebo. |
| 31 | [ros-controls/gazebo_ros2_control](https://github.com/ros-controls/gazebo_ros2_control) | ros2_control 仿真接口 | 255 / 134 | ros2_control controller architecture integration with Gazebo Classic. |
| 32 | [ros-drivers/ackermann_msgs](https://github.com/ros-drivers/ackermann_msgs) | Ackermann 控制消息 | 150+ / 180+ | ROS messages for Ackermann steering. |
| 33 | [duckietown/dt-core](https://github.com/duckietown/dt-core) | Duckietown 自动车栈 | 300+ / 200+ | Code running the core stack on the Duckiebot in ROS. |
| 34 | [open-rmf/rmf_ros2](https://github.com/open-rmf/rmf_ros2) | 多机器人 fleet ROS2 集成 | 113 / 97 | Internal ROS infrastructure for RMF. |
| 35 | [clearpathrobotics/clearpath_common](https://github.com/clearpathrobotics/clearpath_common) | Clearpath 移动底盘通用包 | 200+ / 200+ | Clearpath mobile robot common packages. |
| 36 | [borglab/gtsam](https://github.com/borglab/gtsam) | 因子图估计 | 3k+ / 900+ | Smoothing and mapping library using factor graphs and Bayes networks. |
| 37 | [cartographer-project/cartographer](https://github.com/cartographer-project/cartographer) | 2D/3D SLAM | 7.9k / 2.3k | Real-time SLAM in 2D and 3D across platforms and sensor configurations. |
| 38 | [cartographer-project/cartographer_ros](https://github.com/cartographer-project/cartographer_ros) | Cartographer ROS 接入 | 2k+ / 1k+ | ROS integration for Cartographer. |
| 39 | [MRPT/mrpt](https://github.com/MRPT/mrpt) | 移动机器人程序库 | 2k+ / 700+ | The Mobile Robot Programming Toolkit. |
| 40 | [open-rmf/rmf_traffic](https://github.com/open-rmf/rmf_traffic) | 多机器人交通管理 | 100+ / 80+ | Traffic management libraries for RMF. |

## 后续拆解建议

- AMR/ROS 路线：优先拆 TurtleBot3、Move Base Flex、SBPL、SLAM Toolbox、Cartographer ROS、gazebo_ros_pkgs。
- 自动驾驶/赛车路线：优先拆 CommonRoad、TUMFTM 全局/局部轨迹规划、mod_vehicle_dynamics_control、ForzaETH、F1TENTH。
- 工程基础设施路线：优先拆 Autoware launch/core、ros2_control 仿真接口、Ackermann messages、RMF traffic、GTSAM/MRPT。

## 更新记录

- 2026-06-24：第二批整理 40 个未入库 GitHub 资源，并建立 40 篇单源笔记。
