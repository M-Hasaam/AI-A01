# Pac-Man Search — AI2002 Assignment 01

Graph search algorithms and search-problem formulations for the Berkeley Pac-Man framework,
with automated CSV trace logging of every run.

**Course:** Artificial Intelligence (AI2002) &nbsp;·&nbsp; **Language:** Python 3.12

**Team:** Muhammad Hasaam · M Abdullah · Umer

## What's implemented

| Task | Where | Summary |
|---|---|---|
| 1–5. DFS, BFS, UCS, GBFS, A* | `search/search.py` | Graph search using `util.Stack`, `util.Queue` and `util.PriorityQueue` |
| 6. Corners problem | `search/searchAgents.py` | State `(position, visited_corners)`; exact Manhattan corner-tour heuristic |
| 7. Food search | `search/searchAgents.py` | MST + maze-distance `foodHeuristic`; BFS-based `AnyFoodSearchProblem` |
| CSV trace logging | `search/search.py` | One CSV per search run in `search/evidence/` |
| Custom maze | `search/layouts/i243107Search.lay` | Bait corridor that traps GBFS (cost 78) while A* finds the optimum (42) |

## Repository structure

```
AI-A01/
├── assignment/
│   └── Assignment-01.pdf        Assignment specification
└── search/                      Submission project (starter-code layout kept as required)
    ├── search.py                DFS, BFS, UCS, GBFS, A* and the CSV logger
    ├── searchAgents.py          CornersProblem, heuristics, food search agents
    ├── run.py                   Shortcut runner for the common commands
    ├── test_custom_maze.py      Runs all 5 algorithms on the custom maze
    ├── README.txt               Run commands, system specs, autograder results
    ├── layouts/                 Maze layouts, including i243107Search.lay
    ├── evidence/                CSV trace logs for every run
    │   └── screenshots/         Solution screenshots
    ├── docs/                    Report (report.docx) and its generator script
    ├── test_cases/              Autograder test cases
    └── *.py                     Original starter framework (unmodified)
```

## Quick start

```bash
cd search
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python autograder.py            # 26/25
python run.py gbfs custom       # GBFS on the custom maze
```

The full list of run commands is in [search/README.txt](search/README.txt).
