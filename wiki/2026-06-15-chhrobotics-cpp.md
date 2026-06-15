---
id: "20260615-chhrobotics-cpp"
title: "chhRobotics_CPP"
type: "entity"
source: "https://github.com/CHH3213/chhRobotics_CPP"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - notes/2026-06-15-chhrobotics-cpp-planning-control-demos.md
  - wiki/2026-06-15-cpprobotics.md
  - wiki/2026-06-15-planning-algorithm.md
---

# chhRobotics_CPP

## 基本信息

- 类型：自动驾驶路径规划与轨迹跟踪 C++ 教学演示集
- 作者：CHH3213
- 官方仓库：https://github.com/CHH3213/chhRobotics_CPP
- Python 上游：https://github.com/CHH3213/chhRobotics
- 主要语言：C++14
- 主要依赖：Eigen、Python 3、NumPy、matplotlib-cpp
- MPC 依赖：OsqpEigen、CppAD、IPOPT
- 许可证：未提供
- 默认分支：`master`
- 快照提交：`c8bc45c5b3c5b8bbe5cee823681ab343c3a3f39f`
- 最后提交时间：2024-05-25
- 分析方式：静态源码和 CMake 配置分析；因缺少 OsqpEigen 未完成构建

## 当前判断

chhRobotics_CPP 适合结合中文博客学习经典规划和控制算法，尤其适合比较搜索、采样、曲线规划与几何跟踪控制。它不是可靠算法库：MPC 未完成、构建依赖脆弱、缺少测试和许可证，并存在明确的曲率计算错误。

## 实际算法

### 路径规划

- Dijkstra、A*
- Artificial Potential Field
- Dynamic Window Approach
- RRT、RRT-Connect、RRT*
- Bezier、B-spline、Curve Interpolation
- Dubins、Reeds-Shepp

### 路径跟踪

- PID
- Pure Pursuit
- Stanley
- Rear Wheel Feedback
- LQR
- OsqpEigen MPC，未完成
- CppAD/IPOPT 速度与转向 MPC

README 中蚁群、动态规划、PRM、速度规划和 Kalman Filter 没有对应 C++ 源码。

## 架构

```text
硬编码演示场景
→ 独立算法类
→ 简化运动学模型
→ matplotlib-cpp 可视化
```

CMake 生成 19 个算法演示目标和一个空壳根程序，但没有可安装的算法库接口。

## 明确风险

- 曲率公式中的 `3 / 2` 被执行为整数除法。
- OSQP MPC 缺少完整动力学约束。
- CMake 无条件要求 OsqpEigen。
- Python 3.10 和 NumPy include 路径硬编码。
- IPOPT/CppAD 发现逻辑不完整。
- 搜索失败和空集合处理不足。
- 裸指针节点缺少清晰所有权。
- 无测试、CI、性能基准和许可证。

## 最值得学习

- 栅格搜索与启发式搜索对照。
- DWA 速度窗口和轨迹评价。
- RRT 系列的扩展、连接和重布线。
- Dubins/Reeds-Shepp 曲率约束路径。
- Pure Pursuit、Stanley、后轮反馈和 LQR 的误差定义差异。
- 从 Python 算法原型迁移到 C++ 类的基本过程。

## 关联笔记

- `notes/2026-06-15-chhrobotics-cpp-planning-control-demos.md`
- `wiki/2026-06-15-cpprobotics.md`
- `wiki/2026-06-15-planning-algorithm.md`

## 更新记录

- 2026-06-15：基于 `master` 提交 `c8bc45c` 完成算法范围、构建、数值问题和工程边界建档。
- 2026-06-15：增加 planning_algorithm 的 A*/RRT 最小演示对照。
