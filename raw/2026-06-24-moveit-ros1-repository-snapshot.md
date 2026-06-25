---
id: "20260624-210038-moveit-ros1-raw"
title: "MoveIt ROS1 repository snapshot"
type: "note"
source: "https://github.com/ros-planning/moveit"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-moveit-ros1-motion-planning-framework.md
---

# MoveIt ROS1 repository snapshot

- Repository: `ros-planning/moveit`
- URL: https://github.com/ros-planning/moveit
- Checked branch: `master`
- Checked HEAD: `a4febda3cce71b7beae48aa69f0a4c2cadebef45`

## README facts

- The README describes MoveIt as the MoveIt Motion Planning Framework for ROS.
- It points ROS 2 users to `moveit/moveit2`.
- It describes MoveIt as an open source robotics manipulation platform for commercial applications, prototyping and benchmarking algorithms.
- Branch policy: latest features on `master`; `*-devel` branches correspond to released and stable versions for specific ROS distributions; `noetic-devel` is synced to `master` at the time of README.
- Buildfarm tables cover MoveIt packages such as `moveit_core`, `moveit_planners`, `moveit_planners_ompl`, `moveit_ros_planning`, `moveit_ros_move_group`, `moveit_servo`, `moveit_msgs` and related packages.

## Local interpretation

This is the ROS1 MoveIt codebase. The knowledge base already contains MoveIt 2, so this page is useful mainly as a ROS1 historical/production baseline and for comparing API/package evolution.

