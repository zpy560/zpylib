---
id: "20260614-ros-motion-planning-algorithm-workbench"
title: "ROS Motion Planning：统一实验环境下的规划算法工作台"
type: "note"
source: "raw/2026-06-14-ros-motion-planning-repository-snapshot.md"
created_at: "2026-06-14"
tags:
  - planning-control
  - autonomous-driving
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-14-ros-motion-planning.md
  - notes/2026-06-13-navigation2-ros2-navigation-framework.md
  - notes/2026-06-15-cpprobotics-cpp-robotics-algorithm-demos.md
  - notes/2026-06-15-hybrid-a-star-ros1-vehicle-path-planner.md
---

# ROS Motion Planning：统一实验环境下的规划算法工作台

## 一句话结论

ROS Motion Planning 的价值是把图搜索、采样、进化规划、局部控制和曲线生成算法放进统一的 ROS1 costmap、`move_base`、Gazebo 与 RViz 环境中，适合做算法学习和横向对比；它不是完整导航系统，也不提供量产自动驾驶所需的任务编排与安全闭环。

## 原文要点

### 全局算法共享 costmap 接口

```text
move_base
→ nav_core::BaseGlobalPlanner
→ PathPlannerNode
→ PathPlannerFactory
→ PathPlanner 派生算法
→ nav_msgs/Path
```

全局算法分为图搜索、采样和进化三类。基类负责 costmap、坐标转换、边界障碍化和碰撞检查，具体算法只实现搜索过程。

### 局部算法以 ROS 插件接入

PID、LQR、DWA、APF、RPP、MPC、ORCA 等控制器实现 `nav_core::BaseLocalPlanner`，由 `move_base` 调用。项目同时提供 Polynomial、Bezier、Spline、Dubins 和 Reeds-Shepp 等曲线工具。

### 配置文件是仿真系统入口

`user_config.yaml` 选择机器人、地图、世界和规划控制算法。启动脚本根据它重新生成 launch、world 和 RViz 配置，再运行 Gazebo 与 `move_base`。

## 我的判断

### 最适合用于算法比较，而不是系统架构复用

同一 costmap、机器人模型和仿真环境能降低算法横向比较的环境差异，便于观察 A*、Theta*、RRT*、ACO 或不同控制器的行为差别。

但仓库并没有统一的评测协议。若要得到可信结论，还需补充固定随机种子、地图集、成功率、路径长度、曲率、规划耗时、控制误差和最小障碍距离等指标。

### 抽象统一，但扩展注册仍偏集中

`PathPlanner` 和 `nav_core` 接口使算法调用方式一致；然而新增全局算法还需要修改 `PathPlannerFactory` 的字符串条件分支。相比 pluginlib 的真正运行时注册，这种方式更适合教学仓库，不利于独立包扩展。

### 动态配置生成提高易用性，也增加隐式状态

单一 YAML 生成 launch/world 的方式适合快速实验，但生成物与源配置存在双层状态。调试时必须确认当前运行文件是否由最新 YAML 生成，不能只看 launch。

### 与 Navigation2 的差别

ROS Motion Planning 聚焦算法实现和仿真展示；Navigation2 聚焦任务编排、能力服务器、生命周期、恢复和安全后处理。前者可以作为算法原型来源，后者才是更完整的 ROS2 导航系统骨架。

CppRobotics 提供更轻量的纯 C++ 单算法示例，适合先理解算法控制流；ROS Motion Planning 则用于观察这些算法进入 costmap、`move_base`、插件和 Gazebo 后的系统行为。

独立 Hybrid A Star 仓库更聚焦车辆 `(x, y, yaw)` 状态搜索、前后向运动原语和 Reeds-Shepp 解析扩展，可用于深入阅读 ROS Motion Planning 中 Hybrid A* 类算法背后的核心机制，但该实现存在已确认的地图和 open-set 正确性问题。

## 可复用内容

### 规划算法实验基线

```text
统一地图与机器人
→ 统一 costmap 和碰撞模型
→ 可替换全局规划器
→ 可替换局部控制器
→ 固定场景与随机种子
→ 自动统计性能和安全指标
```

### 阅读顺序

1. 从 `user_config.yaml` 确认实验组合。
2. 检查配置生成脚本输出。
3. 从 `nav_core` 插件入口追踪全局与局部链路。
4. 检查 costmap 图层和碰撞阈值。
5. 再阅读具体算法实现与参数。

## 疑问与冲突

- README 把 Trajectory Optimization 作为核心组成，但当前目录更偏局部控制和曲线生成，严格的时空轨迹优化覆盖有限。
- TEB 与 Lattice 在 README 中仍标为开发状态。
- 本次未编译或运行，ROS Noetic 依赖、Conan 版本和 Gazebo 场景可用性未验证。

## 原料

- `raw/2026-06-14-ros-motion-planning-repository-snapshot.md`
