---
id: "20260624-210006-lanelet2-raw"
title: "Lanelet2 repository snapshot"
type: "note"
source: "https://github.com/fzi-forschungszentrum-informatik/Lanelet2"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-lanelet2-hd-map-routing-framework.md
---

# Lanelet2 repository snapshot

- Repository: `fzi-forschungszentrum-informatik/Lanelet2`
- URL: https://github.com/fzi-forschungszentrum-informatik/Lanelet2
- Checked branch: `master`
- Checked HEAD: `ae39c8d673264afac2339c4f0252df53a7ba82dd`
- README title: `Lanelet2`
- License stated in README: BSD 3-Clause

## README facts

- Lanelet2 is a C++ library for handling map data in automated driving.
- It is designed for high-definition map data and complex traffic scenarios.
- Features include 2D/3D support, lane changes, routing through areas, separated routing for pedestrians/vehicles/bikes, custom traffic rules and routing costs, map IO and Python bindings.
- It supports ROS1, ROS2, Docker and Conan.
- Documentation is split across package docs, Doxygen comments and hosted documentation.

## Local interpretation

Lanelet2 is a planning-enabling infrastructure library. It does not decide behavior by itself, but it defines the map primitives, routing graph, projection and traffic-rule surface that route planning and behavior planning often depend on.

