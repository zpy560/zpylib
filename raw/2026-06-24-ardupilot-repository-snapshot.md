---
id: "20260624-210002-ardupilot-raw"
title: "ArduPilot repository snapshot"
type: "note"
source: "https://github.com/ArduPilot/ardupilot"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-ardupilot-autopilot-control-stack.md
---

# ArduPilot repository snapshot

- Repository: `ArduPilot/ardupilot`
- URL: https://github.com/ArduPilot/ardupilot
- Checked branch: `master`
- Checked HEAD: `870733136072f80c4a4ab7d8e3f598f07eb47a49`
- README title: `ArduPilot Project`
- License stated in README: GNU GPL v3

## README facts

- ArduPilot describes itself as open source autopilot software.
- It supports multiple vehicle families, including conventional airplanes, quad planes, multi-rotors, helicopters, rovers, boats, balance bots and submarines.
- The project is split into vehicle applications such as ArduCopter, ArduPlane, Rover, ArduSub and Antenna Tracker.
- The repository exposes developer information through the ArduPilot developer wiki, discussion forums and Discord.
- CI badges cover SITL and build tests for Copter, Plane, Rover, Sub, Tracker, AP_Periph, ChibiOS, Linux SBC and replay.

## Local interpretation

This is not a single planning algorithm repository. It is a full autopilot stack with vehicle-specific control, navigation, mission execution, simulation and hardware support. For planning/control study, its value is in how a mature open source autopilot connects guidance, mode logic, state estimation, actuator outputs and vehicle-specific constraints.

