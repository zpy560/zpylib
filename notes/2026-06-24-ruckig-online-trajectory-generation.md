---
id: "20260624-ruckig-online-trajectory-generation"
title: "Ruckig：在线轨迹生成库"
type: "note"
source: "raw/2026-06-24-ruckig-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - programming
  - tools
related:
  - wiki/2026-06-24-ruckig.md
  - notes/2026-06-24-toppra-time-optimal-path-parameterization.md
---

# Ruckig：在线轨迹生成库

## 一句话结论

Ruckig 的核心价值是在线生成满足速度、加速度、jerk 等限制的平滑轨迹，适合执行层或局部运动生成；它不负责选择路径、处理语义场景或避障策略。

## 原文要点

- README 将 Ruckig 定位为 motion generation library。
- 当前快照分支是 `main`，HEAD 为 `f48cf5f`。
- 仓库 README 较完整，包含使用文档和示例。

## 我的判断

Ruckig 适合补齐“规划输出到执行命令之间的轨迹时间化/平滑”环节。对机器人和自动驾驶都可借鉴，但前提是路径和目标已由上层确定。

## 可复用内容

- 在线轨迹生成接口。
- 运动学约束下的平滑命令生成。
- 执行层限速、限加速度、限 jerk 的思路。

## 疑问与冲突

- 不解决碰撞检测、动态障碍和任务规划。
- 多约束场景需要结合上层安全监控。

## 原料

- `raw/2026-06-24-ruckig-repository-snapshot.md`

