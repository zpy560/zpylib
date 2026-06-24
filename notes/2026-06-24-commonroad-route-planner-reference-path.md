---
id: "20260624-commonroad-route-planner-reference-path"
title: "CommonRoad Route Planner：路线与参考路径规划器"
type: "note"
source: "raw/2026-06-24-commonroad-route-planner-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-commonroad-route-planner.md
  - notes/2026-06-24-commonroad-drivability-checker-validation-toolbox.md
---

# CommonRoad Route Planner：路线与参考路径规划器

## 一句话结论

CommonRoad Route Planner 负责 CommonRoad 场景中的路线和参考路径生成，适合自动驾驶规划算法的基准场景预处理；它不是行为决策、轨迹优化或控制器。

## 原文要点

- README 定位为 extendable, lightweight route and reference path planner。
- 面向 CommonRoad 项目。
- 支持 PyPI 安装 `commonroad-reference_path-planner`。
- README 说明项目已在仿真和真实自动驾驶车辆中部署过。

## 我的判断

它适合放在规划链路的上游：先给出 route/reference path，再交给局部轨迹规划、可行性检查或控制器。和 drivability checker 组合后，可以形成 CommonRoad 场景下的“生成-验证”闭环。

## 可复用内容

- CommonRoad 场景参考路径生成。
- route planner 与 trajectory planner 的边界。
- 基准场景算法评估前处理。

## 疑问与冲突

- README 说仍在开发中，接口稳定性需要确认。
- 不替代轨迹规划和控制闭环。

## 原料

- `raw/2026-06-24-commonroad-route-planner-repository-snapshot.md`

