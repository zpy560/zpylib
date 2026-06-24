---
id: "20260624-navigation2-dynamic-obstacle-tracking-pipeline"
title: "navigation2_dynamic：Nav2 动态障碍跟踪管线"
type: "note"
source: "raw/2026-06-24-navigation2-dynamic-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-navigation2-dynamic.md
  - wiki/2026-06-13-navigation2.md
---

# navigation2_dynamic：Nav2 动态障碍跟踪管线

## 一句话结论

navigation2_dynamic 是 Nav2 动态障碍方向的实验性支撑仓库，核心包括动态障碍消息和基于 Kalman Filter + Hungarian assignment 的多目标跟踪器；它更像动态障碍感知/跟踪原型，不是完整动态避障导航栈。

## 原文要点

- README 定位为 Nav2 dynamic obstacle detection、tracking、processing pipelines。
- 仓库包含 `nav2_dynamic_msgs` 和 `kf_hungarian_tracker`。
- `kf_hungarian_tracker` 用 Hungarian algorithm 做检测与已有目标关联。
- 每个目标维护一个 Kalman filter，跟踪位置和速度。
- 默认关联代价为目标中心欧氏距离，也可扩展 IoU 等代价。
- 动态障碍消息包含 UUID、置信度、位置、速度、尺寸和协方差。

## 我的判断

### 价值在接口和跟踪骨架

这个仓库最值得看的是动态障碍的消息契约和 tracker 的最小处理链：检测输入如何变成带 ID、速度和协方差的 obstacle array。对 Nav2 动态避障，稳定的障碍状态表示比单帧检测更关键。

### 离完整动态导航还有距离

它没有直接证明动态障碍如何进入 costmap、controller 或 behavior tree 决策，也没有给出预测、速度障碍、时空规划或安全验证闭环。使用时应把它当作感知跟踪上游，而不是直接等价于动态避障算法。

## 可复用内容

- 动态障碍消息字段设计。
- Kalman + Hungarian 多目标跟踪最小架构。
- 速度、高度、关联代价等过滤参数。
- 与 Nav2 costmap/controller 集成前的跟踪层参考。

## 疑问与冲突

- 本次未运行 tracker，也未检查输入检测消息来源。
- 未验证是否仍与当前 Nav2 主线接口兼容。
- README 很短，部分结论来自文件树和 package README。

## 原料

- `raw/2026-06-24-navigation2-dynamic-repository-snapshot.md`
