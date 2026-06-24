# ros-navigation/navigation2_dynamic repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ros-navigation/navigation2_dynamic
- Clone URL: https://github.com/ros-navigation/navigation2_dynamic.git
- Default branch: `master`
- HEAD commit: `e1b0d920fa309c7eb072524b00de7ee12e21076e`
- License file observed: `LICENSE`
- Source inspection method: `git ls-remote`, raw README, shallow clone to `/tmp/navigation2-dynamic-snapshot`

## README facts

- Repository title: `navigation2_dynamic`.
- README summary: Nav2's dynamic obstacle detection, tracking, and processing pipelines.

## File tree facts

- `kf_hungarian_tracker/`: Python ROS package for multi-object tracking.
- `nav2_dynamic_msgs/`: ROS messages for dynamic obstacles.
- `kf_hungarian_tracker/kf_hungarian_tracker/kf_hungarian_node.py`
- `kf_hungarian_tracker/kf_hungarian_tracker/obstacle_class.py`
- `kf_hungarian_tracker/config/kf_hungarian.yaml`
- `nav2_dynamic_msgs/msg/Obstacle.msg`
- `nav2_dynamic_msgs/msg/ObstacleArray.msg`

## Tracker README facts

- `kf_hungarian_tracker` implements a multi-object tracker with Kalman filter and Hungarian algorithm.
- Hungarian algorithm associates detections and previously known objects.
- A Kalman filter is maintained for each object to track position and velocity.
- The implementation uses `scipy.optimize.linear_sum_assignment`.
- The default cost function is Euclidean distance between object centers.
- Possible alternative costs include bounding-box IoU.
- Parameters are set in `config/kf_hungarian.yaml`.
- Parameters include `global_frame`, `death_threshold`, `top_down`, Kalman covariance parameters, velocity filter, height filter, and assignment cost filter.

## Message facts

`Obstacle.msg` contains:

- `unique_identifier_msgs/UUID uuid`
- `float32 score`
- `geometry_msgs/Point position`
- `geometry_msgs/Vector3 velocity`
- `geometry_msgs/Vector3 size`
- position and velocity covariance arrays

`ObstacleArray.msg` contains:

- `std_msgs/Header header`
- `Obstacle[] obstacles`
*** Add File: raw/2026-06-24-navigation2-ignition-gazebo-example-repository-snapshot.md
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
*** Add File: raw/2026-06-24-navigation2-ignition-gazebo-turtlebot3-repository-snapshot.md
# Onicc/navigation2_ignition_gazebo_turtlebot3 repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/Onicc/navigation2_ignition_gazebo_turtlebot3
- Clone URL: https://github.com/Onicc/navigation2_ignition_gazebo_turtlebot3.git
- Default branch: `main`
- HEAD commit: `115bcc30b0f5dc6bdfb918df64c94b88cf953657`
- Source inspection method: `git ls-remote` plus raw README

## README facts

- Project title: `navigation2_ignition_gazebo_turtlebot3`.
- It uses Nav2 for navigating a simulated TurtleBot3 in Ignition Gazebo.
- Main launch command:

```bash
ROS_LOCALHOST_ONLY=1 TURTLEBOT3_MODEL=waffle ros2 launch turtlebot3 simulation.launch.py
```

- The launch starts simulation, Nav2, and RViz2 simultaneously.
- `/odom` topic, `odom` frame, and `/odom/tf` are defined in `model.sdf`.
- `base_footprint` transform in the `odom` frame is published through `/odom/tf`.
- `/odom` publishes the transformation of `odom` frame in the `map` frame.
- `ros2 run tf2_tools view_frames` is recommended to inspect TF relations.
- Ignition Gazebo publishes `joint_states`.
- `ros_ign_bridge` translates Ignition topics to ROS 2 topics.
- `robot_state_publisher` consumes translated `joint_states` to compute and publish most TF.
- `/odom/tf` is remapped to `/tf`.
- `nav2_bringup` initiates basic services and configurations.
- Tested with Ignition Gazebo Fortress and ROS 2 Humble.
- Required packages include Navigation2, Nav2 bringup, `ros_ign_gazebo`, and `ros_ign_bridge`.
*** Add File: raw/2026-06-24-navigation2d-example-repository-snapshot.md
# DaikiMaekawa/navigation2d_example repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/DaikiMaekawa/navigation2d_example
- Clone URL: https://github.com/DaikiMaekawa/navigation2d_example.git
- Default branch: `master`
- HEAD commit: `51318f73a8e53a31f67b8ddda8d7e871a474b6dc`
- License: MIT, according to README
- Source inspection method: `git ls-remote` plus raw README

## README facts

- Project title: `navigation2d_example`.
- It is an example for using UTM-30LX with `navigation2d` of ROS node.
- Related article: http://daikimaekawa.github.io/ros/2014/04/20/Navigation2d/
- Dependency install example: `sudo aptitude install ros-<distro>-move-base`.
- Usage command: `roslaunch navigation2d_example move_base.launch`.
- README links an RViz YouTube video.
- Copyright 2013-2014 Daiki Maekawa.
- License: MIT.

## Interpretation boundary

- This is a ROS 1 era example around `move_base`, not ROS 2 Navigation2.
- The repository name uses `navigation2d`, which should not be confused with ROS 2 `navigation2`.
