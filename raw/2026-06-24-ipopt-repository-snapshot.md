# coin-or/Ipopt repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/coin-or/Ipopt
- Clone URL: https://github.com/coin-or/Ipopt.git
- HEAD commit observed: `72a29c9aab198afa0dbb940339022a22c415a4eb`
- Source inspection method: raw README plus `git ls-remote`

## README facts

- Ipopt stands for Interior Point OPTimizer.
- It is a software package for large-scale nonlinear optimization.
- It solves problems with nonlinear objective and constraints with lower/upper bounds on constraints and variables.
- Functions can be nonlinear and nonconvex but should be twice continuously differentiable.
- Ipopt is part of COIN-OR and is written in C++.
- It is released under the Eclipse Public License.
- Dependencies include sparse linear solvers such as HSL, Pardiso, SPRAL, MUMPS or WSMP, plus BLAS/LAPACK.

## Interpretation boundary

- Ipopt is a local nonlinear optimizer, not a global optimizer and not a planning framework.
- It is useful when a trajectory optimization or MPC problem is formulated as smooth NLP.

