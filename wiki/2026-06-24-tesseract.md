---
id: "20260624-211036-tesseract-wiki"
title: "Tesseract"
type: "entity"
source: "notes/2026-06-24-tesseract-robotics-planning-framework.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-tesseract-robotics-planning-framework.md
---

# Tesseract

## 定位

Tesseract 是 ROS-Industrial 机器人规划框架，强调轻量依赖、ROS-agnostic core 和 Python 支持。

## 适合研究的问题

- 工业机器人规划框架如何组织环境、碰撞、规划和执行接口。
- 规划核心如何与 ROS 集成层解耦。
- Tesseract、MoveIt、Descartes 的边界和适用场景。

## 使用边界

它是框架，不是单个算法。使用前需要确认目标任务、ROS 版本、Python/C++ 接口、工业机器人模型和规划器插件支持情况。

## 入库来源

- 单源笔记：../notes/2026-06-24-tesseract-robotics-planning-framework.md
- 仓库：https://github.com/ros-industrial-consortium/tesseract

