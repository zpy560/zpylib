---
id: "20260624-211019-mc-rtc-note"
title: "mc_rtc：机器人控制框架与接口层"
type: "note"
source: "raw/2026-06-24-mc-rtc-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - wiki/2026-06-24-mc-rtc.md
---

# mc_rtc：机器人控制框架与接口层

## 结论

`mc_rtc` 是控制框架资料，不是规划算法库。它的价值在于控制器插件化、机器人状态输入、命令输出、仿真/实机接口和多机器人控制工程组织方式。

## 事实摘录

- 远端仓库：`jrl-umi3218/mc_rtc`
- 当前核对 HEAD：`c09df00517a18f53236ce4b66599e9e6b68e3c08`
- README 定位：interface for simulation and robot control systems。
- 系统输入机器人状态，`mc_rtc` 输出期望机器人状态命令。
- `MCGlobalController` 持有并委托 `MCController` 派生控制器执行控制。
- 提供 ROS、OpenRTM、UDP、VREP、NAOqi、Franka、MuJoCo 等接口。

## 对规划控制的意义

- 适合研究控制器框架如何跨仿真和实机复用。
- 与 TSID、Pinocchio、RBDyn/Tasks 结合，可以理解全身控制工程链。
- 对自动驾驶底盘控制不是直接参考，但对机器人控制架构很有价值。

## 使用建议

如果目标是学控制算法，先看 TSID/Tasks/Pinocchio；如果目标是做控制框架和接口层，读 `mc_rtc` 的 controller lifecycle、robot module 和接口包。

