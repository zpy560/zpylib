---
id: "20260615-hybrid-a-star"
title: "Hybrid A Star"
type: "entity"
source: "https://github.com/zm0612/Hybrid_A_Star"
created_at: "2026-06-15"
tags:
  - autonomous-driving
  - planning-control
  - programming
related:
  - notes/2026-06-15-hybrid-a-star-ros1-vehicle-path-planner.md
  - wiki/2026-06-24-motionplanning.md
  - wiki/2026-06-14-ros-motion-planning.md
---

# Hybrid A Star

## 基本信息

- 类型：ROS1 车辆 Hybrid A* 路径规划实现
- 作者：Zhang Zhimeng
- 官方仓库：https://github.com/zm0612/Hybrid_A_Star
- 主要语言：C++11
- 平台：ROS1 Melodic、catkin、RViz
- 依赖：Eigen3、glog、nav_msgs、tf、map_server
- 许可证：BSD 3-Clause
- 默认分支：`main`
- 快照提交：`cf0cc997f285e05a1ff51f36b224d3040fc7708c`
- 最后提交时间：2024-06-16
- 分析方式：静态源码分析，未在 ROS Melodic 环境编译运行

## 当前判断

该项目清晰实现了 Hybrid A* 的状态栅格、车辆运动原语、前后向代价、矩形碰撞和 Reeds-Shepp 解析扩展，适合作为泊车规划源码教材。但默认实现存在多项会影响搜索正确性的 bug，必须修复并建立测试后才能作为算法基线。

## 算法链

```text
OccupancyGrid
→ (x, y, yaw) 状态离散
→ 转角 × 前后方向运动原语
→ 矩形车辆碰撞检测
→ 转向/倒车/换向代价
→ L1 或 Reeds-Shepp 启发式
→ 近终点 Reeds-Shepp analytic shot
→ 路径与搜索树发布
```

## 核心参数

- 航向离散数：默认 72
- 状态栅格分辨率：ROS flow 固定 1.0 m
- 最大转角及离散数
- 轴距
- 原语长度和内部碰撞采样步数
- 转向、倒车、转角变化惩罚
- 解析连接距离

## 已确认问题

- 地图数组分配后未初始化。
- 邻居错误复用当前节点启发式。
- open-set 降代价更新未重新入队。
- 自定义地图上界遗漏 origin。
- 障碍写入边界存在越界条件。
- 车体碰撞只检查矩形边界。
- 起终点缺少完整 footprint 校验。
- 性能统计使用错误计时器。
- 搜索硬限制 50000 次。
- 后端轨迹优化器没有接入。

## 最值得学习

- 连续车辆状态与离散搜索索引的结合。
- 前进和倒车运动原语。
- 换向与转角变化代价。
- Reeds-Shepp 启发式和解析扩展。
- OccupancyGrid 与车辆矩形包络碰撞。
- RViz 交互式搜索调试。

## 工程边界

- 仅静态二维地图。
- 没有速度规划和动态约束。
- 没有动态障碍。
- 没有自动测试、CI 或基准结果。
- ROS1 Melodic 技术栈较旧。
- 路径还需平滑、方向分段、时间参数化和闭环跟踪。

## 关联笔记

- `notes/2026-06-15-hybrid-a-star-ros1-vehicle-path-planner.md`
- `wiki/2026-06-14-ros-motion-planning.md`

## 更新记录

- 2026-06-15：基于 `main` 提交 `cf0cc99` 完成搜索、Reeds-Shepp、碰撞、ROS 数据链和正确性风险建档。
