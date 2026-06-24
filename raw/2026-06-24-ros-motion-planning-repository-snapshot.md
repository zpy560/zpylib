# ai-winter/ros_motion_planning repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ai-winter/ros_motion_planning
- Clone URL: https://github.com/ai-winter/ros_motion_planning.git
- Default branch: `dev`
- HEAD commit: `a6f21b0e7a5aa714bab204289f7a4835b2148fa4`
- License: GPL-3.0
- Primary language: C++
- Stars: 3529
- Forks: 516
- Open issues: 8
- Last pushed at: 2026-04-24T14:49:10Z
- Repository description: Motion planning and Navigation of AGV/AMR: ROS planner plugin implementation of A*, JPS, D*, LPA*, D* Lite, Theta*, RRT, RRT*, RRT-Connect, Informed RRT*, ACO, PSO, Voronoi, PID, LQR, MPC, DWA, APF, Pure Pursuit etc.

## README facts

- Robot motion planning is described as path searching plus trajectory optimization.
- The repository provides common motion planning algorithm implementations.
- The README points to Python and MATLAB versions.
- Quick start is tested on Ubuntu 20.04 LTS with ROS Noetic.
- Dependencies include ROS Noetic packages such as `amcl`, `base_local_planner`, `map_server`, `move_base`, `navfn`, and `libgoogle-glog-dev`.
- Build script: `scripts/build.sh`.
- Runtime script: `scripts/main.sh`.
- The README warns that launch files are regenerated from `src/user_config/user_config.yaml`; users should modify YAML rather than generated launch files.
- Multi-agent simulation is supported through `goal_publisher.py`.

## File structure from README

```text
ros_motion_planner
├── 3rd
├── docs
├── docker
├── assets
├── scripts
└── src
    ├── core
    │   ├── common
    │   ├── path_planner
    │   └── controller
    ├── sim_env
    ├── plugins
    └── user_config
```

## Algorithm scope in README

- Global planners: GBFS, Dijkstra, A*, JPS, D*, LPA*, D* Lite, Voronoi, Theta*, Lazy Theta*, S-Theta*, Hybrid A*, RRT, RRT*, Informed RRT, RRT-Connect, ACO, GA, PSO.
- Local planners: PID, LQR, DWA, APF, RPP, MPC; TEB and Lattice are marked as development items in the README.
- Curve generation: Polynomial, Bezier, Cubic Spline, BSpline, Dubins, Reeds-Shepp.
- Related tools: pedestrian simulation plugin and RViz path visualization plugins.

## Current project topics from GitHub

- `artificial-potential-field`
- `astar`
- `autonomous-vehicles`
- `dstar-lite`
- `jump-point-search`
- `lpa-star`
- `model-predictive-control`
- `motion-planning`
- `path-planning`
- `path-tracking`
- `pure-pursuit`
- `robotics`
- `ros`
- `ros-navigation`
- `rrt`
- `rrt-star`
- `trajectory-planning`
- `voronoi`
