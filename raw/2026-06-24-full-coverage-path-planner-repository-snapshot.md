# nobleo/full_coverage_path_planner repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/nobleo/full_coverage_path_planner
- Clone URL: https://github.com/nobleo/full_coverage_path_planner.git
- Default branch: `master`
- HEAD commit: `113e627b2864e0a69de89185a3bc18f04e98bf1f`
- License: Apache-2.0
- Primary language: C++
- Stars: 670
- Forks: 164
- Open issues: 18
- Last pushed at: 2025-05-27T17:42:44Z
- Repository description: Full coverage path planning provides a move_base_flex plugin that can plan a path that will fully cover a given area.

## README facts

- The package implements a Full Coverage Path Planner using the Backtracking Spiral Algorithm.
- It acts as a global planner plugin for ROS `move_base` / Move Base Flex.
- The user can configure robot radius and tool radius separately.
- The README says the package has been tested under ROS Melodic and Ubuntu 18.04.
- Source build uses a catkin workspace and `catkin_make`.
- Unit tests include basic common-function tests, Spiral STC coverage tests, and a ROS system test with a tracking PID.
- Example launch: `roslaunch full_coverage_path_planner test_full_coverage_path_planner.launch`.
- Runtime starts planning after a 2D navigation goal in RViz.
- The example depends on `mobile_robot_simulator` and `tracking_pid`.
- The `coverage_progress` node publishes `/coverage_grid` and `/coverage_progress`.
- Plugin name: `full_coverage_path_planner/SpiralSTC`.
- Plugin parameters include `robot_radius` for collision checking and `tool_radius` for coverage discretization.
- The project README notes that Nobleo no longer uses this package internally, while contributions are still welcome.

## Repository structure

- `.github/workflows`
- `doc`
- `include/full_coverage_path_planner`
- `maps`
- `nodes`
- `src`
- `test`
- `CMakeLists.txt`
- `LICENSE`
- `README.md`
- `fcpp_plugin.xml`
- `package.xml`

## Upstream reference

- Backtracking Spiral Algorithm reference in README: GONZALEZ, Enrique, et al. BSA: A complete coverage algorithm. Proceedings of the 2005 IEEE International Conference on Robotics and Automation.
