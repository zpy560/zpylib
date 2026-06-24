---
id: "20260624-230000-mobile-chassis-planning-control-github-resources"
title: "移动底盘规划控制 GitHub 资源精选"
type: "topic"
source: ""
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-24-carla-simulator-planning-control-git-resource.md
  - notes/2026-06-24-airsim-planning-control-git-resource.md
  - notes/2026-06-24-svl-simulator-planning-control-git-resource.md
  - notes/2026-06-24-carla-ros-bridge-planning-control-git-resource.md
  - notes/2026-06-24-carla-scenario-runner-planning-control-git-resource.md
  - notes/2026-06-24-pylot-planning-control-git-resource.md
  - notes/2026-06-24-autoware-universe-planning-control-git-resource.md
  - notes/2026-06-24-scenario-simulator-v2-planning-control-git-resource.md
  - notes/2026-06-24-comma-panda-planning-control-git-resource.md
  - notes/2026-06-24-comma-opendbc-planning-control-git-resource.md
  - notes/2026-06-24-karlkurzer-path-planner-planning-control-git-resource.md
  - notes/2026-06-24-neonavigation-planning-control-git-resource.md
  - notes/2026-06-24-ros-3d-navigation-planning-control-git-resource.md
  - notes/2026-06-24-rsband-local-planner-planning-control-git-resource.md
  - notes/2026-06-24-art-planner-planning-control-git-resource.md
  - notes/2026-06-24-quadrotor-yrlu-planning-control-git-resource.md
  - notes/2026-06-24-rotors-simulator-planning-control-git-resource.md
  - notes/2026-06-24-mav-control-rw-planning-control-git-resource.md
  - notes/2026-06-24-voxblox-planning-control-git-resource.md
  - notes/2026-06-24-fuel-planning-control-git-resource.md
  - notes/2026-06-24-ego-planner-swarm-planning-control-git-resource.md
  - notes/2026-06-24-gcopter-planning-control-git-resource.md
  - notes/2026-06-24-teach-repeat-replan-planning-control-git-resource.md
  - notes/2026-06-24-ardupilot-planning-control-git-resource.md
  - notes/2026-06-24-mavros-planning-control-git-resource.md
  - notes/2026-06-24-ros-control-planning-control-git-resource.md
  - notes/2026-06-24-ros-controllers-planning-control-git-resource.md
  - notes/2026-06-24-husky-planning-control-git-resource.md
  - notes/2026-06-24-legged-gym-planning-control-git-resource.md
  - notes/2026-06-24-rsl-rl-planning-control-git-resource.md
  - notes/2026-06-24-grid-map-planning-control-git-resource.md
  - notes/2026-06-24-elevation-mapping-planning-control-git-resource.md
  - notes/2026-06-24-traversability-estimation-planning-control-git-resource.md
  - notes/2026-06-24-free-gait-planning-control-git-resource.md
  - notes/2026-06-24-unitree-ros-planning-control-git-resource.md
  - notes/2026-06-24-unitree-ros2-planning-control-git-resource.md
  - notes/2026-06-24-unitree-mujoco-planning-control-git-resource.md
  - notes/2026-06-24-mujoco-planning-control-git-resource.md
  - notes/2026-06-24-isaac-lab-planning-control-git-resource.md
  - notes/2026-06-24-isaac-ros-nvblox-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选

## 当前判断

本页收录 40 个当前知识库未记录过的 GitHub 资源，覆盖整车仿真、车辆接口、Autoware/CARLA 生态、Ackermann/AMR 导航、无人机规划控制、腿式/Unitree 底盘、机器人学习仿真和三维建图。筛选优先级是：业界或社区使用度高、star/fork 尽量高、能补齐现有 Apollo/Autoware/Nav2/PX4/openpilot 等条目的空白。

## 取舍边界

- 本轮排除了知识库中已经出现过的 Git URL，包括 Apollo、Autoware meta、Navigation2、openpilot、PX4、TEB、mpc_local_planner、Fast-Planner、EGO-Planner、OMPL、Ruckig、OCS2 等。
- 不是所有仓库都是规划器：仿真、地图、车辆接口、控制框架和学习控制环境同样是移动底盘规划控制闭环的关键部分。
- star/fork 是筛选信号，不是质量结论；后续真正使用前要看代码、许可证、维护状态和接口假设。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [carla-simulator/carla](https://github.com/carla-simulator/carla) | 整车仿真 | 14k+ / 4.6k+ | 自动驾驶研究仿真器，适合规划、控制、传感器和交通场景闭环验证。 |
| 2 | [microsoft/AirSim](https://github.com/microsoft/AirSim) | 无人机/车辆仿真 | 18k+ / 4.9k+ | Microsoft 开源的无人机和车辆仿真平台，支持 PX4/ArduPilot SITL/HIL。 |
| 3 | [lgsvl/simulator](https://github.com/lgsvl/simulator) | 整车仿真 | 2.4k+ / 790+ | 面向 Autoware/Apollo 的 ROS/ROS2 多机器人自动驾驶仿真器。 |
| 4 | [carla-simulator/ros-bridge](https://github.com/carla-simulator/ros-bridge) | 仿真 ROS 接口 | 630+ / 520+ | CARLA 到 ROS/ROS2 的桥接层，包含车辆状态、传感器和控制命令接口。 |
| 5 | [carla-simulator/scenario_runner](https://github.com/carla-simulator/scenario_runner) | 场景测试 | 660+ / 430+ | CARLA 交通场景定义与执行引擎。 |
| 6 | [erdos-project/pylot](https://github.com/erdos-project/pylot) | 自动驾驶软件栈 | 530+ / 130+ | 运行在 CARLA 和真实车辆上的模块化自动驾驶平台。 |
| 7 | [autowarefoundation/autoware.universe](https://github.com/autowarefoundation/autoware.universe) | 自动驾驶软件栈 | 1.7k+ / 900+ | Autoware 的规划、控制、感知等 ROS2 模块实现主仓。 |
| 8 | [tier4/scenario_simulator_v2](https://github.com/tier4/scenario_simulator_v2) | Autoware 场景测试 | 150+ / 70+ | TIER IV/Autoware 生态的 scenario testing framework。 |
| 9 | [commaai/panda](https://github.com/commaai/panda) | 车辆接口 | 1.7k+ / 950+ | comma.ai panda 车辆 CAN 接口硬件与固件代码。 |
| 10 | [commaai/opendbc](https://github.com/commaai/opendbc) | 车辆信号抽象 | 3.2k+ / 2k+ | 车辆 CAN DBC 和 Python API。 |
| 11 | [karlkurzer/path_planner](https://github.com/karlkurzer/path_planner) | 车辆路径规划 | 1.9k+ / 560+ | 面向 KTH Research Concept Vehicle 的 Hybrid A* 路径规划器。 |
| 12 | [at-wat/neonavigation](https://github.com/at-wat/neonavigation) | AMR 二维导航 | 340+ / 90+ | ROS 2D/3DOF seamless global/local mobile robot motion planner package。 |
| 13 | [ros-planning/3d_navigation](https://github.com/ros-planning/3d_navigation) | 3D 避障导航 | 200+ / 60+ | move_base 全局/局部 planner 插件，使用 3D robot mesh 和 octomap 做避障。 |
| 14 | [gkouros/rsband_local_planner](https://github.com/gkouros/rsband_local_planner) | Ackermann 局部规划 | 170+ / 50+ | 面向 Ackermann 或四轮转向 car-like robots 的 ROS move_base local planner 插件。 |
| 15 | [leggedrobotics/art_planner](https://github.com/leggedrobotics/art_planner) | 腿式局部导航 | 230+ / 20+ | 腿式机器人的局部导航规划器。 |
| 16 | [yrlu/quadrotor](https://github.com/yrlu/quadrotor) | 四旋翼规划控制 | 1.1k+ / 300+ | 四旋翼控制、路径规划和轨迹优化示例。 |
| 17 | [ethz-asl/rotors_simulator](https://github.com/ethz-asl/rotors_simulator) | 无人机仿真 | 1.5k+ / 780+ | ETH ASL UAV Gazebo simulator。 |
| 18 | [ethz-asl/mav_control_rw](https://github.com/ethz-asl/mav_control_rw) | 无人机控制 | 440+ / 160+ | 旋翼 MAV 的 ROS 控制策略集合，含 linear/nonlinear MPC。 |
| 19 | [ethz-asl/voxblox](https://github.com/ethz-asl/voxblox) | 三维地图基础 | 1.6k+ / 390+ | TSDF/ESDF 体素地图基础库。 |
| 20 | [HKUST-Aerial-Robotics/FUEL](https://github.com/HKUST-Aerial-Robotics/FUEL) | 无人机探索规划 | 1.4k+ / 250+ | Fast UAV Exploration framework。 |
| 21 | [ZJU-FAST-Lab/ego-planner-swarm](https://github.com/ZJU-FAST-Lab/ego-planner-swarm) | 无人机多机规划 | 2.1k+ / 360+ | 单机/多机 multicopter trajectory planner。 |
| 22 | [ZJU-FAST-Lab/GCOPTER](https://github.com/ZJU-FAST-Lab/GCOPTER) | 无人机轨迹优化 | 1.2k+ / 200+ | 多旋翼通用轨迹优化器。 |
| 23 | [HKUST-Aerial-Robotics/Teach-Repeat-Replan](https://github.com/HKUST-Aerial-Robotics/Teach-Repeat-Replan) | 无人机重复飞行 | 1.1k+ / 260+ | 复杂环境激进飞行的 Teach-Repeat-Replan 系统。 |
| 24 | [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | 无人系统飞控/车控 | 15k+ / 21k+ | 覆盖 Copter、Plane、Rover、Sub 的开源 autopilot。 |
| 25 | [mavlink/mavros](https://github.com/mavlink/mavros) | MAVLink ROS 接口 | 1.2k+ / 1.1k+ | MAVLink to ROS gateway with GCS proxy。 |
| 26 | [ros-controls/ros_control](https://github.com/ros-controls/ros_control) | ROS1 控制框架 | 520+ / 300+ | ROS1 通用控制框架。 |
| 27 | [ros-controls/ros_controllers](https://github.com/ros-controls/ros_controllers) | ROS1 控制器 | 610+ / 520+ | 伴随 ros_control 的通用机器人控制器集合。 |
| 28 | [husky/husky](https://github.com/husky/husky) | UGV 底盘平台 | 500+ / 430+ | Clearpath Husky 的 ROS 仿真、描述、控制和导航包。 |
| 29 | [leggedrobotics/legged_gym](https://github.com/leggedrobotics/legged_gym) | 腿式学习控制 | 3k+ / 570+ | Isaac Gym Environments for Legged Robots。 |
| 30 | [leggedrobotics/rsl_rl](https://github.com/leggedrobotics/rsl_rl) | 机器人强化学习 | 2.7k+ / 620+ | 机器人学习算法的快速简单实现。 |
| 31 | [ANYbotics/grid_map](https://github.com/ANYbotics/grid_map) | 移动机器人地图 | 3.2k+ / 870+ | 移动机器人通用多层 grid map 库。 |
| 32 | [ANYbotics/elevation_mapping](https://github.com/ANYbotics/elevation_mapping) | 粗糙地形建图 | 1.8k+ / 500+ | 面向 rough terrain navigation 的机器人中心高程地图。 |
| 33 | [leggedrobotics/traversability_estimation](https://github.com/leggedrobotics/traversability_estimation) | 可通行性估计 | 490+ / 100+ | 移动机器人粗糙地形可通行性地图。 |
| 34 | [leggedrobotics/free_gait](https://github.com/leggedrobotics/free_gait) | 腿式步态控制 | 440+ / 120+ | 腿式机器人通用控制架构。 |
| 35 | [unitreerobotics/unitree_ros](https://github.com/unitreerobotics/unitree_ros) | Unitree ROS1 | 1.4k+ / 430+ | Unitree 四足机器人的 ROS1 接口与仿真包。 |
| 36 | [unitreerobotics/unitree_ros2](https://github.com/unitreerobotics/unitree_ros2) | Unitree ROS2 | 730+ / 210+ | Unitree 四足机器人的 ROS2 接口与示例。 |
| 37 | [unitreerobotics/unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco) | Unitree 仿真 | 1k+ / 350+ | Unitree SDK2 与 MuJoCo 的仿真桥。 |
| 38 | [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 动力学仿真 | 14k+ / 1.6k+ | Multi-Joint dynamics with Contact 通用物理仿真器。 |
| 39 | [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 机器人学习仿真 | 7.5k+ / 3.7k+ | 基于 Isaac Sim 的机器人学习、运动规划和仿真框架。 |
| 40 | [NVIDIA-ISAAC-ROS/isaac_ros_nvblox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox) | ROS2 三维建图 | 700+ / 130+ | GPU 3D scene reconstruction and Nav2 local costmap provider。 |

## 后续拆解建议

- 第一优先级：Autoware Universe 的 `planning/`、`control/`，CARLA/Scenario Runner 的场景回归链，ArduPilot Rover/PX4 Rover 的模式与控制边界。
- 第二优先级：grid_map、elevation_mapping、traversability_estimation、isaac_ros_nvblox，整理“感知地图到局部规划代价”的输入链。
- 第三优先级：legged_gym、rsl_rl、Isaac Lab、unitree_mujoco，整理腿式底盘学习控制从仿真到实机接口的工程链。

## 更新记录

- 2026-06-24：首次整理 40 个未入库 GitHub 资源，并建立 40 篇单源笔记。
