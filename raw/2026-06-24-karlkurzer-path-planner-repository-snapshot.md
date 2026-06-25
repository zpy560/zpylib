---
id: "20260624-210010-karlkurzer-path-planner-raw"
title: "karlkurzer/path_planner repository snapshot"
type: "note"
source: "https://github.com/karlkurzer/path_planner"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-karlkurzer-path-planner-hybrid-a-star.md
---

# karlkurzer/path_planner repository snapshot

- Repository: `karlkurzer/path_planner`
- URL: https://github.com/karlkurzer/path_planner
- Checked branch: `master`
- Checked HEAD: `ddf1a3afcafc323ef44d5e49d5cbb7b3c3f53665`
- README title: `Hybrid A* Path Planner for the KTH Research Concept Vehicle`

## README facts

- The repository implements a Hybrid A* path planner for autonomous vehicles, developed for the KTH Research Concept Vehicle.
- It targets real-time path planning for a nonholonomic vehicle in unstructured environments.
- The implementation uses C++ with ROS and RViz.
- Key characteristics include 72 headings per cell, 5 degree discretization, constrained and unconstrained heuristics, Dubins shot and roughly 10 Hz C++ implementation.
- Dependencies listed include OMPL and `ros_map_server`.

## Local interpretation

This is one of the clearest small-to-medium Hybrid A* references for vehicle path planning. It is useful for algorithm structure, heuristic design and RViz debug workflow, but it should be treated as research/teaching code rather than a full production planner.

