---
id: "20260624-280000-mobile-chassis-planning-control-github-resources-batch-5"
title: "移动底盘规划控制 GitHub 资源精选（五）"
type: "topic"
source: ""
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - tools
related:
  - notes/2026-06-24-behaviortree-cpp-planning-control-git-resource.md
  - notes/2026-06-24-moveit-planning-control-git-resource.md
  - notes/2026-06-24-geometric-shapes-planning-control-git-resource.md
  - notes/2026-06-24-moveit-resources-planning-control-git-resource.md
  - notes/2026-06-24-moveit-visual-tools-planning-control-git-resource.md
  - notes/2026-06-24-moveit-tutorials-planning-control-git-resource.md
  - notes/2026-06-24-perception-pcl-planning-control-git-resource.md
  - notes/2026-06-24-vision-opencv-planning-control-git-resource.md
  - notes/2026-06-24-image-pipeline-planning-control-git-resource.md
  - notes/2026-06-24-laser-geometry-planning-control-git-resource.md
  - notes/2026-06-24-pointcloud-to-laserscan-planning-control-git-resource.md
  - notes/2026-06-24-depthimage-to-laserscan-planning-control-git-resource.md
  - notes/2026-06-24-angles-planning-control-git-resource.md
  - notes/2026-06-24-urdfdom-planning-control-git-resource.md
  - notes/2026-06-24-xacro-planning-control-git-resource.md
  - notes/2026-06-24-ros2-launch-planning-control-git-resource.md
  - notes/2026-06-24-ros2-message-filters-planning-control-git-resource.md
  - notes/2026-06-24-lego-loam-planning-control-git-resource.md
  - notes/2026-06-24-a-loam-planning-control-git-resource.md
  - notes/2026-06-24-loam-velodyne-planning-control-git-resource.md
  - notes/2026-06-24-ikd-tree-planning-control-git-resource.md
  - notes/2026-06-24-fast-livo-planning-control-git-resource.md
  - notes/2026-06-24-fast-livo2-planning-control-git-resource.md
  - notes/2026-06-24-ikfom-planning-control-git-resource.md
  - notes/2026-06-24-open-vins-planning-control-git-resource.md
  - notes/2026-06-24-rovio-planning-control-git-resource.md
  - notes/2026-06-24-okvis-planning-control-git-resource.md
  - notes/2026-06-24-maplab-planning-control-git-resource.md
  - notes/2026-06-24-kalibr-planning-control-git-resource.md
  - notes/2026-06-24-rpg-svo-pro-open-planning-control-git-resource.md
  - notes/2026-06-24-hdl-graph-slam-planning-control-git-resource.md
  - notes/2026-06-24-hdl-localization-planning-control-git-resource.md
  - notes/2026-06-24-fast-gicp-planning-control-git-resource.md
  - notes/2026-06-24-kiss-icp-planning-control-git-resource.md
  - notes/2026-06-24-kimera-rpgo-planning-control-git-resource.md
  - notes/2026-06-24-spark-dsg-planning-control-git-resource.md
  - notes/2026-06-24-nebula-planning-control-git-resource.md
  - notes/2026-06-24-autoware-adapi-msgs-planning-control-git-resource.md
  - notes/2026-06-24-rmw-fastrtps-planning-control-git-resource.md
  - notes/2026-06-24-rmw-cyclonedds-planning-control-git-resource.md
---

# 移动底盘规划控制 GitHub 资源精选（五）

## 当前判断

本页是第五批 40 个当前知识库未记录过的 GitHub 资源。相比前四批，本批重点补齐行为树任务编排、MoveIt/规划几何与教程资源、ROS 感知输入转换、机器人模型基础、ROS2 启动与消息同步、LOAM/VIO/LIO/标定、Autoware 接口消息和 ROS2 RMW 通信后端。

## 取舍边界

- 本批继续排除已入库 Git URL，包括前四批 160 个资源和历史已有 Apollo、Autoware、Nav2、PX4、openpilot、CARLA、TurtleBot、F1TENTH、RMF、MAVLink、CommonRoad、Gazebo、Foxglove、VINS、FAST-LIO、ORB-SLAM3 等条目。
- 不是所有仓库都是 planner/controller：移动底盘规划控制还依赖任务树、几何模型、传感器预处理、标定、定位建图、消息同步、启动编排和 DDS 通信。
- star/fork 是筛选信号，不是质量结论；后续真正使用前要看代码、许可证、维护状态和接口假设。

## 资源清单

| # | 仓库 | 方向 | Stars / Forks | 主要价值 |
|---:|---|---|---:|---|
| 1 | [BehaviorTree/BehaviorTree.CPP](https://github.com/BehaviorTree/BehaviorTree.CPP) | 行为树/任务编排 | 5k+ / 1k+ | C++ behavior tree library used by robotics systems including Nav2-style task orchestration. |
| 2 | [moveit/moveit](https://github.com/moveit/moveit) | ROS1 运动规划框架 | 3k+ / 2k+ | ROS motion planning framework for manipulation, collision checking, planning scenes and execution. |
| 3 | [ros-planning/geometric_shapes](https://github.com/ros-planning/geometric_shapes) | 几何形状/碰撞模型 | 100+ / 100+ | Shape representation and conversion utilities used in ROS planning stacks. |
| 4 | [ros-planning/moveit_resources](https://github.com/ros-planning/moveit_resources) | MoveIt 示例模型资源 | 100+ / 200+ | Robot models and configuration resources used by MoveIt tests and tutorials. |
| 5 | [ros-planning/moveit_visual_tools](https://github.com/ros-planning/moveit_visual_tools) | 规划可视化工具 | 500+ / 300+ | Visualization helpers for MoveIt planning and robot motion debugging. |
| 6 | [ros-planning/moveit_tutorials](https://github.com/ros-planning/moveit_tutorials) | MoveIt 教程 | 600+ / 500+ | Tutorial code and documentation for MoveIt usage and extension. |
| 7 | [ros-perception/perception_pcl](https://github.com/ros-perception/perception_pcl) | ROS 点云处理 | 500+ / 500+ | ROS integration packages for Point Cloud Library. |
| 8 | [ros-perception/vision_opencv](https://github.com/ros-perception/vision_opencv) | ROS OpenCV 桥接 | 1k+ / 800+ | ROS packages for OpenCV image transport and cv_bridge integration. |
| 9 | [ros-perception/image_pipeline](https://github.com/ros-perception/image_pipeline) | ROS 图像处理流水线 | 500+ / 500+ | ROS camera calibration, rectification and stereo image processing pipeline. |
| 10 | [ros-perception/laser_geometry](https://github.com/ros-perception/laser_geometry) | LaserScan 点云转换 | 100+ / 150+ | Projection utilities converting LaserScan messages into point clouds. |
| 11 | [ros-perception/pointcloud_to_laserscan](https://github.com/ros-perception/pointcloud_to_laserscan) | 点云转 LaserScan | 300+ / 250+ | ROS package converting PointCloud2 data into LaserScan data. |
| 12 | [ros-perception/depthimage_to_laserscan](https://github.com/ros-perception/depthimage_to_laserscan) | 深度图转 LaserScan | 200+ / 200+ | ROS package converting depth images into LaserScan messages. |
| 13 | [ros/angles](https://github.com/ros/angles) | 角度数学工具 | 200+ / 200+ | Small ROS package for angle wrapping and angular distance utilities. |
| 14 | [ros/urdfdom](https://github.com/ros/urdfdom) | URDF 模型解析 | 500+ / 300+ | URDF parser and DOM library for robot model descriptions. |
| 15 | [ros/xacro](https://github.com/ros/xacro) | URDF 宏工具 | 400+ / 300+ | XML macro language used to generate robot URDF descriptions. |
| 16 | [ros2/launch](https://github.com/ros2/launch) | ROS2 启动编排 | 300+ / 300+ | Launch system for ROS 2 nodes, processes and runtime configurations. |
| 17 | [ros2/message_filters](https://github.com/ros2/message_filters) | ROS2 消息同步 | 100+ / 100+ | ROS 2 message synchronization and filtering utilities. |
| 18 | [RobustFieldAutonomyLab/LeGO-LOAM](https://github.com/RobustFieldAutonomyLab/LeGO-LOAM) | 轻量级激光 SLAM | 2k+ / 1k+ | Lightweight and ground-optimized lidar odometry and mapping system. |
| 19 | [HKUST-Aerial-Robotics/A-LOAM](https://github.com/HKUST-Aerial-Robotics/A-LOAM) | LOAM 实现 | 3k+ / 1k+ | Advanced implementation of LOAM using Ceres and ROS. |
| 20 | [laboshinl/loam_velodyne](https://github.com/laboshinl/loam_velodyne) | LOAM 原始 ROS 实现 | 2k+ / 1k+ | ROS implementation of LOAM for Velodyne lidar. |
| 21 | [hku-mars/ikd-Tree](https://github.com/hku-mars/ikd-Tree) | 增量 KD-Tree | 1k+ / 300+ | Incremental k-d tree for robotic applications and LiDAR-inertial odometry. |
| 22 | [hku-mars/FAST-LIVO](https://github.com/hku-mars/FAST-LIVO) | 激光惯性视觉里程计 | 1k+ / 300+ | Fast and tightly-coupled LiDAR-inertial-visual odometry. |
| 23 | [hku-mars/FAST-LIVO2](https://github.com/hku-mars/FAST-LIVO2) | 激光惯性视觉里程计 | 1k+ / 200+ | Fast, direct LiDAR-inertial-visual odometry system. |
| 24 | [hku-mars/IKFoM](https://github.com/hku-mars/IKFoM) | 迭代卡尔曼滤波工具 | 900+ / 300+ | Toolkit for iterated Kalman filter on manifolds. |
| 25 | [rpng/open_vins](https://github.com/rpng/open_vins) | 视觉惯性状态估计 | 1k+ / 500+ | Research platform for visual-inertial estimation. |
| 26 | [ethz-asl/rovio](https://github.com/ethz-asl/rovio) | 鲁棒视觉惯性里程计 | 1k+ / 500+ | Robust visual inertial odometry framework. |
| 27 | [ethz-asl/okvis](https://github.com/ethz-asl/okvis) | 关键帧视觉惯性 SLAM | 1k+ / 500+ | Open Keyframe-based Visual-Inertial SLAM. |
| 28 | [ethz-asl/maplab](https://github.com/ethz-asl/maplab) | 多会话视觉惯性建图 | 2k+ / 700+ | Research-oriented visual-inertial mapping framework. |
| 29 | [ethz-asl/kalibr](https://github.com/ethz-asl/kalibr) | 相机/IMU 标定 | 2k+ / 1k+ | Calibration toolbox for camera, IMU and multi-sensor systems. |
| 30 | [uzh-rpg/rpg_svo_pro_open](https://github.com/uzh-rpg/rpg_svo_pro_open) | 直接法视觉里程计 | 1k+ / 300+ | Open source release of SVO Pro visual odometry. |
| 31 | [koide3/hdl_graph_slam](https://github.com/koide3/hdl_graph_slam) | 3D 激光图优化 SLAM | 1k+ / 500+ | 3D lidar graph SLAM package for ROS. |
| 32 | [koide3/hdl_localization](https://github.com/koide3/hdl_localization) | 3D 激光定位 | 600+ / 300+ | 3D lidar localization package using NDT matching. |
| 33 | [SMRT-AIST/fast_gicp](https://github.com/SMRT-AIST/fast_gicp) | 点云配准 | 1k+ / 300+ | Fast GICP point cloud registration implementations. |
| 34 | [PRBonn/kiss-icp](https://github.com/PRBonn/kiss-icp) | 激光里程计 | 1k+ / 300+ | Simple, robust and accurate LiDAR odometry pipeline. |
| 35 | [MIT-SPARK/Kimera-RPGO](https://github.com/MIT-SPARK/Kimera-RPGO) | 鲁棒位姿图优化 | 300+ / 100+ | Robust pose graph optimization library. |
| 36 | [MIT-SPARK/Spark-DSG](https://github.com/MIT-SPARK/Spark-DSG) | 动态场景图 | 500+ / 100+ | Dynamic scene graph representation and tooling. |
| 37 | [tier4/nebula](https://github.com/tier4/nebula) | Autoware 激光雷达驱动 | 200+ / 150+ | LiDAR driver framework used in Autoware ecosystem. |
| 38 | [autowarefoundation/autoware_adapi_msgs](https://github.com/autowarefoundation/autoware_adapi_msgs) | Autoware 外部接口消息 | 50+ / 50+ | Autoware AD API message definitions. |
| 39 | [ros2/rmw_fastrtps](https://github.com/ros2/rmw_fastrtps) | ROS2 Fast DDS RMW | 100+ / 200+ | ROS middleware implementation using eProsima Fast DDS. |
| 40 | [ros2/rmw_cyclonedds](https://github.com/ros2/rmw_cyclonedds) | ROS2 Cyclone DDS RMW | 100+ / 100+ | ROS middleware implementation using Eclipse Cyclone DDS. |

## 后续拆解建议

- 任务与规划框架：优先拆 BehaviorTree.CPP、MoveIt、geometric_shapes、moveit_visual_tools。
- 感知输入适配：优先拆 perception_pcl、vision_opencv、image_pipeline、laser_geometry、pointcloud_to_laserscan。
- 定位建图：优先拆 LeGO-LOAM、A-LOAM、FAST-LIVO、OpenVINS、Kalibr、KISS-ICP、fast_gicp。
- 工程接口：优先拆 Nebula、autoware_adapi_msgs、rmw_fastrtps、rmw_cyclonedds、ROS2 launch/message_filters。

## 更新记录

- 2026-06-24：第五批整理 40 个未入库 GitHub 资源，并建立 40 篇单源笔记。
