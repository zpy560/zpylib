# osqp/osqp repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/osqp/osqp
- Clone URL: https://github.com/osqp/osqp.git
- Default branch observed: `master`
- HEAD commit: `1572ae068e9ce9ca723cf8223548ade1ff7acc29`
- Source inspection method: raw README from `master` plus `git ls-remote`

## README facts

- OSQP is the Operator Splitting Quadratic Program solver.
- It solves QP problems of the form `min 0.5 x'Px + q'x` subject to `l <= Ax <= u`.
- Documentation is available at `osqp.org`.
- README links to GitHub Discussions, issue tracker, citing information and benchmark repository.
- License badge indicates Apache 2.0.

## Interpretation boundary

- OSQP is a QP solver, not a path planner or controller by itself.
- It is useful for MPC, smoothing and convex QP subproblems once the problem is formulated.

