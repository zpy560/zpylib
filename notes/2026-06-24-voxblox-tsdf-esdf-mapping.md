---
id: "20260624-210023-voxblox-note"
title: "Voxblox：面向机载规划的 TSDF/ESDF 增量建图"
type: "note"
source: "raw/2026-06-24-voxblox-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-voxblox.md
---

# Voxblox：面向机载规划的 TSDF/ESDF 增量建图

## 结论

Voxblox 不是 planner，但对无人机和移动机器人规划非常关键：它把传感器数据组织成 TSDF/ESDF 地图，让局部规划器能查询障碍距离和空间可行性。

## 事实摘录

- 远端仓库：`ethz-asl/voxblox`
- 当前核对 HEAD：`c8066b04075d2fee509de295346b1c0b788c4f38`
- README 定位：基于 TSDF 的 volumetric mapping library。
- 特性包括 CPU-only、多 layer、protobuf 序列化、ROS 集成、可扩展 integrator、从 TSDF 构建 ESDF。
- README 明确提示 planning applications 参考 `mav_voxblox_planning`。

## 对规划控制的意义

- ESDF 是许多梯度型局部规划、轨迹优化和碰撞代价构造的基础。
- 对 MAV onboard planning，增量更新和 CPU-only 特性比离线地图更重要。
- 它帮助把 perception/mapping 与 planning cost 连接起来。

## 使用建议

如果目标是理解规划算法，Voxblox 应和消费 ESDF 的 planner 一起读。先看 TSDF integration、ESDF update、ROS 接口和 map layer 数据结构，再看 planner 如何查询距离、梯度和碰撞。

