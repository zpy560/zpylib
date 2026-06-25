---
id: "20260615-cpprobotics"
title: "CppRobotics"
type: "entity"
source: "https://github.com/onlytailei/CppRobotics"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-15-cpprobotics-cpp-robotics-algorithm-demos.md
  - notes/2026-06-24-youngtimes-algorithms-planning-demos.md
  - wiki/2026-06-14-ros-motion-planning.md
  - wiki/2026-06-15-chhrobotics-cpp.md
  - wiki/2026-06-15-dev-xys-algorithms.md
  - wiki/2026-06-15-mpcc.md
  - wiki/2026-06-24-pythonrobotics.md
  - wiki/2026-06-24-youngtimes-algorithms.md
---

# CppRobotics

## 基本信息

- 类型：机器人定位、规划和控制算法 C++ 教学示例集
- 作者：Lei Tai
- 官方仓库：https://github.com/onlytailei/CppRobotics
- 上游项目：https://github.com/AtsushiSakai/PythonRobotics
- 主要语言：C++11
- 主要依赖：Eigen3、OpenCV
- MPC 依赖：CppAD、IPOPT
- 许可证：MIT
- 快照分支：`master`
- 快照提交：`e30a914c91eda87da068c076d942bb6251ba95cc`
- 快照日期：2026-06-15
- 分析方式：本地静态源码分析，未编译、未运行

## 当前判断

CppRobotics 适合用最少代码理解经典机器人算法，不适合直接作为工程依赖。它的正确位置是“可视化算法教材”，不是“机器人算法 SDK”。

## 实际算法

### 定位

- Extended Kalman Filter
- Particle Filter

### 规划

- Dijkstra
- A*
- RRT / RRT*
- Dynamic Window Approach
- Cubic Spline
- Model Predictive Trajectory Generator
- State Lattice
- Frenet Optimal Trajectory

### 控制

- LQR Steering
- LQR Speed and Steering
- MPC 源码，默认不构建

## 架构

```text
硬编码仿真场景
→ 独立算法实现
→ OpenCV 可视化
→ GUI 或图片输出
```

每个算法基本对应一个可执行文件。项目没有公共库、统一接口、安装规则、配置系统、测试或 CI。

## 最值得学习

- 栅格搜索和采样规划的基本控制流。
- Frenet 横纵向多项式候选生成。
- State Lattice 终端状态采样与轨迹初值。
- DWA 速度空间采样与代价。
- LQR 误差状态、曲率前馈和反馈控制。

## 工程边界

- 参数和场景硬编码。
- 算法与 OpenCV GUI 耦合。
- 依赖 OpenCV 3.3 的历史环境。
- README 含未实现能力。
- MPC 构建默认关闭。
- 相对路径和输出目录脆弱。
- 缺少动态障碍、复杂车辆边界和安全机制。
- 无自动回归测试。

## 与 ROS Motion Planning

CppRobotics 用独立小程序解释算法；ROS Motion Planning 将规划控制算法放入 ROS1 `move_base`、costmap、Gazebo 和 RViz 中。推荐先读 CppRobotics，再用 ROS Motion Planning 观察系统集成代价。

## 关联笔记

- `notes/2026-06-15-cpprobotics-cpp-robotics-algorithm-demos.md`
- `wiki/2026-06-14-ros-motion-planning.md`
- `wiki/2026-06-15-mpcc.md`
- `wiki/2026-06-15-dev-xys-algorithms.md`
- `wiki/2026-06-15-chhrobotics-cpp.md`

## 更新记录

- 2026-06-15：基于官方 `master` 提交 `e30a914` 完成算法、源码组织、构建与工程边界建档。
- 2026-06-15：补充与 MPCC 自主赛车预测控制实现的进阶关联。
- 2026-06-15：补充与 Dev-XYS Algorithms 竞赛算法模板集的对比关联。
- 2026-06-15：补充与 chhRobotics_CPP 规划控制演示集的对比关联。
