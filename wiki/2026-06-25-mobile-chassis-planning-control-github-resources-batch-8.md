---
id: "20260625-080000-mobile-chassis-planning-control-github-resources-batch-8"
title: "移动底盘规划控制 GitHub 资源精选（八）"
type: "topic"
source: ""
created_at: "2026-06-25"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-25-liuguitao-avp-slam-plus-planning-control-git-resource.md
  - notes/2026-06-25-ai-winter-matlab-motion-planning-planning-control-git-resource.md
  - notes/2026-06-25-w111liang222-lidar-slam-detection-planning-control-git-resource.md
  - notes/2026-06-25-openquadruped-spot-mini-mini-planning-control-git-resource.md
  - notes/2026-06-25-carlosmccosta-dynamic-robot-localization-planning-control-git-resource.md
  - notes/2026-06-25-leggedrobotics-se2-navigation-planning-control-git-resource.md
  - notes/2026-06-25-stevemacenski-spatio-temporal-voxel-layer-planning-control-git-resource.md
  - notes/2026-06-25-mit-acl-mader-planning-control-git-resource.md
  - notes/2026-06-25-thenoobinventor-lidarbot-planning-control-git-resource.md
  - notes/2026-06-25-aurora-opensource-xviz-planning-control-git-resource.md
  - notes/2026-06-25-sollimann-dstar-lite-pathplanner-planning-control-git-resource.md
  - notes/2026-06-25-copterexpress-clover-planning-control-git-resource.md
  - notes/2026-06-25-nicklashansen-tdmpc2-planning-control-git-resource.md
  - notes/2026-06-25-autorally-autorally-planning-control-git-resource.md
  - notes/2026-06-25-ss47816-fiss-planner-planning-control-git-resource.md
  - notes/2026-06-25-motion-planning-rrt-algorithms-planning-control-git-resource.md
  - notes/2026-06-25-ethz-asl-polygon-coverage-planning-planning-control-git-resource.md
  - notes/2026-06-25-deepdrive-deepdrive-planning-control-git-resource.md
  - notes/2026-06-25-learnsyslab-safe-control-gym-planning-control-git-resource.md
  - notes/2026-06-25-hanruihua-rda-planner-planning-control-git-resource.md
  - notes/2026-06-25-silvery107-rl-mpc-locomotion-planning-control-git-resource.md
  - notes/2026-06-25-mrpt-ros-pkg-mrpt-navigation-planning-control-git-resource.md
  - notes/2026-06-25-zhefan-xu-intent-mpc-planning-control-git-resource.md
  - notes/2026-06-25-internrobotics-internnav-planning-control-git-resource.md
  - notes/2026-06-25-ss47816-frenet-optimal-planner-planning-control-git-resource.md
  - notes/2026-06-25-sigmaai-self-driving-golf-cart-planning-control-git-resource.md
  - notes/2026-06-25-lijiangnanbit-path-optimizer-planning-control-git-resource.md
  - notes/2026-06-25-snape-rvo2-cs-planning-control-git-resource.md
  - notes/2026-06-25-nicrusso7-rex-gym-planning-control-git-resource.md
  - notes/2026-06-25-jaeyoung-lim-mavros-controllers-planning-control-git-resource.md
  - notes/2026-06-25-zhaohaojie1998-grey-wolf-optimizer-for-path-planning-planning-control-git-resource.md
  - notes/2026-06-25-autonomousvision-tuplan-garage-planning-control-git-resource.md
  - notes/2026-06-25-luigifreda-3dmr-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（八）

## 当前判断

本页是第 8 批当前知识库未记录过的 GitHub 资源。筛选优先级是：与移动底盘规划控制直接相关，其次是规划控制落地必须依赖的定位建图、传感器接口、仿真验证、ROS/机器人基础设施和无人系统接口。

## 取舍边界

- 已排除当前知识库中已经出现过的 GitHub 仓库 URL。
- star/fork 是筛选信号，不是质量结论；真正使用前仍要检查许可证、维护状态、接口假设和源码实现。
- 本批保留部分非 planner/controller 仓库，因为底盘规划控制系统需要可靠的定位、建图、仿真、消息通信和硬件接口。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [liuguitao/AVP-SLAM-PLUS](https://github.com/liuguitao/AVP-SLAM-PLUS) | 定位建图/状态估计 | 674 / 201 | An implementation of AVP-SLAM and some new contributions |
| 2 | [ai-winter/matlab_motion_planning](https://github.com/ai-winter/matlab_motion_planning) | 控制/最优控制 | 641 / 91 | Motion planning and Navigation of AGV/AMR：matlab implementation of Dijkstra, A*, Theta*, JPS, D*, LPA*, D* Lite, RRT, RRT*, RRT-Connect, Informed RRT*, ACO, Voronoi, PID, LQR, MPC, APF, RPP, DWA, DDPG, Bezier, B-spline, Dubins, Reeds-Shepp etc. |
| 3 | [w111liang222/lidar-slam-detection](https://github.com/w111liang222/lidar-slam-detection) | 定位建图/状态估计 | 754 / 155 | LSD (LiDAR SLAM & Detection) is an open source perception architecture for autonomous vehicle/robotic |
| 4 | [OpenQuadruped/spot_mini_mini](https://github.com/OpenQuadruped/spot_mini_mini) | 控制/最优控制 | 927 / 192 | Dynamics and Domain Randomized Gait Modulation with Bezier Curves for Sim-to-Real Legged Locomotion. |
| 5 | [carlosmccosta/dynamic_robot_localization](https://github.com/carlosmccosta/dynamic_robot_localization) | 定位建图/状态估计 | 897 / 202 | Point cloud registration pipeline for robot localization and 3D perception |
| 6 | [leggedrobotics/se2_navigation](https://github.com/leggedrobotics/se2_navigation) | 控制/最优控制 | 597 / 99 | Pure Pursuit Control and SE(2) Planning |
| 7 | [SteveMacenski/spatio_temporal_voxel_layer](https://github.com/SteveMacenski/spatio_temporal_voxel_layer) | 导航/路径规划 | 840 / 226 | A new voxel layer leveraging modern 3D graphics tools to modernize navigation environmental representations |
| 8 | [mit-acl/mader](https://github.com/mit-acl/mader) | 导航/路径规划 | 608 / 92 | Trajectory Planner in Multi-Agent and Dynamic Environments |
| 9 | [TheNoobInventor/lidarbot](https://github.com/TheNoobInventor/lidarbot) | 控制/最优控制 | 212 / 38 | A differential drive robot is controlled using ROS2 Humble running on a Raspberry Pi 4 (running Ubuntu server 22.04). The vehicle is equipped with a raspberry pi camera for visual feedback and an RPlidar A1 sensor used for Simultaneous Localization and Mapping (SLAM), autonomous navigation and obstacle avoidance. |
| 10 | [aurora-opensource/xviz](https://github.com/aurora-opensource/xviz) | 自动驾驶/移动机器人系统 | 1.1k+ / 233 | A protocol for real-time transfer and visualization of autonomy data |
| 11 | [Sollimann/Dstar-lite-pathplanner](https://github.com/Sollimann/Dstar-lite-pathplanner) | 导航/路径规划 | 197 / 38 | Implementation of the D* lite algorithm in Python for "Improved Fast Replanning for Robot Navigation in Unknown Terrain" |
| 12 | [CopterExpress/clover](https://github.com/CopterExpress/clover) | 控制/最优控制 | 644 / 314 | ROS-based framework and RPi image to control PX4-powered drones 🍀 |
| 13 | [nicklashansen/tdmpc2](https://github.com/nicklashansen/tdmpc2) | 控制/最优控制 | 869 / 197 | Code for "TD-MPC2: Scalable, Robust World Models for Continuous Control" |
| 14 | [AutoRally/autorally](https://github.com/AutoRally/autorally) | 机器人基础设施/接口 | 786 / 235 | Software for the AutoRally platform |
| 15 | [SS47816/fiss_planner](https://github.com/SS47816/fiss_planner) | 导航/路径规划 | 178 / 36 | [RA-L 2022] FISS: A Trajectory Planning Framework using Fast Iterative Search and Sampling Strategy for Autonomous Driving |
| 16 | [motion-planning/rrt-algorithms](https://github.com/motion-planning/rrt-algorithms) | 导航/路径规划 | 831 / 206 | n-dimensional RRT, RRT* (RRT-Star) |
| 17 | [ethz-asl/polygon_coverage_planning](https://github.com/ethz-asl/polygon_coverage_planning) | 导航/路径规划 | 649 / 167 | Coverage planning in general polygons with holes. |
| 18 | [deepdrive/deepdrive](https://github.com/deepdrive/deepdrive) | 控制/最优控制 | 924 / 150 | Deepdrive is a simulator that allows anyone with a PC to push the state-of-the-art in self-driving |
| 19 | [learnsyslab/safe-control-gym](https://github.com/learnsyslab/safe-control-gym) | 控制/最优控制 | 893 / 162 | PyBullet CartPole and Quadrotor environments—with CasADi symbolic a priori dynamics—for learning-based control and RL |
| 20 | [hanruihua/RDA-planner](https://github.com/hanruihua/RDA-planner) | 控制/最优控制 | 345 / 52 | [RA-Letter 2023] RDA: An Accelerated Collision Free Motion Planner for Autonomous Navigation in Cluttered Environments |
| 21 | [silvery107/rl-mpc-locomotion](https://github.com/silvery107/rl-mpc-locomotion) | 控制/最优控制 | 995 / 92 | Deep RL for MPC control of Quadruped Robot Locomotion |
| 22 | [mrpt-ros-pkg/mrpt_navigation](https://github.com/mrpt-ros-pkg/mrpt_navigation) | 导航/路径规划 | 215 / 102 | ROS 2 nodes wrapping core MRPT functionality: localization, autonomous navigation, rawlogs, etc. SLAM is in other packages. |
| 23 | [Zhefan-Xu/Intent-MPC](https://github.com/Zhefan-Xu/Intent-MPC) | 控制/最优控制 | 356 / 29 | [IEEE RA-L'25] Intent Prediction-Driven Model Predictive Control for UAV Planning and Navigation in Dynamic Environments (C++/ROS)  |
| 24 | [InternRobotics/InternNav](https://github.com/InternRobotics/InternNav) | 导航/路径规划 | 915 / 123 | InternRobotics' open platform for building generalized navigation foundation models. |
| 25 | [SS47816/frenet_optimal_planner](https://github.com/SS47816/frenet_optimal_planner) | 导航/路径规划 | 97 / 28 | Implementation of the Frenet Optimal Planning Algorithm (with modifications) in ROS. |
| 26 | [sigmaai/self-driving-golf-cart](https://github.com/sigmaai/self-driving-golf-cart) | 控制/最优控制 | 264 / 69 | Be Driven 🚘 |
| 27 | [LiJiangnanBit/path_optimizer](https://github.com/LiJiangnanBit/path_optimizer) | 导航/路径规划 | 592 / 150 | Optimization-based real-time path planning for vehicles.  |
| 28 | [snape/RVO2-CS](https://github.com/snape/RVO2-CS) | 导航/路径规划 | 846 / 141 | Optimal Reciprocal Collision Avoidance (C#) |
| 29 | [nicrusso7/rex-gym](https://github.com/nicrusso7/rex-gym) | 腿式/足式移动底盘 | 1.1k+ / 140 | OpenAI Gym environments for an open-source quadruped robot (SpotMicro) |
| 30 | [Jaeyoung-Lim/mavros_controllers](https://github.com/Jaeyoung-Lim/mavros_controllers) | 控制/最优控制 | 505 / 181 | Aggressive trajectory tracking using mavros for PX4 enabled vehicles |
| 31 | [zhaohaojie1998/Grey-Wolf-Optimizer-for-Path-Planning](https://github.com/zhaohaojie1998/Grey-Wolf-Optimizer-for-Path-Planning) | 导航/路径规划 | 745 / 59 | 灰狼优化算法(GWO)路径规划/轨迹规划/轨迹优化、多智能体/多无人机航迹规划 |
| 32 | [autonomousvision/tuplan_garage](https://github.com/autonomousvision/tuplan_garage) | 导航/路径规划 | 703 / 76 | [CoRL'23] Parting with Misconceptions about Learning-based Vehicle Motion Planning |
| 33 | [luigifreda/3dmr](https://github.com/luigifreda/3dmr) | 控制/最优控制 | 280 / 31 | 3D Multi-Robot Exploration, Patrolling and Navigation. |

## 后续拆解建议

- 优先拆直接规划控制仓库：MPC、MPPI、Hybrid A*、Frenet、RVO、多机器人路径规划、覆盖路径和三维轨迹规划相关项目。
- 第二优先级拆工程落地依赖：ROS2、MAVLink、仿真器、传感器驱动、NDT/ICP/SLAM/标定工具。
- 对星数高但方向偏感知或平台的项目，只作为系统边界和接口参考，不默认纳入控制算法候选。

## 更新记录

- 2026-06-25：整理第 8 批未入库 GitHub 资源，并建立 33 篇单源笔记。
