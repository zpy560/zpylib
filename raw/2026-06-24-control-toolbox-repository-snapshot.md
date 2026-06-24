# ethz-adrl/control-toolbox repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ethz-adrl/control-toolbox
- Clone URL: https://github.com/ethz-adrl/control-toolbox.git
- HEAD commit observed: `7d36e42ff665c9f4b6c5f3e4ddce04a0ab41628a`
- Source inspection method: raw README from `master` plus `git ls-remote`

## README facts

- Repository title: Control Toolbox.
- README includes a July 2021 note saying the library is only scarcely maintained.
- It is described as an efficient C++ library for control, estimation, optimization and motion planning in robotics.
- It supports modelling, control, estimation, trajectory optimization and model predictive control.
- Listed optimal control algorithms include single shooting, iLQR/iLQG, multiple-shooting iLQR, GNMS and DMS.
- Listed solver interfaces include IPOPT, SNOPT, HPIPM and a custom Riccati solver.
- It includes automatic differentiation and robotics modelling tools.

## Interpretation boundary

- Control Toolbox is valuable historically and architecturally, but maintenance status must be considered before new dependency adoption.
- It is a robotics control/optimization library, not a complete deployment stack.

