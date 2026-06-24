# ros2-gbp/navigation2-release repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ros2-gbp/navigation2-release
- Clone URL: https://github.com/ros2-gbp/navigation2-release.git
- Default branch observed: `master`
- HEAD commit: `48c11ee63a39eafbec6d4754f4a414a7fc4ca007`
- GitHub description: Bloom Release Repository for the Navigation2 Metapackage https://github.com/ros-planning/navigation2
- GitHub observed counts: 314 commits, 6 stars, 4 forks
- Source inspection method: GitHub page, raw `README.md`, raw `tracks.yaml`, and `git ls-remote`

## Repository role

- This is a Bloom release repository for the Navigation2 metapackage.
- It is not the Navigation2 runtime source repository.
- The upstream repository recorded in release metadata is `https://github.com/ros-planning/navigation2.git`.
- The release repository records generated Debian/RPM release branches, upstream tarball tags, and Bloom release history.

## Top-level files

- `README.md`: generated release history entries.
- `tracks.yaml`: Bloom track configuration for ROS distributions.

## Current track facts from `tracks.yaml`

| ROS distro | devel branch | last version |
|---|---|---:|
| bouncy | null | 0.1.0 |
| crystal | crystal-devel | 0.1.7 |
| dashing | dashing-devel | 0.2.6 |
| eloquent | eloquent-devel | 0.3.5 |
| foxy | foxy-devel | 0.4.7 |
| galactic | galactic | 1.0.12 |
| humble | humble | 1.1.20 |
| iron | iron | 1.2.10 |
| jazzy | jazzy | 1.3.12 |
| kilted | kilted | 1.4.2 |

Common track settings:

- `name`: `navigation2`
- `vcs_type`: `git`
- `vcs_uri`: `https://github.com/ros-planning/navigation2.git`
- `release_tag`: `:{version}`
- `version`: `:{auto}`
- tracks generate `rosrelease`, `rosdebian`, and `rosrpm` outputs.
- later tracks include Ubuntu/Debian package generation plus Fedora/RHEL RPM generation.

## Latest README entries observed

### jazzy 1.3.12-1

- Release command: `/usr/bin/bloom-release navigation2 --rosdistro jazzy --track jazzy`
- Release time: `Wed, 29 Apr 2026 23:41:21 -0000`
- rosdistro version: `1.3.11-1`
- old version: `1.3.11-1`
- new version: `1.3.12-1`
- Tool versions: bloom `0.13.0`, catkin_pkg `1.1.0`, rosdep `0.26.0`, rosdistro `1.0.1`, vcstools `0.1.42`

### humble 1.1.20-1

- Release command: `/usr/bin/bloom-release navigation2 --ros-distro humble --track humble`
- Release time: `Mon, 17 Nov 2025 18:02:06 -0000`
- rosdistro version: `1.1.19-1`
- old version: `1.1.19-1`
- new version: `1.1.20-1`

### kilted 1.4.2-1

- Release command: `/usr/bin/bloom-release navigation2 --track kilted --rosdistro kilted`
- Release time: `Sat, 20 Sep 2025 00:26:56 -0000`
- rosdistro version: `1.4.1-1`
- old version: `1.4.1-1`
- new version: `1.4.2-1`
- release repository in this entry: `https://github.com/ros2-gbp/navigation2-release.git`

## Package set in recent jazzy/kilted releases

- `costmap_queue`
- `dwb_core`
- `dwb_critics`
- `dwb_msgs`
- `dwb_plugins`
- `nav2_amcl`
- `nav2_behavior_tree`
- `nav2_behaviors`
- `nav2_bringup`
- `nav2_bt_navigator`
- `nav2_collision_monitor`
- `nav2_common`
- `nav2_constrained_smoother`
- `nav2_controller`
- `nav2_core`
- `nav2_costmap_2d`
- `nav2_dwb_controller`
- `nav2_graceful_controller`
- `nav2_lifecycle_manager`
- `nav2_loopback_sim`
- `nav2_map_server`
- `nav2_mppi_controller`
- `nav2_msgs`
- `nav2_navfn_planner`
- `nav2_planner`
- `nav2_regulated_pure_pursuit_controller`
- `nav2_rotation_shim_controller`
- `nav2_route`
- `nav2_rviz_plugins`
- `nav2_simple_commander`
- `nav2_smac_planner`
- `nav2_smoother`
- `nav2_system_tests`
- `nav2_theta_star_planner`
- `nav2_util`
- `nav2_velocity_smoother`
- `nav2_voxel_grid`
- `nav2_waypoint_follower`
- `nav_2d_msgs`
- `nav_2d_utils`
- `navigation2`
- `opennav_docking`
- `opennav_docking_bt`
- `opennav_docking_core`

## Remote ref facts

- `HEAD`: `48c11ee63a39eafbec6d4754f4a414a7fc4ca007`
- `refs/tags/upstream/1.1.20`: `8fed2c851be70f7faba9e7408483f2fda45bc864`
- `refs/tags/upstream/1.3.12`: `d737b2a5d1dd7b2515a66e6cdd4f5bd023251353`
- `refs/tags/upstream/1.4.2`: `8e3b60cf49eb67863fa876831cfac15a833127be`
- `git ls-remote` returned thousands of generated package branches and tags, including `debian/*`, `release/*`, `rpm/*`, and `upstream/*`.

## Interpretation boundary

- This snapshot records packaging and release metadata, not Nav2 algorithm implementation.
- For source-level behavior, use the Navigation2 upstream repository and match it to the ROS distro/version recorded here.
- For installed binary behavior, this release repository is useful evidence of what package version entered each ROS distribution.

