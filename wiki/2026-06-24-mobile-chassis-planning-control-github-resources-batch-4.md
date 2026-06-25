---
id: "20260624-270000-mobile-chassis-planning-control-github-resources-batch-4"
title: "移动底盘规划控制 GitHub 资源精选（四）"
type: "topic"
source: ""
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-24-webots-planning-control-git-resource.md
  - notes/2026-06-24-sumo-planning-control-git-resource.md
  - notes/2026-06-24-esmini-planning-control-git-resource.md
  - notes/2026-06-24-chrono-planning-control-git-resource.md
  - notes/2026-06-24-open-simulation-interface-planning-control-git-resource.md
  - notes/2026-06-24-lanelet2-planning-control-git-resource.md
  - notes/2026-06-24-rosbag2-planning-control-git-resource.md
  - notes/2026-06-24-fast-dds-planning-control-git-resource.md
  - notes/2026-06-24-cyclonedds-planning-control-git-resource.md
  - notes/2026-06-24-foxglove-planning-control-git-resource.md
  - notes/2026-06-24-ros-foxglove-bridge-planning-control-git-resource.md
  - notes/2026-06-24-plotjuggler-planning-control-git-resource.md
  - notes/2026-06-24-rviz2-planning-control-git-resource.md
  - notes/2026-06-24-isaac-ros-visual-slam-planning-control-git-resource.md
  - notes/2026-06-24-velodyne-planning-control-git-resource.md
  - notes/2026-06-24-urg-node-planning-control-git-resource.md
  - notes/2026-06-24-sick-scan-xd-planning-control-git-resource.md
  - notes/2026-06-24-ouster-ros-planning-control-git-resource.md
  - notes/2026-06-24-livox-ros-driver2-planning-control-git-resource.md
  - notes/2026-06-24-realsense-ros-planning-control-git-resource.md
  - notes/2026-06-24-zed-ros2-wrapper-planning-control-git-resource.md
  - notes/2026-06-24-vins-fusion-planning-control-git-resource.md
  - notes/2026-06-24-vins-mono-planning-control-git-resource.md
  - notes/2026-06-24-lio-sam-planning-control-git-resource.md
  - notes/2026-06-24-fast-lio-planning-control-git-resource.md
  - notes/2026-06-24-fast-lio-localization-planning-control-git-resource.md
  - notes/2026-06-24-orb-slam3-planning-control-git-resource.md
  - notes/2026-06-24-stella-vslam-planning-control-git-resource.md
  - notes/2026-06-24-apriltag-planning-control-git-resource.md
  - notes/2026-06-24-carla-leaderboard-planning-control-git-resource.md
  - notes/2026-06-24-scenic-planning-control-git-resource.md
  - notes/2026-06-24-kobuki-ros-planning-control-git-resource.md
  - notes/2026-06-24-teleop-twist-keyboard-planning-control-git-resource.md
  - notes/2026-06-24-twist-mux-planning-control-git-resource.md
  - notes/2026-06-24-yujin-ocs-planning-control-git-resource.md
  - notes/2026-06-24-comma-cereal-planning-control-git-resource.md
  - notes/2026-06-24-comma-cabana-planning-control-git-resource.md
  - notes/2026-06-24-valhalla-planning-control-git-resource.md
  - notes/2026-06-24-osrm-backend-planning-control-git-resource.md
  - notes/2026-06-24-waymax-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（四）

## 当前判断

本页是第四批 40 个当前知识库未记录过的 GitHub 资源。相比前三批，本批重点补齐仿真与标准场景、交通路由、ROS2 中间件和数据工具、可视化调试、激光雷达/相机驱动、VIO/LIO/视觉 SLAM、测试场景生成、底盘命令工具和 openpilot CAN 分析链。

## 取舍边界

- 本批继续排除已入库 Git URL，包括前三批 120 个资源和历史已有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、TurtleBot、F1TENTH、RMF、MAVLink 等条目。
- 不是所有仓库都是 planner/controller：移动底盘规划控制还依赖仿真器、传感器驱动、定位、记录回放、可视化和控制命令仲裁。
- star/fork 是筛选信号，不是质量结论；后续真正使用前要看代码、许可证、维护状态和接口假设。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [cyberbotics/webots](https://github.com/cyberbotics/webots) | 机器人/自动驾驶仿真 | 3k+ / 1k+ | Open-source robot simulator used in industry, education and research. |
| 2 | [eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo) | 交通流仿真 | 2.8k+ / 1.5k+ | Microscopic and continuous multi-modal traffic simulation package. |
| 3 | [esmini/esmini](https://github.com/esmini/esmini) | OpenSCENARIO 仿真 | 900+ / 300+ | Environment simulator for OpenSCENARIO and OpenDRIVE. |
| 4 | [projectchrono/chrono](https://github.com/projectchrono/chrono) | 多体动力学/车辆仿真 | 2k+ / 700+ | Physics-based simulation infrastructure with vehicle and robotics modules. |
| 5 | [OpenSimulationInterface/open-simulation-interface](https://github.com/OpenSimulationInterface/open-simulation-interface) | 自动驾驶仿真接口标准 | 500+ / 250+ | Generic interface for the environmental perception of automated driving functions in virtual scenarios. |
| 6 | [fzi-forschungszentrum-informatik/Lanelet2](https://github.com/fzi-forschungszentrum-informatik/Lanelet2) | HD Map/车道地图 | 1.3k+ / 500+ | Map handling framework for automated driving, focused on lane-level maps. |
| 7 | [ros2/rosbag2](https://github.com/ros2/rosbag2) | ROS2 数据记录回放 | 500+ / 400+ | ROS2 bag recording and playback framework. |
| 8 | [eProsima/Fast-DDS](https://github.com/eProsima/Fast-DDS) | DDS/ROS2 中间件 | 2k+ / 900+ | DDS middleware implementation used in ROS 2 deployments. |
| 9 | [eclipse-cyclonedds/cyclonedds](https://github.com/eclipse-cyclonedds/cyclonedds) | DDS/ROS2 中间件 | 1k+ / 400+ | Eclipse Cyclone DDS implementation. |
| 10 | [foxglove/foxglove](https://github.com/foxglove/foxglove) | 机器人数据可视化 | 3k+ / 300+ | Visualization and observability platform for robotics data. |
| 11 | [foxglove/ros-foxglove-bridge](https://github.com/foxglove/ros-foxglove-bridge) | ROS 可视化桥接 | 600+ / 200+ | ROS 1/2 bridge for Foxglove websocket visualization. |
| 12 | [facontidavide/PlotJuggler](https://github.com/facontidavide/PlotJuggler) | 时序数据分析 | 3k+ / 500+ | Time series visualization and analysis tool with ROS support. |
| 13 | [ros2/rviz](https://github.com/ros2/rviz) | ROS2 可视化 | 600+ / 500+ | ROS2 3D visualization tool. |
| 14 | [NVIDIA-ISAAC-ROS/isaac_ros_visual_slam](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam) | ROS2 视觉 SLAM | 900+ / 200+ | NVIDIA accelerated stereo visual inertial SLAM ROS package. |
| 15 | [ros-drivers/velodyne](https://github.com/ros-drivers/velodyne) | 激光雷达驱动 | 700+ / 700+ | ROS support for Velodyne 3D LIDARs. |
| 16 | [ros-drivers/urg_node](https://github.com/ros-drivers/urg_node) | 2D 激光雷达驱动 | 300+ / 300+ | ROS driver for Hokuyo URG laser scanners. |
| 17 | [SICKAG/sick_scan_xd](https://github.com/SICKAG/sick_scan_xd) | SICK 激光雷达驱动 | 300+ / 200+ | ROS/ROS2 driver for SICK lidar and radar devices. |
| 18 | [ouster-lidar/ouster-ros](https://github.com/ouster-lidar/ouster-ros) | Ouster 激光雷达驱动 | 600+ / 400+ | ROS drivers for Ouster lidar sensors. |
| 19 | [Livox-SDK/livox_ros_driver2](https://github.com/Livox-SDK/livox_ros_driver2) | Livox 激光雷达驱动 | 700+ / 500+ | ROS2/ROS1 driver for Livox lidar. |
| 20 | [IntelRealSense/realsense-ros](https://github.com/IntelRealSense/realsense-ros) | 深度相机 ROS 驱动 | 3k+ / 2k+ | ROS wrapper for Intel RealSense devices. |
| 21 | [stereolabs/zed-ros2-wrapper](https://github.com/stereolabs/zed-ros2-wrapper) | 双目/视觉定位 ROS2 驱动 | 700+ / 300+ | ROS2 wrapper for Stereolabs ZED cameras. |
| 22 | [HKUST-Aerial-Robotics/VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) | 视觉惯性定位 | 4k+ / 1.5k+ | Optimization-based multi-sensor state estimator. |
| 23 | [HKUST-Aerial-Robotics/VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono) | 单目视觉惯性定位 | 4k+ / 1.6k+ | Monocular visual-inertial system for state estimation. |
| 24 | [TixiaoShan/LIO-SAM](https://github.com/TixiaoShan/LIO-SAM) | 激光惯性 SLAM | 3k+ / 1k+ | Lidar inertial odometry via smoothing and mapping. |
| 25 | [hku-mars/FAST_LIO](https://github.com/hku-mars/FAST_LIO) | 激光惯性里程计 | 4k+ / 1k+ | Fast LiDAR-inertial odometry package. |
| 26 | [hku-mars/FAST_LIO_LOCALIZATION](https://github.com/hku-mars/FAST_LIO_LOCALIZATION) | 激光定位 | 1k+ / 300+ | Localization package based on FAST-LIO. |
| 27 | [UZ-SLAMLab/ORB_SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) | 视觉/视觉惯性 SLAM | 7k+ / 2k+ | Visual, visual-inertial and multi-map SLAM library. |
| 28 | [stella-cv/stella_vslam](https://github.com/stella-cv/stella_vslam) | 视觉 SLAM | 2k+ / 500+ | Open-source visual SLAM library forked from OpenVSLAM. |
| 29 | [AprilRobotics/apriltag](https://github.com/AprilRobotics/apriltag) | 视觉定位标记 | 4k+ / 1k+ | AprilTag visual fiducial detection library. |
| 30 | [carla-simulator/leaderboard](https://github.com/carla-simulator/leaderboard) | 自动驾驶评测 | 700+ / 400+ | Leaderboard and evaluation framework for autonomous driving agents in CARLA. |
| 31 | [BerkeleyLearnVerify/Scenic](https://github.com/BerkeleyLearnVerify/Scenic) | 场景生成语言 | 1k+ / 200+ | Probabilistic programming language for scenario generation. |
| 32 | [kobuki-base/kobuki_ros](https://github.com/kobuki-base/kobuki_ros) | 差速底盘 ROS 包 | 300+ / 300+ | ROS packages for Kobuki mobile base. |
| 33 | [ros-teleop/teleop_twist_keyboard](https://github.com/ros-teleop/teleop_twist_keyboard) | 手动控制工具 | 500+ / 500+ | Keyboard teleoperation node publishing Twist commands. |
| 34 | [ros-teleop/twist_mux](https://github.com/ros-teleop/twist_mux) | 速度命令仲裁 | 300+ / 250+ | Twist multiplexer for ROS. |
| 35 | [yujinrobot/yujin_ocs](https://github.com/yujinrobot/yujin_ocs) | 移动底盘速度平滑/工具 | 200+ / 200+ | Yujin Open Control System packages, including velocity smoother and mux tools. |
| 36 | [commaai/cereal](https://github.com/commaai/cereal) | openpilot 消息定义 | 500+ / 300+ | Message and logging schema used by comma.ai stack. |
| 37 | [commaai/cabana](https://github.com/commaai/cabana) | CAN 数据分析 | 700+ / 200+ | CAN bus reverse engineering and analysis tool. |
| 38 | [valhalla/valhalla](https://github.com/valhalla/valhalla) | 道路路由引擎 | 5k+ / 1k+ | Open-source routing engine and accompanying libraries. |
| 39 | [Project-OSRM/osrm-backend](https://github.com/Project-OSRM/osrm-backend) | 道路路由引擎 | 6k+ / 4k+ | High performance routing engine for OpenStreetMap. |
| 40 | [waymo-research/waymax](https://github.com/waymo-research/waymax) | 自动驾驶规划仿真 | 1k+ / 150+ | JAX-based simulator for autonomous driving research. |

## 后续拆解建议

- 仿真与标准：优先拆 Webots、SUMO、esmini、Chrono、OSI、CARLA Leaderboard、Scenic、Waymax。
- 数据与调试：优先拆 rosbag2、Foxglove、ros-foxglove-bridge、PlotJuggler、RViz2。
- 感知定位输入：优先拆 velodyne、ouster_ros、livox_ros_driver2、realsense_ros、VINS-Fusion、LIO-SAM、FAST-LIO、ORB-SLAM3。
- 底盘接口与路由：优先拆 Lanelet2、teleop_twist_keyboard、twist_mux、cereal、cabana、Valhalla、OSRM。

## 更新记录

- 2026-06-24：第四批整理 40 个未入库 GitHub 资源，并建立 40 篇单源笔记。
