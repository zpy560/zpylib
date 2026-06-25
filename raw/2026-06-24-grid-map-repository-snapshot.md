---
id: "20260624-210030-grid-map-raw"
title: "grid_map repository snapshot"
type: "note"
source: "https://github.com/ANYbotics/grid_map"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-grid-map-multilayer-robot-map.md
---

# grid_map repository snapshot

- Repository: `ANYbotics/grid_map`
- Alternate fetched repository: `leggedrobotics/grid_map`
- URL: https://github.com/ANYbotics/grid_map
- Checked branch: `master`
- Checked HEAD: `515e3d815296635ac2420dd8d6a0350e0bdc4ab4`
- README title: `Grid Map`
- License stated in README: BSD 3-Clause

## README facts

- Grid Map is a C++ library with ROS interface for two-dimensional grid maps with multiple data layers.
- It is designed for mobile robotic mapping with data such as elevation, variance, color, friction coefficient, foothold quality, surface normal and traversability.
- It is used in Robot-Centric Elevation Mapping for rough terrain navigation.
- Features include multi-layered 2.5D grid mapping, circular-buffer map repositioning, Eigen storage, iterators, ROS conversions, OpenCV conversion, RViz visualization and filter chains.
- README explicitly says this is research code and disclaims fitness for a particular purpose.

## Local interpretation

Grid Map is valuable for planning because many planners do not consume raw point clouds directly; they consume layered terrain/cost/traversability maps. It is especially relevant for rough terrain, legged robotics and local navigation cost construction.

