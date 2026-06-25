---
id: "20260625-060000-mobile-chassis-planning-control-github-resources-batch-6"
title: "移动底盘规划控制 GitHub 资源精选（六）"
type: "topic"
source: ""
created_at: "2026-06-25"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-25-ros2-ros2-planning-control-git-resource.md
  - notes/2026-06-25-realsenseai-realsense-ros-planning-control-git-resource.md
  - notes/2026-06-25-autorope-donkeycar-planning-control-git-resource.md
  - notes/2026-06-25-petoicamp-opencat-quadruped-robot-planning-control-git-resource.md
  - notes/2026-06-25-petercorke-robotics-toolbox-python-planning-control-git-resource.md
  - notes/2026-06-25-ob-f-openbot-planning-control-git-resource.md
  - notes/2026-06-25-pjlab-adg-sensorscalibration-planning-control-git-resource.md
  - notes/2026-06-25-autowarefoundation-autoware-universe-planning-control-git-resource.md
  - notes/2026-06-25-unity-technologies-unity-robotics-hub-planning-control-git-resource.md
  - notes/2026-06-25-nate711-stanforddoggoproject-planning-control-git-resource.md
  - notes/2026-06-25-hku-mars-r3live-planning-control-git-resource.md
  - notes/2026-06-25-generalized-intelligence-gaas-planning-control-git-resource.md
  - notes/2026-06-25-learnsyslab-gym-pybullet-drones-planning-control-git-resource.md
  - notes/2026-06-25-mit-spark-teaser-plusplus-planning-control-git-resource.md
  - notes/2026-06-25-petercorke-robotics-toolbox-matlab-planning-control-git-resource.md
  - notes/2026-06-25-chvmp-champ-planning-control-git-resource.md
  - notes/2026-06-25-norlab-ulaval-libpointmatcher-planning-control-git-resource.md
  - notes/2026-06-25-mit-spark-kimera-planning-control-git-resource.md
  - notes/2026-06-25-dji-sdk-onboard-sdk-planning-control-git-resource.md
  - notes/2026-06-25-introlab-rtabmap-ros-planning-control-git-resource.md
  - notes/2026-06-25-mit-acl-faster-planning-control-git-resource.md
  - notes/2026-06-25-geonhee-lee-mpc-ros-planning-control-git-resource.md
  - notes/2026-06-25-pypose-pypose-planning-control-git-resource.md
  - notes/2026-06-25-nvlabs-curobo-planning-control-git-resource.md
  - notes/2026-06-25-stereolabs-zed-sdk-planning-control-git-resource.md
  - notes/2026-06-25-google-deepmind-mujoco-mpc-planning-control-git-resource.md
  - notes/2026-06-25-symforce-org-symforce-planning-control-git-resource.md
  - notes/2026-06-25-hku-mars-lidar-imu-init-planning-control-git-resource.md
  - notes/2026-06-25-atsushisakai-matlabrobotics-planning-control-git-resource.md
  - notes/2026-06-25-atb033-multi-agent-path-planning-planning-control-git-resource.md
  - notes/2026-06-25-reiniscimurs-drl-robot-navigation-planning-control-git-resource.md
  - notes/2026-06-25-slamtec-rplidar-ros-planning-control-git-resource.md
  - notes/2026-06-25-roboticslibrary-rl-planning-control-git-resource.md
  - notes/2026-06-25-ardupilot-pymavlink-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（六）

## 当前判断

本页是第 6 批当前知识库未记录过的 GitHub 资源。筛选优先级是：与移动底盘规划控制直接相关，其次是规划控制落地必须依赖的定位建图、传感器接口、仿真验证、ROS/机器人基础设施和无人系统接口。

## 取舍边界

- 已排除当前知识库中已经出现过的 GitHub 仓库 URL。
- star/fork 是筛选信号，不是质量结论；真正使用前仍要检查许可证、维护状态、接口假设和源码实现。
- 本批保留部分非 planner/controller 仓库，因为底盘规划控制系统需要可靠的定位、建图、仿真、消息通信和硬件接口。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [ros2/ros2](https://github.com/ros2/ros2) | 机器人基础设施/接口 | 5.7k+ / 919 | The Robot Operating System, is a meta operating system for robots. |
| 2 | [realsenseai/realsense-ros](https://github.com/realsenseai/realsense-ros) | 机器人基础设施/接口 | 3.4k+ / 2.0k+ | ROS Wrapper for RealSense™ Cameras |
| 3 | [autorope/donkeycar](https://github.com/autorope/donkeycar) | 自动驾驶/移动机器人系统 | 3.5k+ / 1.4k+ | Open source hardware and software platform to build a small scale self driving car. |
| 4 | [PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | 定位建图/状态估计 | 4.9k+ / 571 | An open source quadruped robot pet framework for developing Boston Dynamics-style four-legged robots that are perfect for STEM, coding & robotics education, IoT robotics applications, AI-enhanced robotics application services, research, and DIY robotics kit development.  |
| 5 | [petercorke/robotics-toolbox-python](https://github.com/petercorke/robotics-toolbox-python) | 控制/最优控制 | 3.1k+ / 580 | Robotics Toolbox for Python |
| 6 | [ob-f/OpenBot](https://github.com/ob-f/OpenBot) | 导航/路径规划 | 3.3k+ / 632 | OpenBot leverages smartphones as brains for low-cost robots. We have designed a small electric vehicle that costs about $50 and serves as a robot body. Our software stack for Android smartphones supports advanced robotics workloads such as person following and real-time autonomous navigation. |
| 7 | [PJLab-ADG/SensorsCalibration](https://github.com/PJLab-ADG/SensorsCalibration) | 定位建图/状态估计 | 3.1k+ / 697 | OpenCalib: A Multi-sensor Calibration Toolbox for Autonomous Driving |
| 8 | [autowarefoundation/autoware_universe](https://github.com/autowarefoundation/autoware_universe) | 导航/路径规划 | 1.7k+ / 918 | GitHub repository |
| 9 | [Unity-Technologies/Unity-Robotics-Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub) | 控制/最优控制 | 2.5k+ / 467 | Central repository for tools, tutorials, resources, and documentation for robotics simulation in Unity. |
| 10 | [Nate711/StanfordDoggoProject](https://github.com/Nate711/StanfordDoggoProject) | 腿式/足式移动底盘 | 2.5k+ / 748 | Stanford Doggo is an open source quadruped robot that jumps, flips, and trots! |
| 11 | [hku-mars/r3live](https://github.com/hku-mars/r3live) | 定位建图/状态估计 | 2.4k+ / 482 | A Robust, Real-time, RGB-colored, LiDAR-Inertial-Visual tightly-coupled state Estimation and mapping package |
| 12 | [generalized-intelligence/GAAS](https://github.com/generalized-intelligence/GAAS) | 控制/最优控制 | 2.1k+ / 464 | GAAS is an open-source program designed for fully autonomous VTOL(a.k.a flying cars) and drones. GAAS stands for Generalized Autonomy Aviation System.  |
| 13 | [learnsyslab/gym-pybullet-drones](https://github.com/learnsyslab/gym-pybullet-drones) | 控制/最优控制 | 2.1k+ / 542 | PyBullet Gymnasium environments for single and multi-agent reinforcement learning of quadcopter control |
| 14 | [MIT-SPARK/TEASER-plusplus](https://github.com/MIT-SPARK/TEASER-plusplus) | 定位建图/状态估计 | 2.3k+ / 412 | A fast and robust point cloud registration library |
| 15 | [petercorke/robotics-toolbox-matlab](https://github.com/petercorke/robotics-toolbox-matlab) | 导航/路径规划 | 1.5k+ / 463 | Robotics Toolbox for MATLAB |
| 16 | [chvmp/champ](https://github.com/chvmp/champ) | 定位建图/状态估计 | 2.3k+ / 436 | MIT Cheetah I Implementation |
| 17 | [norlab-ulaval/libpointmatcher](https://github.com/norlab-ulaval/libpointmatcher) | 定位建图/状态估计 | 1.8k+ / 566 | An Iterative Closest Point (ICP) library for 2D and 3D mapping in Robotics |
| 18 | [MIT-SPARK/Kimera](https://github.com/MIT-SPARK/Kimera) | 定位建图/状态估计 | 2.1k+ / 241 | Index repo for Kimera code |
| 19 | [dji-sdk/Onboard-SDK](https://github.com/dji-sdk/Onboard-SDK) | 控制/最优控制 | 983 / 648 | DJI Onboard SDK Official Repository |
| 20 | [introlab/rtabmap_ros](https://github.com/introlab/rtabmap_ros) | 机器人基础设施/接口 | 1.5k+ / 652 | RTAB-Map's ROS package. |
| 21 | [mit-acl/faster](https://github.com/mit-acl/faster) | 导航/路径规划 | 1.2k+ / 200 | 3D Trajectory Planner in Unknown Environments |
| 22 | [Geonhee-LEE/mpc_ros](https://github.com/Geonhee-LEE/mpc_ros) | 控制/最优控制 | 965 / 187 | Differential Wheeled Mobile Robot - Nonlinear Model Predictive Control based on ROS |
| 23 | [pypose/pypose](https://github.com/pypose/pypose) | 控制/最优控制 | 1.6k+ / 127 | A library for differentiable robotics on manifolds. |
| 24 | [NVlabs/curobo](https://github.com/NVlabs/curobo) | 导航/路径规划 | 1.7k+ / 298 | CUDA Accelerated Robot Library |
| 25 | [stereolabs/zed-sdk](https://github.com/stereolabs/zed-sdk) | 定位建图/状态估计 | 1.2k+ / 507 | ⚡️The spatial perception framework for rapidly building smart robots and spaces |
| 26 | [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc) | 控制/最优控制 | 1.7k+ / 268 | Real-time behaviour synthesis with MuJoCo, using Predictive Control |
| 27 | [symforce-org/symforce](https://github.com/symforce-org/symforce) | 导航/路径规划 | 1.6k+ / 169 | Fast symbolic computation, code generation, and nonlinear optimization for robotics |
| 28 | [hku-mars/LiDAR_IMU_Init](https://github.com/hku-mars/LiDAR_IMU_Init) | 定位建图/状态估计 | 1.4k+ / 240 | [IROS2022] Robust Real-time LiDAR-inertial Initialization Method. |
| 29 | [AtsushiSakai/MATLABRobotics](https://github.com/AtsushiSakai/MATLABRobotics) | 导航/路径规划 | 678 / 326 | MATLAB sample codes for mobile robot navigation |
| 30 | [atb033/multi_agent_path_planning](https://github.com/atb033/multi_agent_path_planning) | 导航/路径规划 | 1.5k+ / 305 | Python implementation of a bunch of multi-robot path-planning algorithms. |
| 31 | [reiniscimurs/DRL-robot-navigation](https://github.com/reiniscimurs/DRL-robot-navigation) | 导航/路径规划 | 1.3k+ / 194 | Deep Reinforcement Learning for mobile robot navigation in ROS Gazebo simulator. Using Twin Delayed Deep Deterministic Policy Gradient (TD3) neural network, a robot learns to navigate to a random goal point in a simulated environment while avoiding obstacles. |
| 32 | [Slamtec/rplidar_ros](https://github.com/Slamtec/rplidar_ros) | 定位建图/状态估计 | 673 / 635 | GitHub repository |
| 33 | [roboticslibrary/rl](https://github.com/roboticslibrary/rl) | 控制/最优控制 | 1.2k+ / 242 | The Robotics Library (RL) is a self-contained C++ library for rigid body kinematics and dynamics, motion planning, and control. |
| 34 | [ArduPilot/pymavlink](https://github.com/ArduPilot/pymavlink) | 机器人基础设施/接口 | 708 / 727 | python MAVLink interface and utilities |

## 后续拆解建议

- 优先拆直接规划控制仓库：MPC、MPPI、Hybrid A*、Frenet、RVO、多机器人路径规划、覆盖路径和三维轨迹规划相关项目。
- 第二优先级拆工程落地依赖：ROS2、MAVLink、仿真器、传感器驱动、NDT/ICP/SLAM/标定工具。
- 对星数高但方向偏感知或平台的项目，只作为系统边界和接口参考，不默认纳入控制算法候选。

## 更新记录

- 2026-06-25：整理第 6 批未入库 GitHub 资源，并建立 34 篇单源笔记。
