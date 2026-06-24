---
id: "20260624-planning-algorithm-current-status-refresh"
title: "planning_algorithm：当前状态确认"
type: "note"
source: "raw/2026-06-24-planning-algorithm-current-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
related:
  - wiki/2026-06-15-planning-algorithm.md
  - notes/2026-06-15-planning-algorithm-a-star-rrt-demos.md
---

# planning_algorithm：当前状态确认

## 一句话结论

planning_algorithm 当前远端 HEAD 仍停留在 `e5ce3ff`，与 2026-06-15 已建档版本一致；旧结论无需改变：这是 A* 与 RRT 的 OpenCV 最小演示，不是完整自动驾驶规划算法库。

## 原文要点

- README 推荐 Ubuntu 20.04/18.04、CMake 和 OpenCV 4。
- 构建后运行 `./a_star` 与 `./rrt`。
- README 说明坐标系为 X 向右、Y 向下。
- README 给出自动驾驶运动规划分类表，但实际源码范围仍需以仓库文件为准。

## 我的判断

### 这是状态刷新，不是新结论

本次 `git ls-remote` 看到的 HEAD 与旧条目一致，因此不重复改写旧分析。旧条目中关于 A* open-set 松弛缺失、RRT 边碰撞检查缺失、无许可证和无测试的判断仍有效。

### README 分类仍容易误导

README 的 taxonomy 覆盖 Dijkstra、A* family、State Lattice、RRT、曲线、数值优化等，但该仓库核心可运行内容只有 `a_star` 与 `rrt` 两个 demo。知识库中应继续把它归类为“最小可视化演示”。

## 可复用内容

- 用于演示 A* 栅格扩展和 RRT 随机树生长。
- 用于构造反例教学：为什么最小 demo 不等于正确算法基线。

## 疑问与冲突

- 无新提交，暂无增量源码可分析。
- 本次没有重新构建运行。

## 原料

- `raw/2026-06-24-planning-algorithm-current-repository-snapshot.md`
- `notes/2026-06-15-planning-algorithm-a-star-rrt-demos.md`
