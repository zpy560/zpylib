---
id: "20260624-210003-ardupilot-note"
title: "ArduPilot：多载具开源飞控与控制栈"
type: "note"
source: "raw/2026-06-24-ardupilot-repository-snapshot.md"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - wiki/2026-06-24-ardupilot.md
---

# ArduPilot：多载具开源飞控与控制栈

## 结论

ArduPilot 值得入库，但它不是“路径规划算法库”，而是覆盖多旋翼、固定翼、车、船、潜航器等平台的完整开源 autopilot。对控制和规划知识库的价值在于观察成熟系统如何把任务、模式、制导、控制、仿真测试和硬件抽象组织成可长期演进的工程栈。

## 事实摘录

- 远端仓库：`ArduPilot/ardupilot`
- 当前核对 HEAD：`870733136072f80c4a4ab7d8e3f598f07eb47a49`
- README 声称支持 airplanes、quad planes、multi-rotors、helicopters、rovers、boats、balance bots、submarines 等多类载具。
- 子项目包含 ArduCopter、ArduPlane、Rover、ArduSub、Antenna Tracker。
- README 声明项目许可证为 GNU GPL v3。

## 对规划控制的意义

- 适合研究飞控软件中的控制分层、任务模式、failsafe 与 vehicle-specific 约束。
- 适合对比 PX4，理解两套开源飞控在模块组织、开发文化和车辆覆盖面的差异。
- 不适合作为“抽一个 planner 直接复用”的资料入口，学习成本应按完整系统评估。

## 使用建议

优先从目标载具目录和开发者 wiki 切入。例如无人车相关先看 `Rover`，多旋翼控制先看 `ArduCopter`。如果目标是自动驾驶地面车路径规划，应把它作为控制执行和系统集成参考，而不是替代 Apollo、Autoware、Nav2 或 Hybrid A* 类规划仓库。

