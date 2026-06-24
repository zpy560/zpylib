---
id: "20260624-pathplanning-search-sampling-algorithm-demos"
title: "PathPlanning：搜索与采样路径规划算法示例"
type: "note"
source: "raw/2026-06-24-pathplanning-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-pathplanning.md
  - wiki/2026-06-24-motionplanning.md
  - wiki/2026-06-24-pythonrobotics.md
---

# PathPlanning：搜索与采样路径规划算法示例

## 一句话结论

PathPlanning 是图搜索和采样式路径规划的示例集合，适合横向比较 A*、D*、RRT、RRT*、BIT* 等算法流程；它不提供完整导航系统、车辆动力学约束和工程部署接口。

## 原文要点

- README 明确实现 robotics 中常见 path planning algorithms。
- 搜索类覆盖 A*、D*、LPA*、ARA* 等大量变体。
- 采样类覆盖 RRT、RRT-Connect、Informed RRT*、FMT*、BIT* 等。
- 每个算法配动画展示运行过程。

## 我的判断

它适合补齐 PythonRobotics 和 MotionPlanning 之间的算法谱系：前者更综合，后者更偏自动驾驶车辆，这个仓库更聚焦路径规划算法本身。

## 可复用内容

- 搜索类和采样类规划器目录结构。
- 算法可视化教学材料。
- 选型前的快速算法地图。

## 疑问与冲突

- 不处理完整机器人感知、地图、控制闭环。
- 动态约束、障碍预测和实时性需要额外验证。

## 原料

- `raw/2026-06-24-pathplanning-repository-snapshot.md`

