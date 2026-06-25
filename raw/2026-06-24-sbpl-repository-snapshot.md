---
id: "20260624-211010-sbpl-raw"
title: "SBPL repository snapshot"
type: "note"
source: "https://github.com/sbpl/sbpl"
created_at: "2026-06-24"
tags:
  - planning-control
  - tools
related:
  - notes/2026-06-24-sbpl-search-based-planning-library.md
---

# SBPL repository snapshot

- Repository: `sbpl/sbpl`
- URL: https://github.com/sbpl/sbpl
- Checked branch: `master`
- Checked HEAD: `4d654845aa3b92aa1b4282a342e9011bac95aeb9`
- Source inspected: `README.txt` from shallow clone

## README facts

- SBPL is available as a standalone software library.
- SBPL itself has no dependencies other than the C/C++ standard library.
- It can be built with CMake.
- Examples are in `src/test/main.cpp`.
- Planning problem examples are stored as ASCII `.cfg` files in `env_examples`.
- Example environments include 2D, xytheta and robot arm examples.
- Motion primitive files are in `matlab/mprim`.
- README links to `sbpl.net`, ROS wiki `sbpl`, and `sbpl_lattice_planner`.

## Source tree facts

- Planner source files include `araplanner.cpp`, `adplanner.cpp`, `rstarplanner.cpp`, `mhaplanner.cpp`, `ANAplanner.cpp`, `lazyARA.cpp`, `ppcpplanner.cpp` and `viplanner.cpp`.
- Environment files include `environment_nav2D`, `environment_navxythetalat`, `environment_navxythetamlevlat` and `environment_robarm`.

## Local interpretation

SBPL is a core reference for search-based planning and lattice planning. It is older but conceptually important for anytime search, heuristic planning and motion primitives.

