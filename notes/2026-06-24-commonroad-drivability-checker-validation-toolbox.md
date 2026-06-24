---
id: "20260624-commonroad-drivability-checker-validation-toolbox"
title: "CommonRoad Drivability Checker：规划轨迹可行性验证工具箱"
type: "note"
source: "raw/2026-06-24-commonroad-drivability-checker-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-commonroad-drivability-checker.md
  - notes/2026-06-24-commonroad-route-planner-reference-path.md
---

# CommonRoad Drivability Checker：规划轨迹可行性验证工具箱

## 一句话结论

CommonRoad Drivability Checker 不负责生成轨迹，而是验证轨迹是否满足碰撞规避、运动学可行性和道路约束；它适合做自动驾驶规划算法的回归测试和 benchmark 检查。

## 原文要点

- README 明确统一 collision avoidance、kinematic feasibility、road-compliance checks。
- 兼容 CommonRoad benchmark suite。
- 支持 Python 包安装，也可源码构建。
- 包含 2025.1 后 curvilinear coordinate system 迁移到 `commonroad-clcs` 的弃用提示。
- 技术栈是 Python 3.10 和 C++17。

## 我的判断

规划算法没有验证工具容易变成只看轨迹形状。这个仓库补的是“能不能开、是否合法、会不会撞”的检查层，应该和 route planner、trajectory planner 分开理解。

## 可复用内容

- 轨迹可行性与道路合规检查。
- CommonRoad benchmark 回归验证。
- 碰撞检测和约束检查工具链。

## 疑问与冲突

- 版本迁移提示需要注意，尤其是 curvilinear 坐标相关代码。
- 它验证规划结果，不替代规划算法。

## 原料

- `raw/2026-06-24-commonroad-drivability-checker-repository-snapshot.md`

