# autowarefoundation/autoware repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/autowarefoundation/autoware
- Clone URL: https://github.com/autowarefoundation/autoware.git
- Default branch observed: `main`
- HEAD commit: `4847819760656247343dfb995ea8e151fc3d9b00`
- License: Apache-2.0
- Current tag list observed up to: `1.8.0`
- Source inspection method: shallow clone to `/tmp/autoware-snapshot`

## README facts

- README describes Autoware as an open-source autonomous driving framework.
- README states that Autoware provides a comprehensive, production-ready software stack for accelerating commercial autonomous vehicle deployment across diverse platforms and use cases.
- README points new users to the official installation guide and quick-start demos.
- README points developers to the Autoware documentation site and the `autowarefoundation/autoware-documentation` source repository.
- README links contribution guidelines, working groups, Q&A discussions, Autoware Foundation homepage, support guidelines, CI metrics, health-check CI, and Codecov for Autoware Universe.

## Source layout facts

- The `autoware` repository is a meta-repository and does not contain the full Autoware source code.
- `src/README.md` states that source repositories are managed through manifest files under `repositories/`.
- Essential source checkout command:

```bash
vcs import src < repositories/autoware.repos
```

- Top-level repository files include `README.md`, `LICENSE`, `NOTICE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `DISCLAIMER.md`, `setup-dev-env.sh`, `docker/`, `ansible/`, `repositories/`, and `src/`.

## Manifest facts from `repositories/autoware.repos`

- Core:
  - `agnocast`: `2.3.5`
  - `autoware_msgs`: `1.13.0`
  - `autoware_adapi_msgs`: `1.9.1`
  - `autoware_internal_msgs`: `1.12.1`
  - `autoware_cmake`: `1.2.0`
  - `autoware_utils`: `1.8.0`
  - `autoware_lanelet2_extension`: `1.1.0`
  - `autoware_core`: `1.8.0`
  - `autoware_rviz_plugins`: `0.5.0`
  - `autoware_system_designer`: `v0.4.1`
  - `rviz_2d_overlay_plugins`: `1.4.0`
- Universe:
  - `autoware_universe`: `0.51.0`
  - `tier4_autoware_msgs`: `v0.58.0`
  - `morai_msgs`: `e2e75fc1603a9798773e467a679edf68b448e705`
  - `muSSP`: `c79e98fd5e658f4f90c06d93472faa977bc873b9`
  - `pointcloud_to_laserscan`: `d969ec699f84fad827fbadfa3001c9c657482fbe`
  - `eagleye`: `575136ebba99892946d36d8398f228aee2136af0`
  - `rtklib_ros_bridge`: `ef094407bba4f475a8032972e0c60cbb939b51b8`
  - `llh_converter`: `4fc2a2e1bc9dcf3e6ab0a8085d8257168e160342`
  - `glog`: `ea36766fdc2ac8e8c8e3ac988ae69acd6d09bb30`
  - `bevdet_vendor`: `0.1.0`
  - `trt_batched_nms`: `0.1.0`
  - `cuda_blackboard`: `0.4.0`
  - `negotiated`: `eac198b55dcd052af5988f0f174902913c5f20e7`
  - `managed_transform_buffer`: `0.2.0`
- Launcher:
  - `autoware_launch`: `0.51.0`
- Sensor components:
  - `sensor_component_description`: `03ba094851ec90febfcfc0adb20b64b0e19df7a8`
  - `nebula`: `v1.1.0`
  - `sync_tooling_msgs`: `v0.2.10`
  - `transport_drivers`: `39ebd8afe1bb9760a6cd6272e428468480f6de90`
  - `ros2_socketcan`: `e39a814180b03f00a5692b6951a5d4e9f0463486`

## Current interpretation boundary

- This snapshot did not recursively import all source repositories.
- Any implementation-level judgment must still inspect the pinned `autoware_core`, `autoware_universe`, `autoware_launch`, message, sensor, and external repositories.
