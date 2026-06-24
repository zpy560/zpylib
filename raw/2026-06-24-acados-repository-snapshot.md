# acados/acados repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/acados/acados
- Clone URL: https://github.com/acados/acados.git
- Default branch observed: `main`
- HEAD commit: `8e1a6f856e063c423de583e03c691e3b2b7fc0a0`
- Source inspection method: raw README from `main` plus `git ls-remote`

## README facts

- acados provides fast embedded solvers for nonlinear optimal control, designed for real-time applications and embedded systems.
- It is written in C and offers Python, MATLAB and Octave interfaces.
- It solves NLPs with optimal control problem structure, used repeatedly in MPC and MHE.
- Features include NMPC, MHE, DAE support, multiple shooting, efficient integration, SQP-type solvers, modular design and solution sensitivities.
- Documentation is at `docs.acados.org`.
- README says it uses tailored QP solvers such as HPIPM and supports CasADi in interfaces.

## Interpretation boundary

- acados is a real-time OCP/NMPC solver toolkit, not a full planning stack.
- It is most relevant when the problem is already formulated as an optimal control problem.

