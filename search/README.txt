==============================================================================
                    PAC-MAN SEARCH PROJECT - README
==============================================================================

Python Version: 3.12.10
OS: Microsoft Windows 11 Pro (build 26200), 64-bit
CPU: AMD Ryzen 7 7735U with Radeon Graphics (8 cores / 16 threads)
RAM: 32 GB

==============================================================================
FILES MODIFIED:
==============================================================================

1. search.py
   - Implemented: DFS, BFS, UCS, GBFS (Greedy Best-First Search), A* Search
   - Added: CSVLogger class for automated trace logging to evidence/ directory
   - All algorithms produce CSV trace files with columns:
     iteration, expanded_state, parent, action, generated_successors,
     frontier_before, frontier_after, explored, g, h, f

2. searchAgents.py
   - Implemented: CornersProblem (state space formulation with visited corners)
   - Implemented: cornersHeuristic (exact shortest Manhattan tour over unvisited
     corners; admissible and consistent)
   - Implemented: foodHeuristic (maze distance to nearest food + MST weight over
     remaining food, maze distances via cached BFS; trickySearch: 255 nodes)
   - Implemented: AnyFoodSearchProblem.isGoalState (food position check)
   - Implemented: ClosestDotSearchAgent.findPathToClosestDot (via BFS)

3. layouts/i243107Search.lay
   - Custom maze with multiple dead ends, decision branches, and a deceptive
     bait corridor aimed at the food. GBFS takes the bait (cost 78) while
     BFS, UCS and A* find the optimal path (cost 42).

==============================================================================
RUN COMMANDS:
==============================================================================

--- Task 1: Depth-First Search (DFS) ---
python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs

--- Task 2: Breadth-First Search (BFS) ---
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=bfs

--- Task 3: Uniform-Cost Search (UCS) ---
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
Note: the mediumDenselyMaze and stayEastSearch layouts named in the assignment
are not included in the starter layouts/, so mediumDottedMaze with
StayEastSearchAgent / StayWestSearchAgent is used to test varying step costs.
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

--- Task 4: Greedy Best-First Search (GBFS) ---
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=gbfs,heuristic=manhattanHeuristic

--- Task 5: A* Search ---
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=nullHeuristic
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

--- Task 6: Corners Problem ---
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p AStarCornersAgent -z .5

--- Task 7: Food Search ---
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

--- Custom Maze ---
python pacman.py -l i243107Search -p SearchAgent -a fn=dfs
python pacman.py -l i243107Search -p SearchAgent -a fn=bfs
python pacman.py -l i243107Search -p SearchAgent -a fn=ucs
python pacman.py -l i243107Search -p SearchAgent -a fn=gbfs,heuristic=manhattanHeuristic
python pacman.py -l i243107Search -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

--- Run All Autograder Tests ---
python autograder.py

--- Helper Utility Script (run.py) ---
For convenience, a custom `run.py` script is included to quickly execute tests dynamically.
Usage: python run.py [algorithm] [layout] [--fast]

[algorithm] options: dfs, bfs, ucs, gbfs, astar
[layout] shortcuts: tiny, medium, big, custom (defaults to mediumMaze)

Examples:
python run.py dfs               (Runs DFS on mediumMaze)
python run.py bfs big           (Runs BFS on bigMaze)
python run.py astar custom      (Runs A* on i243107Search)

Other Tasks:
python run.py task6-tiny        (Runs Corners Problem on tinyCorners)
python run.py task6-medium      (Runs Corners Problem on mediumCorners)
python run.py task7             (Runs Food Search on trickySearch)
python run.py task8             (Runs Closest Dot Agent on bigSearch)
python run.py all               (Runs autograder.py)

* Add --fast to any command to skip GUI animations.

==============================================================================
AUTOGRADER RESULTS: 26/25 (100% + 1 extra credit)
==============================================================================
Question q1 (DFS):              3/3
Question q2 (BFS):              3/3
Question q3 (UCS):              3/3
Question q4 (A*):               3/3
Question q5 (CornersProblem):   3/3
Question q6 (cornersHeuristic): 3/3
Question q7 (foodHeuristic):    5/4  (extra credit: 255 nodes on trickySearch)
Question q8 (closestDot):       3/3
                              ------
Total:                         26/25
==============================================================================
