---
id: "20260625-070000-mobile-chassis-planning-control-github-resources-batch-7"
title: "移动底盘规划控制 GitHub 资源精选（七）"
type: "topic"
source: ""
created_at: "2026-06-25"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-25-cyberbotics-webots-ros2-planning-control-git-resource.md
  - notes/2026-06-25-mavlink-mavsdk-planning-control-git-resource.md
  - notes/2026-06-25-px4-px4-sitl-gazebo-classic-planning-control-git-resource.md
  - notes/2026-06-25-hanruihua-ir-sim-planning-control-git-resource.md
  - notes/2026-06-25-ardupilot-mavproxy-planning-control-git-resource.md
  - notes/2026-06-25-giacomo-b-cpprobotics-planning-control-git-resource.md
  - notes/2026-06-25-ros2-rclcpp-planning-control-git-resource.md
  - notes/2026-06-25-naturerobots-mesh-navigation-planning-control-git-resource.md
  - notes/2026-06-25-zhengyinan-air-diffusion-planner-planning-control-git-resource.md
  - notes/2026-06-25-ethz-adrl-towr-planning-control-git-resource.md
  - notes/2026-06-25-zhefan-xu-cerlab-uav-autonomy-planning-control-git-resource.md
  - notes/2026-06-25-ros2-examples-planning-control-git-resource.md
  - notes/2026-06-25-linorobot-linorobot2-planning-control-git-resource.md
  - notes/2026-06-25-huawei-noah-smarts-planning-control-git-resource.md
  - notes/2026-06-25-linorobot-linorobot-planning-control-git-resource.md
  - notes/2026-06-25-autowarefoundation-awsim-planning-control-git-resource.md
  - notes/2026-06-25-autonomousvision-navsim-planning-control-git-resource.md
  - notes/2026-06-25-rsasaki0109-rust-robotics-planning-control-git-resource.md
  - notes/2026-06-25-snape-rvo2-planning-control-git-resource.md
  - notes/2026-06-25-6-robot-wpr-simulation-planning-control-git-resource.md
  - notes/2026-06-25-eclipse-ecal-ecal-planning-control-git-resource.md
  - notes/2026-06-25-timthony-self-drive-planning-control-git-resource.md
  - notes/2026-06-25-prbonn-semantic-suma-planning-control-git-resource.md
  - notes/2026-06-25-louiszengcn-carlaair-planning-control-git-resource.md
  - notes/2026-06-25-shunichi09-pythonlinearnonlinearcontrol-planning-control-git-resource.md
  - notes/2026-06-25-teddyluo-hybrid-a-star-annotation-planning-control-git-resource.md
  - notes/2026-06-25-robosense-lidar-rslidar-sdk-planning-control-git-resource.md
  - notes/2026-06-25-wh200720041-iscloam-planning-control-git-resource.md
  - notes/2026-06-25-yashbansod-robotics-planning-dynamics-and-control-planning-control-git-resource.md
  - notes/2026-06-25-ros2-demos-planning-control-git-resource.md
  - notes/2026-06-25-sollimann-cleanit-planning-control-git-resource.md
  - notes/2026-06-25-mizuhoaoki-python-simple-mppi-planning-control-git-resource.md
  - notes/2026-06-25-koide3-ndt-omp-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（七）

## 当前判断

本页是第 7 批当前知识库未记录过的 GitHub 资源。筛选优先级是：与移动底盘规划控制直接相关，其次是规划控制落地必须依赖的定位建图、传感器接口、仿真验证、ROS/机器人基础设施和无人系统接口。

## 取舍边界

- 已排除当前知识库中已经出现过的 GitHub 仓库 URL。
- star/fork 是筛选信号，不是质量结论；真正使用前仍要检查许可证、维护状态、接口假设和源码实现。
- 本批保留部分非 planner/controller 仓库，因为底盘规划控制系统需要可靠的定位、建图、仿真、消息通信和硬件接口。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [cyberbotics/webots_ros2](https://github.com/cyberbotics/webots_ros2) | 导航/路径规划 | 539 / 186 | Webots ROS 2 packages |
| 2 | [mavlink/MAVSDK](https://github.com/mavlink/MAVSDK) | 机器人基础设施/接口 | 895 / 625 | API and library for MAVLink compatible systems written in C++ 20 |
| 3 | [PX4/PX4-SITL_gazebo-classic](https://github.com/PX4/PX4-SITL_gazebo-classic) | 定位建图/状态估计 | 458 / 841 | Set of plugins, models and worlds to use with OSRF Gazebo Simulator in SITL and HITL. |
| 4 | [hanruihua/ir-sim](https://github.com/hanruihua/ir-sim) | 控制/最优控制 | 1.1k+ / 141 | A  Python-based lightweight robot simulator designed for navigation, control, and learning |
| 5 | [ArduPilot/MAVProxy](https://github.com/ArduPilot/MAVProxy) | 机器人基础设施/接口 | 581 / 771 | MAVLink proxy and command line ground station |
| 6 | [giacomo-b/CppRobotics](https://github.com/giacomo-b/CppRobotics) | 控制/最优控制 | 495 / 58 | Header-only C++ library for robotics, control, and path planning algorithms. Work in progress, contributions are welcome! |
| 7 | [ros2/rclcpp](https://github.com/ros2/rclcpp) | 机器人基础设施/接口 | 771 / 539 | rclcpp (ROS Client Library for C++) |
| 8 | [naturerobots/mesh_navigation](https://github.com/naturerobots/mesh_navigation) | 控制/最优控制 | 862 / 104 | The Mesh Navigation Stack: Efficient Mobile Robot Navigation in Uneven Terrain |
| 9 | [ZhengYinan-AIR/Diffusion-Planner](https://github.com/ZhengYinan-AIR/Diffusion-Planner) | 导航/路径规划 | 1.0k+ / 156 | [ICLR 2025 Oral] The official implementation of "Diffusion-Based Planning for Autonomous Driving with Flexible Guidance" |
| 10 | [ethz-adrl/towr](https://github.com/ethz-adrl/towr) | 导航/路径规划 | 1.1k+ / 250 | A light-weight, Eigen-based C++ library for trajectory optimization for legged robots. |
| 11 | [Zhefan-Xu/CERLAB-UAV-Autonomy](https://github.com/Zhefan-Xu/CERLAB-UAV-Autonomy) | 控制/最优控制 | 841 / 104 | [CMU] A Versatile and Modular Framework Designed for Autonomous Unmanned Aerial Vehicles [UAVs] (C++/ROS/PX4) |
| 12 | [ros2/examples](https://github.com/ros2/examples) | 机器人基础设施/接口 | 945 / 360 | Example packages for ROS 2 |
| 13 | [linorobot/linorobot2](https://github.com/linorobot/linorobot2) | 仿真/测试 | 924 / 232 | Autonomous mobile robots (2WD, 4WD, Mecanum Drive) |
| 14 | [huawei-noah/SMARTS](https://github.com/huawei-noah/SMARTS) | 定位建图/状态估计 | 1.1k+ / 220 | Scalable Multi-Agent RL Training School for Autonomous Driving |
| 15 | [linorobot/linorobot](https://github.com/linorobot/linorobot) | 机器人基础设施/接口 | 1.1k+ / 353 | Autonomous ground robots (2WD, 4WD, Ackermann Steering, Mecanum Drive) |
| 16 | [autowarefoundation/AWSIM](https://github.com/autowarefoundation/AWSIM) | 定位建图/状态估计 | 719 / 153 | Open sourced digital twin simulator for Autoware |
| 17 | [autonomousvision/navsim](https://github.com/autonomousvision/navsim) | 导航/路径规划 | 1.0k+ / 119 | [CoRL '25] Pseudo-Simulation for Autonomous Driving; [NeurIPS '24] NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking |
| 18 | [rsasaki0109/rust_robotics](https://github.com/rsasaki0109/rust_robotics) | 控制/最优控制 | 233 / 15 | 100+ robotics algorithms in Rust: planning, localization, SLAM, control, and benchmarks. |
| 19 | [snape/RVO2](https://github.com/snape/RVO2) | 导航/路径规划 | 950 / 281 | Optimal Reciprocal Collision Avoidance (C++) |
| 20 | [6-robot/wpr_simulation](https://github.com/6-robot/wpr_simulation) | 导航/路径规划 | 992 / 111 | GitHub repository |
| 21 | [eclipse-ecal/ecal](https://github.com/eclipse-ecal/ecal) | 机器人基础设施/接口 | 1.0k+ / 212 | 📦 eCAL - enhanced Communication Abstraction Layer. A high performance publish-subscribe, client-server cross-plattform middleware.  |
| 22 | [Timthony/self_drive](https://github.com/Timthony/self_drive) | 自动驾驶/移动机器人系统 | 1.1k+ / 278 | 基于树莓派的自动驾驶小车，利用树莓派和tensorflow实现小车在赛道的自动驾驶。（Self-driving car based on raspberry pi（tensorflow）） |
| 23 | [PRBonn/semantic_suma](https://github.com/PRBonn/semantic_suma) | 定位建图/状态估计 | 1.0k+ / 209 | SuMa++: Efficient LiDAR-based Semantic SLAM (Chen et al IROS 2019) |
| 24 | [louiszengCN/CarlaAir](https://github.com/louiszengCN/CarlaAir) | 定位建图/状态估计 | 1.0k+ / 84 | CarlaAir: Fly Drones Inside a CARLA World!! A Unified Infrastructure for Air-Ground Embodied Intelligence |
| 25 | [Shunichi09/PythonLinearNonlinearControl](https://github.com/Shunichi09/PythonLinearNonlinearControl) | 控制/最优控制 | 1.0k+ / 190 | PythonLinearNonLinearControl is a library implementing the linear and nonlinear control theories in python. |
| 26 | [teddyluo/hybrid-a-star-annotation](https://github.com/teddyluo/hybrid-a-star-annotation) | 导航/路径规划 | 882 / 251 | Hybrid A*路径规划器的代码注释 |
| 27 | [RoboSense-LiDAR/rslidar_sdk](https://github.com/RoboSense-LiDAR/rslidar_sdk) | 定位建图/状态估计 | 702 / 338 | RoboSense LiDAR SDK for ROS & ROS2 |
| 28 | [wh200720041/iscloam](https://github.com/wh200720041/iscloam) | 定位建图/状态估计 | 605 / 135 | Intensity Scan Context based full SLAM implementation for autonomous driving. ICRA 2020 |
| 29 | [YashBansod/Robotics-Planning-Dynamics-and-Control](https://github.com/YashBansod/Robotics-Planning-Dynamics-and-Control) | 控制/最优控制 | 443 / 87 | RPDC : This contains all my MATLAB codes for the Robotics, Planning, Dynamics and Control . The implementations model various kinds of manipulators and mobile robots for position control, trajectory planning and path planning problems. |
| 30 | [ros2/demos](https://github.com/ros2/demos) | 机器人基础设施/接口 | 640 / 359 | GitHub repository |
| 31 | [Sollimann/CleanIt](https://github.com/Sollimann/CleanIt) | 控制/最优控制 | 312 / 19 | Open-source Autonomy Software in Rust-lang using gRPC for the Roomba series robot vacuum cleaners. Under development. |
| 32 | [MizuhoAOKI/python_simple_mppi](https://github.com/MizuhoAOKI/python_simple_mppi) | 控制/最优控制 | 711 / 69 | Python implementation of MPPI (Model Predictive Path-Integral) controller to understand the basic idea. Mandatory dependencies are numpy and matplotlib only. |
| 33 | [koide3/ndt_omp](https://github.com/koide3/ndt_omp) | 机器人基础设施/接口 | 847 / 374 | Multi-threaded and SSE friendly NDT algorithm |

## 后续拆解建议

- 优先拆直接规划控制仓库：MPC、MPPI、Hybrid A*、Frenet、RVO、多机器人路径规划、覆盖路径和三维轨迹规划相关项目。
- 第二优先级拆工程落地依赖：ROS2、MAVLink、仿真器、传感器驱动、NDT/ICP/SLAM/标定工具。
- 对星数高但方向偏感知或平台的项目，只作为系统边界和接口参考，不默认纳入控制算法候选。

## 更新记录

- 2026-06-25：整理第 7 批未入库 GitHub 资源，并建立 33 篇单源笔记。
