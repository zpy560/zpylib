# xtaci/algorithms repository snapshot

- Snapshot date: 2026-06-24
- Repository: https://github.com/xtaci/algorithms
- Clone URL: https://github.com/xtaci/algorithms.git
- Default branch: `master`
- HEAD commit: `9449b5d50b940508780f980e6686692ab97e8792`
- License: MIT
- Primary language: C++
- Tag observed: `v1.0`
- GitHub API metadata: not captured because anonymous API requests were rate limited.

## README facts

- Project title: Algorithms & Data Structures in C++.
- Goal: classical algorithm implementations.
- Target environment: server side, based on Linux/GCC.
- Stated design: correctness, ease of use and modification.
- Repository convention: one header file per algorithm under `include/`.
- Repository convention: one demo program per algorithm under `src/`.
- Contributions are expected through fork and pull request after programs pass correctness checks.
- Graph output format is Graphviz Dot.

## Implemented algorithm groups from README and file tree

- Basic utilities and math: array shuffle, primality tests, arbitrary integer, random number generator, maximum subarray.
- Containers and data structures: 2D array, bitset, queue, stack, heap, Fibonacci heap, priority queue, linked list, skip list.
- Sorting: bubble, selection, insertion, shell, radix, quicksort, merge sort.
- Trees: binary search tree, AVL, dynamic order statistics, red-black tree, interval tree, trie, suffix tree, B-tree, suffix array.
- Hashing and filters: multiplication hash, hash table, universal hash, perfect hash, Java string hash, FNV-1a, SimHash, Bloom Filter.
- Encoding and digest: SHA-1, MD5, Base64.
- Graph algorithms: SCC, Prim MST, Kruskal MST, BFS, DFS, Dijkstra, Bellman-Ford, Edmonds-Karp, Push-Relabel.
- Other algorithms: Huffman coding, word segmentation, A*, K-Means, KMP, disjoint-set, 8-queen, palindrome, LCA by binary lifting.

## Repository structure

- `include/`: header-only algorithm implementations.
- `src/`: demo programs, one demo per algorithm in most cases.
- `msvc/`: MSVC compatibility files.
- `utils/`: byte order and encoding helpers.
- `CMakeLists.txt`, `Makefile`, `.travis.yml`: build and CI-related files.

## Local inspection notes

- A shallow clone was used only to inspect file structure and HEAD.
- The repository contains many single-header implementations and matching demos, but no evidence was collected here for modern C++ style, sanitizer coverage, fuzzing, or formal tests.
