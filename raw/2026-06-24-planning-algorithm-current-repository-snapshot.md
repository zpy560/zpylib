# kushuaiming/planning_algorithm current repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/kushuaiming/planning_algorithm
- Clone URL: https://github.com/kushuaiming/planning_algorithm.git
- Default branch: `master`
- HEAD commit: `e5ce3ffcc04c1c579a9785a42c7d98b27de0a500`
- Prior local knowledge entry: `raw/2026-06-15-planning-algorithm-repository-snapshot.md`

## README facts

- Recommended environment: Ubuntu 20.04 or Ubuntu 18.04, CMake, OpenCV 4 recommended.
- Build commands:

```bash
mkdir build
cd build
cmake ..
make -j10
./a_star
./rrt
```

- Coordinate convention: X positive to the right, Y positive downward.
- README includes a taxonomy of automated driving motion planning techniques:
  - Graph search based planners: Dijkstra, A* family, State Lattices.
  - Sampling based planners: RRT.
  - Interpolating curve planners: line/circle, clothoid, polynomial, Bezier, spline.
  - Numerical optimization approaches.

## Current status relative to prior entry

- `git ls-remote` shows the same HEAD commit as the 2026-06-15 local entry: `e5ce3ffcc04c1c579a9785a42c7d98b27de0a500`.
- No new upstream commit was observed in this refresh.
- The prior local analysis already recorded that the actual source scope is A* and RRT OpenCV demos, much narrower than the README taxonomy.
