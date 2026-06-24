---
id: "20260624-250000-mobile-chassis-planning-control-github-resources-batch-3"
title: "移动底盘规划控制 GitHub 资源精选（三）"
type: "topic"
source: ""
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-24-robot-localization-planning-control-git-resource.md
  - notes/2026-06-24-geometry2-planning-control-git-resource.md
  - notes/2026-06-24-robot-state-publisher-planning-control-git-resource.md
  - notes/2026-06-24-realtime-tools-planning-control-git-resource.md
  - notes/2026-06-24-control-msgs-planning-control-git-resource.md
  - notes/2026-06-24-ros-control-toolbox-planning-control-git-resource.md
  - notes/2026-06-24-ros2-control-demos-planning-control-git-resource.md
  - notes/2026-06-24-gz-ros2-control-planning-control-git-resource.md
  - notes/2026-06-24-gz-sim-planning-control-git-resource.md
  - notes/2026-06-24-ros-gz-planning-control-git-resource.md
  - notes/2026-06-24-fcl-planning-control-git-resource.md
  - notes/2026-06-24-coal-planning-control-git-resource.md
  - notes/2026-06-24-bullet3-planning-control-git-resource.md
  - notes/2026-06-24-ceres-solver-planning-control-git-resource.md
  - notes/2026-06-24-pcl-planning-control-git-resource.md
  - notes/2026-06-24-open3d-planning-control-git-resource.md
  - notes/2026-06-24-tsid-planning-control-git-resource.md
  - notes/2026-06-24-opencda-planning-control-git-resource.md
  - notes/2026-06-24-carma-platform-planning-control-git-resource.md
  - notes/2026-06-24-autoware-auto-msgs-planning-control-git-resource.md
  - notes/2026-06-24-autoware-auto-planning-control-git-resource.md
  - notes/2026-06-24-autoware-ai-planning-control-git-resource.md
  - notes/2026-06-24-autoware-tools-planning-control-git-resource.md
  - notes/2026-06-24-commonroad-vehicle-models-planning-control-git-resource.md
  - notes/2026-06-24-commonroad-reactive-planner-planning-control-git-resource.md
  - notes/2026-06-24-commonroad-sumo-interface-planning-control-git-resource.md
  - notes/2026-06-24-fields2cover-planning-control-git-resource.md
  - notes/2026-06-24-python-motion-planning-planning-control-git-resource.md
  - notes/2026-06-24-ego-planner-v2-planning-control-git-resource.md
  - notes/2026-06-24-racer-planning-control-git-resource.md
  - notes/2026-06-24-kimera-vio-planning-control-git-resource.md
  - notes/2026-06-24-kimera-semantics-planning-control-git-resource.md
  - notes/2026-06-24-rmf-demos-planning-control-git-resource.md
  - notes/2026-06-24-rmf-task-planning-control-git-resource.md
  - notes/2026-06-24-jackal-planning-control-git-resource.md
  - notes/2026-06-24-clearpath-simulator-planning-control-git-resource.md
  - notes/2026-06-24-metadrive-planning-control-git-resource.md
  - notes/2026-06-24-self-driving-car-sim-planning-control-git-resource.md
  - notes/2026-06-24-qgroundcontrol-planning-control-git-resource.md
  - notes/2026-06-24-mavlink-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（三）

## 当前判断

本页是第三批 40 个当前知识库未记录过的 GitHub 资源。相比前两批，本批重点补齐移动底盘闭环的基础设施层：状态估计、tf/URDF 状态发布、实时控制工具、现代 Gazebo 仿真、碰撞检测、点云处理、非线性优化、协同自动驾驶、Autoware 历史与工具链、CommonRoad 车辆模型/反应式规划、无人机重规划、MAVLink 协议和地面站。

## 取舍边界

- 本批继续排除已入库 Git URL，包括前两批 80 个资源和历史已有 Apollo、Autoware meta、Nav2、PX4、openpilot、CARLA、ArduPilot、TurtleBot3、F1TENTH、RMF 等条目。
- 不是所有仓库都是 planner/controller：移动底盘规划控制还依赖定位、坐标、仿真、碰撞、优化、通信协议和调试评测工具。
- star/fork 是筛选信号，不是质量结论；后续真正使用前要看代码、许可证、维护状态和接口假设。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [cra-ros-pkg/robot_localization](https://github.com/cra-ros-pkg/robot_localization) | 状态估计/定位融合 | 1.1k+ / 700+ | ROS package for nonlinear state estimation through sensor fusion. |
| 2 | [ros2/geometry2](https://github.com/ros2/geometry2) | 坐标变换基础设施 | 600+ / 400+ | ROS2 geometry2 repository, including tf2 libraries and tools. |
| 3 | [ros/robot_state_publisher](https://github.com/ros/robot_state_publisher) | 机器人状态发布 | 300+ / 200+ | Publishes robot state to tf from joint states and URDF. |
| 4 | [ros-controls/realtime_tools](https://github.com/ros-controls/realtime_tools) | 实时控制工具 | 300+ / 180+ | Realtime-safe utilities for ROS control code. |
| 5 | [ros-controls/control_msgs](https://github.com/ros-controls/control_msgs) | 控制消息接口 | 170+ / 220+ | Standard ROS control messages and actions. |
| 6 | [ros-controls/control_toolbox](https://github.com/ros-controls/control_toolbox) | ROS 控制工具箱 | 250+ / 220+ | Control toolbox containing PID and control utilities. |
| 7 | [ros-controls/ros2_control_demos](https://github.com/ros-controls/ros2_control_demos) | ros2_control 示例 | 400+ / 300+ | Examples and demonstrations for ros2_control. |
| 8 | [ros-controls/gz_ros2_control](https://github.com/ros-controls/gz_ros2_control) | Modern Gazebo 控制接口 | 180+ / 90+ | ros2_control integration with modern Gazebo / gz-sim. |
| 9 | [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | 机器人仿真平台 | 1k+ / 500+ | Open source robotics simulator, formerly Ignition Gazebo. |
| 10 | [gazebosim/ros_gz](https://github.com/gazebosim/ros_gz) | ROS-Gazebo 桥接 | 400+ / 250+ | ROS integration for Gazebo / gz transport. |
| 11 | [flexible-collision-library/fcl](https://github.com/flexible-collision-library/fcl) | 碰撞检测库 | 1.1k+ / 500+ | Flexible Collision Library for proximity queries. |
| 12 | [coal-library/coal](https://github.com/coal-library/coal) | 碰撞检测库 | 400+ / 100+ | Collision detection library, successor/continuation of hpp-fcl ecosystem. |
| 13 | [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) | 物理仿真/碰撞 | 13k+ / 3k+ | Real-time collision detection and multi-physics simulation SDK. |
| 14 | [ceres-solver/ceres-solver](https://github.com/ceres-solver/ceres-solver) | 非线性最小二乘优化 | 8k+ / 1.8k+ | Large scale nonlinear optimization library. |
| 15 | [PointCloudLibrary/pcl](https://github.com/PointCloudLibrary/pcl) | 点云处理基础库 | 10k+ / 4.8k+ | Point Cloud Library for 2D/3D image and point cloud processing. |
| 16 | [isl-org/Open3D](https://github.com/isl-org/Open3D) | 3D 数据处理 | 13k+ / 2.9k+ | Open-source library for 3D data processing. |
| 17 | [stack-of-tasks/tsid](https://github.com/stack-of-tasks/tsid) | 任务空间逆动力学控制 | 500+ / 150+ | Task Space Inverse Dynamics for robots. |
| 18 | [ucla-mobility/OpenCDA](https://github.com/ucla-mobility/OpenCDA) | 车路协同自动驾驶 | 600+ / 200+ | Open cooperative driving automation framework based on CARLA. |
| 19 | [usdot-fhwa-stol/carma-platform](https://github.com/usdot-fhwa-stol/carma-platform) | 协同自动驾驶平台 | 300+ / 200+ | USDOT CARMA cooperative automation platform. |
| 20 | [autowarefoundation/autoware_auto_msgs](https://github.com/autowarefoundation/autoware_auto_msgs) | Autoware 消息接口 | 100+ / 200+ | Message definitions for Autoware.Auto and Autoware ecosystems. |
| 21 | [autowarefoundation/autoware.auto](https://github.com/autowarefoundation/autoware.auto) | 自动驾驶软件栈历史分支 | 800+ / 400+ | Autoware.Auto autonomous driving stack. |
| 22 | [autowarefoundation/autoware_ai](https://github.com/autowarefoundation/autoware_ai) | ROS1 自动驾驶平台历史栈 | 2k+ / 1.5k+ | Legacy ROS1 Autoware autonomous driving stack. |
| 23 | [autowarefoundation/autoware_tools](https://github.com/autowarefoundation/autoware_tools) | Autoware 调试/标定/评测工具 | 38 / 63 | Non-runtime Autoware packages for benchmarking, debugging, tuning, calibrating, etc. |
| 24 | [CommonRoad/commonroad-vehicle-models](https://github.com/CommonRoad/commonroad-vehicle-models) | 车辆模型 | 100+ / 40+ | Vehicle models for CommonRoad planning benchmarks. |
| 25 | [CommonRoad/commonroad-reactive-planner](https://github.com/CommonRoad/commonroad-reactive-planner) | 反应式轨迹规划 | 120+ / 40+ | Reactive planner for CommonRoad scenarios. |
| 26 | [CommonRoad/commonroad-sumo-interface](https://github.com/CommonRoad/commonroad-sumo-interface) | 交通仿真接口 | 80+ / 30+ | SUMO interface for CommonRoad scenarios. |
| 27 | [Fields2Cover/Fields2Cover](https://github.com/Fields2Cover/Fields2Cover) | 覆盖路径规划 | 700+ / 180+ | Coverage path planning library for agricultural and field robots. |
| 28 | [ai-winter/python_motion_planning](https://github.com/ai-winter/python_motion_planning) | 规划算法实验 | 500+ / 120+ | Python implementation of common motion planning algorithms. |
| 29 | [ZJU-FAST-Lab/ego-planner-v2](https://github.com/ZJU-FAST-Lab/ego-planner-v2) | 无人机局部规划 | 800+ / 150+ | Newer EGO-Planner variant from ZJU FAST Lab. |
| 30 | [HKUST-Aerial-Robotics/RACER](https://github.com/HKUST-Aerial-Robotics/RACER) | 无人机探索/重规划 | 900+ / 150+ | Rapid collaborative exploration with aerial robots. |
| 31 | [MIT-SPARK/Kimera-VIO](https://github.com/MIT-SPARK/Kimera-VIO) | 视觉惯性里程计 | 1.8k+ / 500+ | Visual-inertial odometry library from MIT SPARK. |
| 32 | [MIT-SPARK/Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics) | 语义建图 | 1k+ / 250+ | Metric-semantic mapping for robotics. |
| 33 | [open-rmf/rmf_demos](https://github.com/open-rmf/rmf_demos) | 多机器人调度示例 | 200+ / 150+ | Demonstrations for Open-RMF. |
| 34 | [open-rmf/rmf_task](https://github.com/open-rmf/rmf_task) | 多机器人任务分配 | 80+ / 60+ | RMF library for managing task allocations. |
| 35 | [jackal/jackal](https://github.com/jackal/jackal) | UGV 底盘平台 | 184 / 152 | Common packages for Jackal, including messages, robot description, navigation and controllers. |
| 36 | [clearpathrobotics/clearpath_simulator](https://github.com/clearpathrobotics/clearpath_simulator) | Clearpath 仿真 | 200+ / 150+ | Simulation packages for Clearpath robots. |
| 37 | [metadriverse/metadrive](https://github.com/metadriverse/metadrive) | 自动驾驶仿真/RL | 1.5k+ / 300+ | Compositional driving simulator for reinforcement learning and autonomous driving. |
| 38 | [udacity/self-driving-car-sim](https://github.com/udacity/self-driving-car-sim) | 自动驾驶教学仿真 | 5k+ / 2k+ | Unity-based simulator for Udacity self-driving car projects. |
| 39 | [mavlink/qgroundcontrol](https://github.com/mavlink/qgroundcontrol) | 无人系统地面站 | 3k+ / 3k+ | Ground control station for MAVLink-based vehicles. |
| 40 | [mavlink/mavlink](https://github.com/mavlink/mavlink) | 无人系统通信协议 | 1.9k+ / 1.5k+ | MAVLink protocol message definitions and generators. |

## 后续拆解建议

- 底盘闭环基础：优先拆 robot_localization、geometry2、robot_state_publisher、realtime_tools、control_msgs、control_toolbox。
- 仿真与几何：优先拆 gz-sim、ros_gz、gz_ros2_control、FCL、COAL、Bullet、PCL、Open3D。
- 自动驾驶与协同：优先拆 OpenCDA、CARMA、Autoware.Auto/AI/tools、CommonRoad reactive planner、Fields2Cover、MetaDrive。
- 无人系统接口：优先拆 MAVLink、QGroundControl、EGO-Planner-v2、RACER、Kimera-VIO/Semantics。

## 更新记录

- 2026-06-24：第三批整理 40 个未入库 GitHub 资源，并建立 40 篇单源笔记。
