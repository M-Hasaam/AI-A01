==============================================================================
                    PAC-MAN SEARCH PROJECT - README
==============================================================================

Python Version: 3.12.10
OS: Windows 11

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
   - Implemented: cornersHeuristic (greedy nearest-unvisited-corner Manhattan)
   - Implemented: foodHeuristic (max Manhattan distance + pairwise food distances)
   - Implemented: AnyFoodSearchProblem.isGoalState (food position check)
   - Implemented: ClosestDotSearchAgent.findPathToClosestDot (via BFS)

3. layouts/CustomSearch.lay
   - Custom maze with multiple dead ends, decision branches, and deceptive
     corridors designed to highlight differences between GBFS and A*.

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
python pacman.py -l CustomSearch -p SearchAgent -a fn=dfs
python pacman.py -l CustomSearch -p SearchAgent -a fn=bfs
python pacman.py -l CustomSearch -p SearchAgent -a fn=ucs
python pacman.py -l CustomSearch -p SearchAgent -a fn=gbfs,heuristic=manhattanHeuristic
python pacman.py -l CustomSearch -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

--- Run All Autograder Tests ---
python autograder.py

--- Helper Utility Script (run.py) ---
For convenience, a custom `run.py` script is included to quickly execute tests on the custom maze and run specific tasks:
python run.py dfs         (Runs DFS on CustomSearch)
python run.py bfs         (Runs BFS on CustomSearch)
python run.py ucs         (Runs UCS on CustomSearch)
python run.py gbfs        (Runs GBFS on CustomSearch)
python run.py astar       (Runs A* on CustomSearch)
python run.py task6-tiny  (Runs Corners Problem on tinyCorners)
python run.py task6-medium(Runs Corners Problem on mediumCorners)
python run.py task7       (Runs Food Search on trickySearch)
python run.py task8       (Runs Closest Dot Agent on bigSearch)
python run.py all         (Runs autograder.py)
* Add --fast to any command to skip GUI animations.

==============================================================================
AUTOGRADER RESULTS: 25/25 (100%)
==============================================================================
Question q1 (DFS):              3/3
Question q2 (BFS):              3/3
Question q3 (UCS):              3/3
Question q4 (A*):               3/3
Question q5 (CornersProblem):   3/3
Question q6 (cornersHeuristic): 3/3
Question q7 (foodHeuristic):    4/4
Question q8 (closestDot):       3/3
                              ------
Total:                         25/25
==============================================================================
