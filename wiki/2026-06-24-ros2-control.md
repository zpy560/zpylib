---
id: "20260624-ros2-control"
title: "ros2_control"
type: "entity"
source: "https://github.com/ros-controls/ros2_control.git"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
  - architecture
  - programming
  - tools
related:
  - notes/2026-06-24-ros2-control-hardware-controller-framework.md
  - wiki/2026-06-24-ros2-controllers.md
  - wiki/2026-06-13-navigation2.md
  - wiki/2026-06-14-autoware.md
---

# ros2_control

## 基本信息

- 类型：ROS 2 硬件抽象与控制器管理框架
- 官方仓库：https://github.com/ros-controls/ros2_control.git
- 官方文档：https://control.ros.org/
- 默认分支：`master`
- 主要发行版分支：`humble`、`jazzy`、`kilted`
- 快照提交：`4f9692862234f260684fa27d04ff5b773fa1ef76`
- 最后提交时间：2026-06-22
- 最后提交标题：`Bump actions/checkout from 6 to 7 (#3402)`
- 当前包版本：`6.7.1`
- 主要语言：C++、Python、reStructuredText、YAML
- 主要机制：Controller Manager、Resource Manager、hardware plugin、controller plugin、Lifecycle、pluginlib、Command/State Interface
- 分析方式：静态源码、文档、消息服务和 CI 分析；未编译运行

## 当前判断

ros2_control 是 ROS 2 执行层控制框架，价值在硬件抽象、资源管理、控制器生命周期和实时主循环，而不是具体控制算法。它适合作为机器人底盘、机械臂和执行器控制的基础设施；用于自动驾驶时，应把它理解为靠近车辆接口的执行层机制，不是规划、决策或功能安全系统。

## 架构总览

```text
robot_description / <ros2_control>
→ Resource Manager
→ hardware plugins
→ state interfaces
→ controller update
→ command interfaces
→ hardware write
```

控制线程按固定周期执行：

```text
read hardware
→ update active controllers
→ write hardware
```

## 核心包

- `controller_manager`：主入口和控制器/硬件生命周期管理。
- `hardware_interface`：Actuator、Sensor、System 抽象和 Resource Manager。
- `controller_interface`：Controller 和 Chainable Controller 基类。
- `controller_manager_msgs`：加载、配置、切换、查询控制器和硬件的服务消息。
- `joint_limits`：命令限制基础设施。
- `transmission_interface`：actuator/joint 空间传动关系。
- `ros2controlcli`：`ros2 control` CLI。
- `rqt_controller_manager`：图形前端。

## 关键机制

### 资源声明与借用

Controller 声明需要哪些 state/command interface。Resource Manager 管理接口是否 available、是否 claimed，避免多个控制器同时抢占同一硬件命令接口。

### 硬件生命周期

硬件组件有 `UNCONFIGURED`、`INACTIVE`、`ACTIVE`、`FINALIZED` 等状态。`ACTIVE` 才表示硬件可运动并接收命令。错误处理通过 `on_error` 和 lifecycle 转换完成。

### 控制器切换

`SwitchController` 支持 `STRICT`、`BEST_EFFORT`、`AUTO`、`FORCE_AUTO`。复杂系统中可以让 Controller Manager 根据链式控制依赖和接口互斥关系辅助处理切换。

### 串级控制

Chainable controller 可以导出 reference/state interface，让上层控制器接入下层控制器输入。适合 position tracking、diff drive、wheel PID 等层级控制组合。

### 实时运行

`ros2_control_node` 会尝试配置 `SCHED_FIFO`、内存锁定、CPU affinity 和 overrun 检测。但实时性仍取决于系统内核、权限、硬件驱动和控制器实现。

## 与现有知识库条目的关系

### 与 Navigation2

Navigation2 负责导航任务、规划、局部控制和安全后处理，通常输出 `cmd_vel` 或导航动作结果。ros2_control 更靠近底盘执行层，负责把控制器和硬件接口规范化。二者不是替代关系。

### 与 Autoware

Autoware 关注开放道路自动驾驶的感知、规划、控制命令、门控和车辆接口。ros2_control 可以作为 ROS 2 控制执行层参考，但乘用车自动驾驶仍需要 Autoware/Apollo 这类系统中的模式管理、命令门控、AEB、MRM 和车辆接口安全策略。

## 工程边界

- 不提供完整自动驾驶规划控制栈。
- 具体控制算法主要在 `ros2_controllers` 等下游仓库。
- 使用实时调度不等于达到硬实时。
- 硬件 `read/write` 阻塞会直接破坏控制周期。
- INACTIVE 状态下命令接口安全语义仍需要部署侧保证。
- Controller switch、fallback 和 chained controllers 必须实测。
- 必须按 ROS 发行版选择对应分支。

## 最值得学习

- 执行层如何用接口资源管理防止命令冲突。
- 硬件生命周期如何与控制器生命周期解耦。
- `read → update → write` 主循环如何组织。
- controller plugin 和 hardware plugin 如何通过 pluginlib 接入。
- controller chaining 如何表达串级控制。
- CLI 和 service 如何暴露运行时可观测性。

## 关联笔记

- `notes/2026-06-24-ros2-control-hardware-controller-framework.md`
- `wiki/2026-06-24-ros2-controllers.md`
- `wiki/2026-06-13-navigation2.md`
- `wiki/2026-06-14-autoware.md`

## 更新记录

- 2026-06-24：基于 `master` 分支提交 `4f96928` 完成 Controller Manager、Resource Manager、hardware interface、controller interface、实时主循环和工程边界建档。
- 2026-06-24：增加 ros2_controllers 通用控制器插件集合关联。
