---
id: "20260624-210022-voxblox-raw"
title: "Voxblox repository snapshot"
type: "note"
source: "https://github.com/ethz-asl/voxblox"
created_at: "2026-06-24"
tags:
  - autonomous-driving
  - planning-control
related:
  - notes/2026-06-24-voxblox-tsdf-esdf-mapping.md
---

# Voxblox repository snapshot

- Repository: `ethz-asl/voxblox`
- URL: https://github.com/ethz-asl/voxblox
- Checked branch: `master`
- Checked HEAD: `c8066b04075d2fee509de295346b1c0b788c4f38`
- README title: `Voxblox`

## README facts

- Voxblox is a volumetric mapping library based mainly on Truncated Signed Distance Fields.
- Features include CPU-only operation, multiple layer types, protobuf serialization, different scan insertion and weighting methods, ROS integration and extensible integrators.
- It includes an implementation for building ESDFs directly from TSDFs.
- The README points planning users to `mav_voxblox_planning`.
- The cited paper is "Voxblox: Incremental 3D Euclidean Signed Distance Fields for On-Board MAV Planning", IROS 2017.

## Local interpretation

Voxblox is planning-adjacent infrastructure: it gives planners a 3D distance field and map representation. For actual planning algorithms, pair it with `mav_voxblox_planning` or other planners that consume ESDFs.

