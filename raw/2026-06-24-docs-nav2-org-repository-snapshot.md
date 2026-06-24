# ros-navigation/docs.nav2.org repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/ros-navigation/docs.nav2.org
- Clone URL: https://github.com/ros-navigation/docs.nav2.org.git
- Default branch observed: `master`
- HEAD commit: `92e92dfa37778eccde54a2d4d57036f34aadc576`
- Documentation site: https://docs.nav2.org/
- Source inspection method: `git ls-remote` plus raw README from `master`

## README facts

- Repository title: `docs.nav2.org`.
- The repository holds the source and configuration files used to generate the Navigation2 documentation website.
- Website URL: https://docs.nav2.org/
- Native build dependencies:
  - `python3-pip`
  - dependencies from `requirements.txt`
- Virtual environment flow:
  - install `python3-pip python3-venv`
  - create and activate `venv`
  - run `pip3 install -r requirements.txt`
- Docker build command uses `Dockerfile` and tags the image as `nav2_docs`.
- Docker documentation build command: `docker run --rm -v $(pwd):/docs nav2_docs make html`.
- Docker autobuild command exposes local port `8000`.
- VS Code Dev Container is supported.
- Local docs build command: `make html`.
- Built HTML entry point: `_build/html/index.html`.
- The README also mentions `sphinx-autobuild` for automatic rebuild and local serving.
- Images, diagrams and videos may have separate copyrights, trademarks and licenses.

## Branch facts

- `master`: `92e92dfa37778eccde54a2d4d57036f34aadc576`
- `gh-pages`: `212edaa5ecbcc6b68a31bd24a49d278093ef8727`
- `features`: `9883341a8b59bbc94c42bc625b9ac6d76c68fa29`

## Interpretation boundary

- This snapshot covers the documentation source repository, not the Navigation2 runtime code.
- The content of the rendered documentation pages was not crawled page by page in this refresh.
