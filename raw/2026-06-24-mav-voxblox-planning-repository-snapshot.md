---
id: "20260624-211006-mav-voxblox-planning-raw"
title: "mav_voxblox_planning repository snapshot"
type: "note"
source: "https://github.com/ethz-asl/mav_voxblox_planning"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-mav-voxblox-planning-esdf-mav-planners.md
---

# mav_voxblox_planning repository snapshot

- Repository: `ethz-asl/mav_voxblox_planning`
- URL: https://github.com/ethz-asl/mav_voxblox_planning
- Checked branch: `master`
- Checked HEAD: `a90260baaa07cd046847d7a237ab17e2947dbce7`

## README facts

- README describes it as MAV planning tools using Voxblox as the map representation.
- It includes global planning with OMPL planners such as RRT*, RRT Connect, BIT* and PRM.
- It includes planning on skeleton sparse graphs and generation of skeleton sparse graphs from ESDF Voxblox maps.
- It includes path smoothing with velocity ramp, polynomial smoothing and local polynomial optimization.
- It includes local planning that sends timed, dynamically feasible trajectories to a MAV controller and replans online.
- It provides an RViz planning plugin for start/goal interaction and planning requests.

## Local interpretation

This repository is the missing planning counterpart to Voxblox. It directly connects ESDF maps to global planning, local trajectory optimization, smoothing and controller-facing timed trajectories.

