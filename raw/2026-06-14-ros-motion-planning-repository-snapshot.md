# ROS Motion Planning 仓库快照

## 来源与版本

- 官方仓库: https://github.com/ai-winter/ros_motion_planning.git
- 分支: `dev`
- 提交: `a6f21b0e7a5aa714bab204289f7a4835b2148fa4`
- 提交日期: 2026-03-28
- 分析日期: 2026-06-14
- 分析方式: 本地静态分析，未安装依赖、未编译、未运行 ROS/Gazebo
- 许可证: GPLv3

## 项目定位

项目面向 ROS Noetic 和 Ubuntu 20.04，提供移动机器人运动规划算法、`move_base` 接口、Gazebo 仿真环境、RViz 可视化和动态配置工具。

README 将运动规划分为 Path Searching 与 Trajectory Optimization。仓库实际结构主要由全局路径规划、局部控制、曲线生成、costmap 插件、仿真环境和配置生成工具组成。

## 全局规划算法

全局规划器实现为 `PathPlanner` 子类，并由 `PathPlannerNode` 适配 `nav_core::BaseGlobalPlanner`。工厂根据 ROS 参数 `planner_name` 创建实现。

主要算法包括：

- 图搜索: GBFS、Dijkstra、A*、JPS、D*、LPA*、D* Lite、Voronoi、Theta*、Lazy Theta*、S-Theta*、Hybrid A*。
- 采样规划: RRT、RRT*、RRT-Connect、Informed RRT*。
- 进化规划: ACO、GA、PSO。
- 另有 Lazy Planner。

所有全局算法建立在 ROS `costmap_2d` 上。基类统一地图尺寸、坐标转换、边界处理和 CollisionChecker；采样与任意角算法使用 Bresenham 线段碰撞检测。D*、LPA* 和 D* Lite 保存前后 costmap 快照以处理变化区域。

## 局部控制算法

局部算法以 pluginlib 插件接入 `nav_core::BaseLocalPlanner`：

- PID
- LQR
- DWA
- APF
- RPP
- MPC
- ORCA，多机器人配置使用该控制器
- Static Controller

README 将 TEB 与 Lattice 标为开发中。DWA 复用了 ROS `base_local_planner` 的轨迹采样和代价函数。

## 曲线与环境

曲线生成模块包括 Polynomial、Bezier、Cubic Spline、B-Spline、Dubins 和 Reeds-Shepp。

环境侧支持：

- global/local costmap 图层组合
- static map、obstacle、inflation 和 Voronoi layer
- Gazebo 静态障碍物
- 基于 Social Force Model 的动态行人
- 多机器人仿真和目标发布

## 配置与启动

用户主要编辑 `src/user_config/user_config.yaml`，选择地图、世界、机器人类型、全局规划器、局部控制器和插件。`scripts/main.sh` 执行：

```text
source devel/setup.bash
→ dynamic_xml_config/main_generate.py
→ 重新生成 launch/world/RViz 等配置
→ roslaunch sim_env main.launch
```

因此直接修改生成后的 launch 文件可能在下次启动时被覆盖。

## 工程限制

- 目标环境是 ROS1 Noetic，不是 ROS2。
- 全局算法虽然共享抽象基类，但工厂仍使用集中式字符串条件分支。
- 项目侧重算法展示和统一实验环境，不覆盖完整任务编排、生命周期、恢复策略或量产安全链。
- README 的“Trajectory Optimization”定位比当前代码结构更宽；本快照中主要可见的是路径规划、局部控制和曲线生成。
