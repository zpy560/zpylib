---
id: "20260624-navigation2-tutorials-nav2-plugin-and-integration-examples"
title: "Navigation2 Tutorials：Nav2 插件与集成教程代码集合"
type: "note"
source: "raw/2026-06-24-navigation2-tutorials-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-navigation2-tutorials.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
---

# Navigation2 Tutorials：Nav2 插件与集成教程代码集合

## 一句话结论

navigation2_tutorials 不是 Nav2 主框架，而是 `docs.nav2.org` 配套的教程代码仓库，最有价值的是展示 Nav2 的 pluginlib 接口、Lifecycle 回调、costmap layer/filter、GPS waypoint、语义分割和地面分割如何接入完整导航链；其中 straight-line planner、pure pursuit controller、gradient layer 和 SMS behavior 都是教学骨架，不能直接当作生产规划控制或安全行为模块。

## 原文要点

### 教程覆盖面

仓库按 ROS 2 包组织，覆盖三类内容：

```text
插件开发
→ GlobalPlanner / Controller / Costmap Layer / Behavior

导航功能集成
→ Costmap Filter / GPS Waypoint / Semantic Segmentation / Ground Segmentation

仿真与机器人描述
→ URDF/SDF / Gazebo bridge / EKF / RViz
```

默认分支是 `rolling`，同时有 `humble`、`jazzy`、`kilted` 分支。教程代码与 Nav2 API 和 ROS 发行版强绑定，复现时应先切到目标发行版分支。

### 插件接口骨架

`nav2_straightline_planner` 展示 `nav2_core::GlobalPlanner` 的最小插件形态：`configure()` 读取参数，`createPlan()` 生成 `nav_msgs/Path`，最后通过 pluginlib 导出。

`nav2_pure_pursuit_controller` 展示 `nav2_core::Controller` 的最小控制器形态：配置参数、将路径变换到机器人坐标系、选取 lookahead 点、输出 `TwistStamped`。

`nav2_gradient_costmap_plugin` 展示 costmap layer 的关键回调：初始化、更新边界、更新代价、footprint 变化和 pluginlib 注册。

`nav2_sms_behavior` 展示 Behavior 插件、自定义 Action 与外部 HTTP 服务的连接方式。

### 集成演示

Costmap filter 演示提供 keepout mask 和 speed mask，配套 `filter_mask_server`、`costmap_filter_info_server` 和 lifecycle manager launch，且支持 composable node。

GPS waypoint 演示用 `robot_localization` 融合 GPS、IMU、odom，移除静态地图和 AMCL，让 Nav2 在 rolling global costmap 上执行经纬度 waypoint。

语义分割演示用 ONNX Runtime 对 RGB 图像推理，发布 mask、confidence、overlay 和 label info，再由外部 semantic segmentation costmap layer 投影到代价地图。

激光地面分割演示用 Gazebo、Husky、VLP-16、KISS-ICP、ground segmentation 和 ground consistency layer 展示 3D lidar 如何影响 Nav2 costmap。

## 我的判断

### 它的价值在“怎么接入 Nav2”

主 Navigation2 笔记已经覆盖了系统架构；这个仓库补上的是可运行包层面的接口样板：

- 插件 XML 怎么声明。
- `package.xml` 怎样导出 Nav2 插件。
- 生命周期回调需要放哪些初始化和清理。
- costmap layer 如何声明更新区域并写代价。
- Python `BasicNavigator` 如何调用 GPS waypoint。
- 感知结果如何通过 topic 和 costmap layer 进入导航约束。

如果目标是写自己的 planner、controller、costmap layer 或 behavior，这个仓库比直接啃 Nav2 主仓库更适合作为入口。

### 示例算法本身很弱，不应误读为推荐实现

直线 planner 不查 costmap 障碍、不处理取消，还存在短距离时插值循环数为 0 的除零风险。Pure Pursuit controller 没有实现 `setSpeedLimit()`，没有主动碰撞检查，也没有加速度、曲率连续性或终点减速策略。Gradient layer 直接覆盖 master costmap，只是为了展示 API。SMS behavior 依赖 Twilio 凭据和外网，不适合默认恢复链。

这些问题不是仓库质量失败，而是教程定位决定的边界：它教接口，不教完整算法工程。

### 感知增强导航值得单独关注

语义分割和地面分割示例把 Nav2 的二维 costmap 与更丰富的感知结果连接起来：相机语义 mask 可以区分 sidewalk/grass，3D lidar ground segmentation 可以区分地面和障碍。这条线对自动驾驶算法也有参考价值：复杂感知结果最终需要压缩成规划可消费的约束表达。

但要注意，示例仍是移动机器人导航范式，不解决开放道路语义规则、动态交互预测、车辆动力学轨迹规划或功能安全验证。

### 复现成本比普通教程高

仓库只有少量算法源码，但集成演示依赖很重：Nav2 rolling、Gazebo、robot_localization、Mapviz、ONNX Runtime、semantic segmentation layer、KISS-ICP、ground segmentation 等。它适合在目标 ROS 发行版环境中逐包复现，不适合直接整仓库盲目 `colcon build` 后期待全部示例一次跑通。

## 可复用内容

### 写 Nav2 插件的最小清单

1. 实现对应 `nav2_core` 或 `nav2_costmap_2d` 基类。
2. 在 `configure()` 或 `onInitialize()` 中声明和读取参数。
3. 正确处理 Lifecycle 的 activate/deactivate/cleanup。
4. 用 pluginlib 宏导出类。
5. 写插件 XML。
6. 在 `package.xml` 的 `export` 中注册插件 XML。
7. 在 CMake 中构建共享库并安装 XML、头文件和库。
8. 在 Nav2 参数 YAML 中把插件名指向实现类。

### 教程阅读顺序

1. `nav2_straightline_planner`：理解 GlobalPlanner 接口。
2. `nav2_pure_pursuit_controller`：理解 Controller 接口。
3. `nav2_gradient_costmap_plugin`：理解 costmap layer 的更新模型。
4. `nav2_costmap_filters_demo`：理解 filter mask 与 filter info server。
5. `nav2_gps_waypoint_follower_demo`：理解无静态地图 GPS waypoint 导航。
6. `nav2_semantic_segmentation_demo`：理解语义感知如何进入 costmap。
7. `nav2_lidar_ground_segmentation_demo`：理解 3D lidar 地面分割如何服务导航。
8. `nav2_sms_behavior`：只作为 Behavior 插件和外部服务集成样板，不作为安全恢复行为。

### 生产化前必须补齐

- Planner：障碍检查、costmap footprint、取消处理、短距离边界、异常返回语义。
- Controller：速度限制、加速度限制、终点减速、碰撞预测、路径为空处理。
- Costmap layer：使用正确 merge 策略，不随意覆盖 master costmap。
- Behavior：外部 API 超时、凭据安全、失败隔离和恢复链安全策略。
- 感知示例：模型版本、类别定义、置信度阈值、延迟、失效检测和仿真/实车回归。

## 疑问与冲突

- 本次未执行 `colcon build`，因为本地未确认完整 ROS 2 rolling、Nav2、Gazebo 和外部感知依赖环境。
- 仓库没有顶层 CI，行为正确性需要依赖目标环境手动或补充测试验证。
- 教程分支与 ROS 发行版对应关系需要在使用前确认，不能拿 `rolling` 代码直接套到 Humble/Jazzy 项目。
- SMS 示例涉及 Twilio 账号、token 和电话号码，任何复现都不能把凭据写入知识库或代码。

## 原料

- `raw/2026-06-24-navigation2-tutorials-repository-snapshot.md`
