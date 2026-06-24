# ApolloAuto/apollo current repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ApolloAuto/apollo
- Clone URL: https://github.com/ApolloAuto/apollo.git
- Default branch observed: `master`
- HEAD commit: `d53aa3da47a06a08e6d0cd175d5623a34fa0d6aa`
- Prior local knowledge entry: `raw/2026-06-14-apollo-local-repository-snapshot.md`
- Source inspection method: `git ls-remote` plus raw README.

## README facts

- README describes Apollo as a high-performance, flexible architecture for accelerating autonomous vehicle development, testing, and deployment.
- The 2024-11 prerequisite note says the stable Apollo platform upgraded software packages and dependencies:
  - CUDA 11.8 for Nvidia Ada Lovelace GPUs.
  - NVIDIA driver requirement around 520.61.05 and above in the prerequisite section.
  - LibTorch 1.11.0 for arm64, while x86_64 remains 1.7.0.
- README supports Ubuntu 18.04, 20.04, and 22.04.
- README lists Docker CE 19.03+, NVIDIA Container Toolkit, and GPU recommendations.
- README recommends installing versions in order from Apollo 1.0 to the target version for safety and hardware validation.
- README documents the release progression from Apollo 1.0 through 11.0.
- Apollo 11.0 is described as focusing on large-scale deployment of functional autonomous vehicles in high-value scenarios, upgrading perception, localization, planning, and development toolchains.
- README links documents for Installation, Quick Start, Package Management, CyberRT, Localization, Perception, Prediction, Planning, Decider, Control, Hardware Integration, Map acquisition, Apollo Tool, Others, and FAQs.
- README states Apollo is under Apache-2.0.
- README disclaimer says the open source platform contains source code for models, algorithms, and processes, and cybersecurity defense strategy is integrated in commercial/productized deployment.

## Current status relative to prior entry

- `git ls-remote` shows the same `master` HEAD commit as the 2026-06-14 local Apollo entry: `d53aa3da47a06a08e6d0cd175d5623a34fa0d6aa`.
- The latest observed release tag remains `v11.0.0`.
- No new upstream `master` commit was observed in this refresh.
- The prior local static analysis remains valid for the same commit.
