---
id: "20260624-ros-motion-planning-current-repository-refresh"
title: "ROS Motion Planning：当前仓库状态补充"
type: "note"
source: "raw/2026-06-24-ros-motion-planning-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - autonomous-driving
  - architecture
  - programming
  - tools
related:
  - wiki/2026-06-14-ros-motion-planning.md
  - notes/2026-06-14-ros-motion-planning-algorithm-workbench.md
---

# ROS Motion Planning：当前仓库状态补充

## 一句话结论

本次快照确认 ROS Motion Planning 仍应归类为 ROS1/Noetic 下的运动规划算法工作台：优势是算法覆盖面和仿真集成，短板仍是教学与实验属性强，不能直接等价为生产级导航系统。

## 原文要点

- GitHub 默认分支为 `dev`，快照提交为 `a6f21b0e7a5aa714bab204289f7a4835b2148fa4`。
- README 的快速开始环境是 Ubuntu 20.04 LTS 和 ROS Noetic。
- 依赖包括 `amcl`、`base_local_planner`、`map_server`、`move_base`、`navfn` 和 `libgoogle-glog-dev`。
- 构建入口是 `scripts/build.sh`，运行入口是 `scripts/main.sh`。
- README 明确提醒 launch 文件会从 `src/user_config/user_config.yaml` 重新生成，应修改 YAML 而不是生成后的 launch。
- 全局规划覆盖图搜索、采样和进化算法；局部规划覆盖 PID、LQR、DWA、APF、RPP、MPC 等；曲线生成覆盖多项式、Bezier、Spline、Dubins、Reeds-Shepp。

## 我的判断

### 原有结论不需要改方向

2026-06-14 的判断仍成立：该项目适合学习、演示和横向比较规划/控制算法，不适合作为 Navigation2、Autoware 或 Apollo 那类系统框架的替代品。

### 更适合作为算法试验平台

如果要做规划算法实验，它的价值是统一 ROS costmap、Gazebo、RViz 和机器人模型，降低环境差异。实验可信度仍取决于是否补充固定地图集、随机种子、运行次数、路径代价、规划耗时、碰撞距离和控制误差等指标。

### 配置生成机制是调试风险点

运行脚本会基于 YAML 生成 launch/world/RViz 配置。排查“参数改了没生效”时，不能只看 launch 文件，必须回到 `user_config.yaml` 和生成脚本。

## 可复用内容

- ROS1 `move_base` 插件化规划控制算法实验外壳。
- 经典全局规划算法目录：A*、JPS、D* Lite、Theta*、Hybrid A*、RRT 系列、ACO/GA/PSO。
- 经典局部控制与跟踪算法目录：DWA、APF、RPP、MPC、PID、LQR。
- 用统一配置切换地图、机器人、全局规划器和局部控制器的实验方式。

## 疑问与冲突

- README 把 motion planning 分为 path searching 与 trajectory optimization，但项目主体更偏搜索、跟踪控制和曲线生成，严格时空轨迹优化能力有限。
- README 中 TEB 与 Lattice 仍显示开发状态。
- 本次只做仓库资料快照，未执行 ROS/Gazebo 构建和仿真。

## 原料

- `raw/2026-06-24-ros-motion-planning-repository-snapshot.md`
- `notes/2026-06-14-ros-motion-planning-algorithm-workbench.md`
