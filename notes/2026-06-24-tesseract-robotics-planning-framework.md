---
id: "20260624-211035-tesseract-note"
title: "Tesseract：ROS-Industrial 机器人规划框架"
type: "note"
source: "raw/2026-06-24-tesseract-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-tesseract.md
---

# Tesseract：ROS-Industrial 机器人规划框架

## 结论

Tesseract 是 ROS-Industrial 体系里值得长期跟踪的规划框架。它和 MoveIt、Descartes 都相关，但更强调轻量、核心包 ROS 无关和 Python 支持。

## 事实摘录

- 远端仓库：`ros-industrial-consortium/tesseract`
- 当前核对 HEAD：`ecac4e7a1613e6145796cdee983eb6508739302b`
- README 定位：planning framework。
- 设计目标包括 lightweight、限制依赖、core packages ROS agnostic、full Python support。
- README 显示 Linux/Windows 和多项 lint/code quality CI。
- 项目支持等级为 ROS-Industrial consortium。

## 对规划控制的意义

- 对工业机器人：可作为 MoveIt/Descartes 之外的规划框架参考。
- 对架构：ROS-agnostic core 有助于理解如何把规划内核和 ROS 集成层分离。
- 对产品化：轻依赖和 Python 支持对工具链、调试和自动化流程有价值。

## 使用建议

建议与 MoveIt ROS1、MoveIt 2、Descartes 一起阅读，重点比较环境模型、碰撞检测、运动规划、任务规划和 ROS 集成边界。

