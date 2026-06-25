---
id: "20260624-211018-mc-rtc-raw"
title: "mc_rtc repository snapshot"
type: "note"
source: "https://github.com/jrl-umi3218/mc_rtc"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-mc-rtc-robot-control-framework.md
---

# mc_rtc repository snapshot

- Repository: `jrl-umi3218/mc_rtc`
- URL: https://github.com/jrl-umi3218/mc_rtc
- Checked branch: `master`
- Checked HEAD: `c09df00517a18f53236ce4b66599e9e6b68e3c08`
- README title: `mc_rtc`
- License badge: BSD 2-Clause

## README facts

- `mc_rtc` is an interface for simulation and robot control systems.
- A system provides robot state such as joint values and sensor readings; `mc_rtc` returns desired robot state commands.
- `mc_control::MCGlobalController` delegates control to held `mc_control::MCController` objects.
- Controllers are written by inheriting from `mc_control::MCController`.
- It is a superset of SpaceVecAlg, RBDyn and Tasks libraries.
- Interfaces are available for ROS, OpenRTM, UDP, VREP, NAOqi, Franka and MuJoCo.

## Local interpretation

mc_rtc is a control framework rather than a planner. It is important for understanding how whole-body or task controllers are packaged, switched and connected to robot/simulator interfaces.

