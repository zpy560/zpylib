# Navigation2 官方仓库快照

> 本文件记录 2026-06-13 抓取和检查到的官方事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/ros-navigation/navigation2
- 官方文档：https://docs.nav2.org/
- API 文档：https://api.nav2.org/
- 抓取分支：`main`
- 抓取提交：`374cd2556640586251b1e49a346f6c8d0cb76224`
- 提交时间：2026-06-08T13:18:28+02:00
- 提交标题：`[mppi] Add per-axis delay compensation with cmd-history replay (#6154)`
- GitHub 页面快照：约 4.3k stars、1.9k forks、3553 commits

## 项目定位

Navigation2（Nav2）是 ROS 2 的移动机器人导航框架。官方仓库将概念说明、入门、机器人接入、配置、插件、API、迁移和贡献文档统一指向 `docs.nav2.org`。

仓库采用多许可证模式，具体以各 ROS 包的 `package.xml` 为准；未单独标记的文件默认使用 Apache-2.0。

README 展示的构建目标包含 ROS 2 Humble、Jazzy 和 Kilted。支持状态会随时间变化，使用时应重新查看官方 distribution status。

## 仓库规模与组成

本次快照找到 46 个包含 `package.xml` 的 ROS 包，主要分为：

### 任务编排

- `nav2_bt_navigator`
- `nav2_behavior_tree`
- `nav2_msgs`

### 核心导航服务器

- `nav2_planner`
- `nav2_controller`
- `nav2_smoother`
- `nav2_behaviors`
- `nav2_route`

### 环境表达与定位

- `nav2_costmap_2d`
- `nav2_map_server`
- `nav2_amcl`
- `nav2_voxel_grid`

### 规划算法

- `nav2_navfn_planner`
- `nav2_smac_planner`
- `nav2_theta_star_planner`

### 控制算法

- `nav2_dwb_controller`
- `nav2_mppi_controller`
- `nav2_regulated_pure_pursuit_controller`
- `nav2_graceful_controller`
- `nav2_rotation_shim_controller`

### 安全与执行后处理

- `nav2_velocity_smoother`
- `nav2_collision_monitor`

### 任务扩展

- `nav2_waypoint_follower`
- `opennav_docking`
- `opennav_following`

### 系统运行与工具

- `nav2_lifecycle_manager`
- `nav2_bringup`
- `nav2_simple_commander`
- `nav2_rviz_plugins`
- `nav2_system_tests`
- `nav2_loopback_sim`

## 核心插件接口

`nav2_core/include/nav2_core/` 定义的主要扩展接口包括：

- `GlobalPlanner`
- `Controller`
- `Smoother`
- `Behavior`
- `BehaviorTreeNavigator`
- `GoalChecker`
- `ProgressChecker`
- `PathHandler`
- `WaypointTaskExecutor`

全局规划器通过 `createPlan()` 接收起点、终点、中间点和取消检查器，输出 `nav_msgs::msg::Path`。

控制器接收当前位姿、速度、目标检查器和经过变换裁剪的全局路径，输出 `geometry_msgs::msg::TwistStamped`。规划器与控制器接口都包含 `configure`、`activate`、`deactivate`、`cleanup` 生命周期方法。

## 默认运行节点

`nav2_bringup/launch/navigation_launch.py` 启动并由生命周期管理器管理：

- `controller_server`
- `smoother_server`
- `planner_server`
- `route_server`
- `behavior_server`
- `velocity_smoother`
- `collision_monitor`
- `bt_navigator`
- `waypoint_follower`
- `docking_server`
- `following_server`

这些节点既可以独立进程运行，也可以作为 composable nodes 装入同一容器，并可选择进程内通信。

## 默认行为树

默认 `navigate_to_pose_w_replanning_and_recovery.xml` 的主要行为：

1. 选择 progress checker、goal checker、path handler、controller 和 planner。
2. 以 1 Hz 检查并按需要重新规划。
3. 规划失败时先清理全局代价地图，再重试。
4. 控制失败时先清理局部代价地图，再重试。
5. 系统级恢复按轮询执行：清理代价地图、旋转、等待、后退。
6. 新目标到达时可中断恢复流程。

仓库同时提供按时间、距离、速度或路径有效性触发重规划的多种行为树，以及路线图导航、动态目标跟随和里程计标定行为树。

## 默认配置快照

`nav2_bringup/params/nav2_params.yaml` 在本次提交中的示例默认值包括：

- 全局规划器：`nav2_navfn_planner::NavfnPlanner`
- 控制器：`nav2_mppi_controller::MPPIController`
- 控制频率：20 Hz
- 平滑器：`nav2_smoother::SimpleSmoother`
- 恢复行为：spin、backup、drive-on-heading、assisted teleop、wait
- Waypoint 任务：到点等待
- Route Server：支持速度限制调整、重路由服务和碰撞检查操作
- Collision Monitor：接收 `cmd_vel_smoothed`，输出最终 `cmd_vel`

从启动文件和参数的组合可还原默认速度命令链：

```text
controller / behavior
→ cmd_vel_nav
→ velocity_smoother
→ cmd_vel_smoothed
→ collision_monitor
→ cmd_vel
```

## 生命周期

`nav2_lifecycle_manager` 统一管理节点的 configure、activate、deactivate、cleanup、shutdown、pause 和 resume，并使用 bond 监测节点连接状态。自动启动时，它按配置顺序完成节点配置与激活。

## 本次检查的关键文件

- `README.md`
- `LICENSE`
- `nav2_bringup/launch/navigation_launch.py`
- `nav2_bringup/params/nav2_params.yaml`
- `nav2_core/include/nav2_core/global_planner.hpp`
- `nav2_core/include/nav2_core/controller.hpp`
- `nav2_core/include/nav2_core/`
- `nav2_bt_navigator/behavior_trees/navigate_to_pose_w_replanning_and_recovery.xml`
- `nav2_bt_navigator/behavior_trees/`
- `nav2_lifecycle_manager/src/lifecycle_manager.cpp`
