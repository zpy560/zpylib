# Navigation2 Tutorials 官方仓库源码快照

> 本文件记录 2026-06-24 对官方仓库的静态检查事实。分析与判断见对应的 `notes/` 和 `wiki/` 文件。

## 来源

- 官方仓库：https://github.com/ros-navigation/navigation2_tutorials.git
- 官方文档：https://docs.nav2.org/
- 默认分支：`rolling`
- 其他分支：`humble`、`jazzy`、`kilted`
- 抓取提交：`86f674fef07f2e9e78bdaebbedd88292840b3011`
- 提交时间：`2026-05-15 09:54:23 -0700`
- 提交标题：`Add tutorial for usage of ground consistency layer (#142)`
- 抓取方式：Git 浅克隆
- 分析方式：静态源码、配置和 launch 文件分析，未在 ROS 2 环境编译运行

## 仓库定位

根 README 仅说明本仓库是 `docs.nav2.org` 引用的教程代码。源码实际由多个 ROS 2 包组成，用于展示 Nav2 插件开发、仿真接入和传感器增强导航，而不是 Navigation2 主仓库本身。

当前教程覆盖：

- 全局规划器插件：`nav2_straightline_planner`
- 控制器插件：`nav2_pure_pursuit_controller`
- Costmap layer 插件：`nav2_gradient_costmap_plugin`
- Costmap filter 演示：`nav2_costmap_filters_demo`
- Behavior 插件：`nav2_sms_behavior`
- GPS waypoint follower 演示：`nav2_gps_waypoint_follower_demo`
- 语义分割感知与 costmap 集成演示：`nav2_semantic_segmentation_demo`
- 激光地面分割与 ground consistency layer 演示：`nav2_lidar_ground_segmentation_demo`
- 差速机器人 URDF/Gazebo/RViz 示例：`sam_bot_description`

## 快照规模

- 浅克隆目录：约 121 MB。
- 文件总数：128。
- 关键源码与配置文件：约 64。
- C++ 源文件：5。
- C++ 头文件：6。
- Python 文件：23。
- Markdown 文件：6。
- YAML 文件：16。
- XML 文件：14。
- Launch 文件：多个 Python launch。

## 包结构

| 包 | 职责 | 主要许可证 |
|---|---|---|
| `nav2_straightline_planner` | 展示 `nav2_core::GlobalPlanner` 插件注册和路径生成 | BSD-3-Clause |
| `nav2_pure_pursuit_controller` | 展示 `nav2_core::Controller` 插件注册和 Pure Pursuit 控制 | BSD-3-Clause |
| `nav2_gradient_costmap_plugin` | 展示 `nav2_costmap_2d::Layer` 插件注册和 costmap 更新窗口 | BSD-3-Clause |
| `nav2_costmap_filters_demo` | 演示 keepout 与 speed filter mask server 配置 | Apache 2.0 |
| `nav2_sms_behavior` | 展示 `nav2_core::Behavior` 插件与自定义 Action | MIT |
| `nav2_gps_waypoint_follower_demo` | 用 `BasicNavigator` 发送 GPS waypoint，并用 `robot_localization` 做 GPS/IMU/odom 融合 | MIT |
| `nav2_semantic_segmentation_demo` | ONNX segmentation 节点与语义 costmap layer 仿真 | BSD-3-Clause |
| `nav2_lidar_ground_segmentation_demo` | Gazebo Husky + VLP-16 + ground segmentation + Nav2 ground consistency layer | BSD-3-Clause |
| `sam_bot_description` | 差速机器人描述、Gazebo bridge、EKF 与 RViz 示例 | Apache 2.0 |

## 插件示例事实

### Straight Line Planner

- 实现 `nav2_core::GlobalPlanner`。
- 在 `configure()` 中读取 `interpolation_resolution`。
- `createPlan()` 支持 `viapoints`，逐段线性插值生成 `nav_msgs/Path`。
- 只检查 start/goal frame 是否等于 costmap global frame。
- 不查询 costmap 障碍、不做碰撞检测、不处理 `cancel_checker`。
- 当两点距离小于插值分辨率时，`total_number_of_loop` 可能为 0，随后计算增量存在除零风险。

### Pure Pursuit Controller

- 实现 `nav2_core::Controller`。
- 参数包括 `desired_linear_vel`、`lookahead_dist`、`max_angular_vel`、`transform_tolerance`。
- 将全局路径变换到 robot base frame，选择第一个超过 lookahead 距离的点。
- 若 lookahead 点在机器人前方，使用曲率 `2y / (x^2 + y^2)` 生成角速度；否则原地旋转。
- `setSpeedLimit()` 为空实现。
- 未主动检查局部 costmap 碰撞、加速度约束、曲率连续性或目标速度收敛。

### Gradient Costmap Layer

- 实现 `nav2_costmap_2d::Layer`。
- 展示 `onInitialize()`、`updateBounds()`、`updateCosts()`、`onFootprintChanged()` 和 pluginlib 导出。
- 直接写 `master_grid` 的 char map，生成周期性梯度代价。
- 注释明确说明这会覆盖其他 layer；生产插件应使用 `costmap_` 并调用合适的 merge 方法。

### SMS Behavior

- 实现 `nav2_core::Behavior`，自定义 `SendSms.action`。
- 通过参数读取 Twilio `account_sid`、`auth_token`、`from_number`、`to_number`。
- 用 libcurl 调 Twilio REST API 发送短信。
- 这是 Behavior 插件与外部服务集成示例，不适合默认进入机器人恢复链。

## 集成演示事实

### Costmap Filters

`nav2_costmap_filters_demo` 安装 filter mask、参数和 launch。示例包含：

- keepout filter：`type: 0`，mask topic 为 `/keepout_filter_mask`。
- speed filter：`type: 1`，mask topic 为 `/speed_filter_mask`，`base: 100.0`，`multiplier: -1.0`。
- launch 支持普通节点和 composable node 两种加载方式。

### GPS Waypoint Follower

`nav2_gps_waypoint_follower_demo` 包含：

- `demo_waypoints.yaml`：经纬度与 yaw waypoint。
- `dual_ekf_navsat_params.yaml`：两个 EKF 和 `navsat_transform` 配置。
- `nav2_no_map_params.yaml`：移除 AMCL/static layer，global costmap 使用 rolling 模式。
- `interactive_waypoint_follower.py`：从 Mapviz `/clicked_point` 接收 `wgs84` 点并调用 `followGpsWaypoints()`。
- `logged_waypoint_follower.py`：从 YAML 读取 GPS waypoint。
- `gps_waypoint_logger.py`：用 Tkinter 记录 `/gps/fix` 与 `/imu` 到 YAML。

### Semantic Segmentation

`semantic_segmentation_node`：

- 订阅 RGB 图像，默认 topic `/rgbd_camera/image`。
- 使用 ONNX Runtime 推理。
- 发布 class id mask、confidence、overlay 和 `vision_msgs/LabelInfo`。
- 默认 CPU provider，可配置 CUDA provider。
- README 说明模型可由 Simple Segmentation Toolkit 生成。

`semantic_segmentation_sim`：

- 使用 TurtleBot 4、RGBD camera、Baylands world。
- 依赖外部 `semantic_segmentation_layer`。
- 将语义 mask、confidence、point cloud 投影到 costmap，并按 terrain class 分配代价。

### Lidar Ground Segmentation

`nav2_lidar_ground_segmentation_demo`：

- 提供 Gazebo 仿真、Husky 差速机器人、Velodyne VLP-16 模型和 Nav2 配置。
- 依赖 `kiss_icp`、`ground_segmentation`、`ground_segmentation_ros2`、`nav2_ground_consistency_costmap_plugin`。
- `dependencies.repos` 将这些依赖指向外部 Git 仓库。

### Sam Bot

`sam_bot_description`：

- 提供差速机器人描述、Gazebo world、bridge 配置、EKF 参数、RViz 配置和 display launch。
- bridge 涵盖 clock、IMU、odom、joint states、cmd_vel、scan、point cloud、depth camera。

## 构建与测试观察

- 仓库没有顶层 CI 工作流。
- 仅 `nav2_gps_waypoint_follower_demo` 包含 Python lint 测试文件。
- 多数 CMake 包只接入 `ament_lint_auto`，未发现针对算法行为的单元测试或仿真回归。
- 未执行 `colcon build`，原因是本地未确认完整 ROS 2 rolling/Nav2/Gazebo/外部感知依赖环境。

## 工程边界

- 教程代码与 Nav2 rolling API 绑定，使用 Humble/Jazzy/Kilted 时必须切换对应分支。
- 插件示例重在接口骨架，不代表推荐生产算法。
- 多数示例参数、topic、frame 和 world 与示例机器人强绑定。
- GPS、语义分割和地面分割演示依赖外部包、仿真资源和模型文件。
- SMS 行为涉及外部 API 凭据，使用时必须通过环境或安全参数管理，不能写入仓库。
- 生产化至少需要补充碰撞检查、取消处理、速度限制、异常路径、可重复测试和场景回归。
