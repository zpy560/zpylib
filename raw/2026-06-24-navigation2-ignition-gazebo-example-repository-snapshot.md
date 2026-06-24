# art-e-fact/navigation2_ignition_gazebo_example repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/art-e-fact/navigation2_ignition_gazebo_example
- Clone URL: https://github.com/art-e-fact/navigation2_ignition_gazebo_example.git
- Default branch observed: `main`
- HEAD commit: `26b1d74431d2d6130d23880a5f40416abfe4cfc7`
- Source inspection method: `git ls-remote` plus raw README

## README facts

- Project title: Navigation2 (Ignition) Gazebo Example.
- It is a minimal ROS 2 project to use Navigation2 with Ignition Gazebo.
- It is based on the official Gazebo Classic Navigation2 tutorial and sample code.
- Requirements:
  - ROS 2 Humble
  - Gazebo Fortress
  - Navigation2
- Setup installs `ros-humble-navigation2` and `ros-humble-nav2-bringup`.
- Source dependencies are imported with `vcs import --input deps.repos src`.
- Build uses `colcon build`.
- Main launch command: `ros2 launch sam_bot_nav2_gz complete_navigation.launch.py`.
- Example runners:
  - `ros2 run sam_bot_nav2_gz follow_waypoints.py`
  - `ros2 run sam_bot_nav2_gz reach_goal.py`
- Launch tests:
  - `test_bringup.launch.py`
  - `test_reach_goal.launch.py`
  - `test_follow_waypoints.launch.py`
- Artefacts CI is supported.
- Rerun.io visualization is mentioned as experimental.
