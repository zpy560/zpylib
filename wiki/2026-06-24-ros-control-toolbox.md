---
id: "20260624-210016-ros-control-toolbox-wiki"
title: "ros-controls/control_toolbox"
type: "entity"
source: "notes/2026-06-24-ros-control-toolbox-controller-utilities.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-ros-control-toolbox-controller-utilities.md
---

# ros-controls/control_toolbox

## 定位

`ros-controls/control_toolbox` 是 ROS 控制器开发工具包，提供控制器实现中会用到的 C++ 类和 filter plugins。它属于控制工程基础设施。

## 适合研究的问题

- ROS 控制器如何复用 PID、滤波和控制工具。
- `ros2_control` 生态中哪些逻辑放在 framework，哪些放在 toolbox。
- 不同 ROS 发行版下控制工具包如何发布和维护。

## 使用边界

- 不是完整控制器集合，完整控制器集合应看 `ros2_controllers`。
- 不是硬件抽象框架，硬件接口和 controller manager 应看 `ros2_control`。
- 不是高层路径规划或轨迹规划库。

## 入库来源

- 单源笔记：../notes/2026-06-24-ros-control-toolbox-controller-utilities.md
- 仓库：https://github.com/ros-controls/control_toolbox

