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
