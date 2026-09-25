import sys
import os

def get_command(algo, layout, fast):
    if algo == "dfs":
        cmd = f"python pacman.py -l {layout} -p SearchAgent -a fn=dfs"
    elif algo == "bfs":
        cmd = f"python pacman.py -l {layout} -p SearchAgent -a fn=bfs"
    elif algo == "ucs":
        cmd = f"python pacman.py -l {layout} -p SearchAgent -a fn=ucs"
    elif algo == "gbfs":
        cmd = f"python pacman.py -l {layout} -p SearchAgent -a fn=gbfs,heuristic=manhattanHeuristic"
    elif algo == "astar":
        cmd = f"python pacman.py -l {layout} -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic"
    elif algo == "task6-tiny":
        cmd = "python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem"
    elif algo == "task6-medium":
        cmd = "python pacman.py -l mediumCorners -p AStarCornersAgent"
    elif algo == "task7":
        cmd = "python pacman.py -l trickySearch -p AStarFoodSearchAgent"
    elif algo == "task8":
        cmd = "python pacman.py -l bigSearch -p ClosestDotSearchAgent"
    elif algo == "all":
        cmd = "python autograder.py"
    else:
        return None
        
    if fast:
        cmd += " --frameTime 0"
    return cmd

def print_help():
    print("Usage: python run.py [algorithm] [layout] [--fast]")
    print("\nAlgorithms: dfs, bfs, ucs, gbfs, astar")
    print("\nExamples:")
    print("  python run.py dfs               (Runs DFS on mediumMaze by default)")
    print("  python run.py dfs tiny          (Runs DFS on tinyMaze)")
    print("  python run.py dfs big           (Runs DFS on bigMaze)")
    print("  python run.py dfs custom        (Runs DFS on CustomSearch)")
    print("  python run.py astar CustomSearch (Runs A* on CustomSearch)")
    print("\nOther Tasks:")
    print("  task6-tiny, task6-medium, task7, task8, all")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
        
    algo = sys.argv[1]
    
    # Parse fast flag
    fast = "--fast" in sys.argv
    args = [arg for arg in sys.argv[2:] if arg != "--fast"]
    
    # Parse layout (defaults to mediumMaze if running standard search algos)
    layout = "mediumMaze"
    if args:
        layout = args[0]
        # Allow shortcuts like 'tiny', 'medium', 'big', 'custom'
        if layout in ["tiny", "medium", "big"]:
            layout = layout + "Maze"
        elif layout == "custom":
            layout = "CustomSearch"
            
    cmd = get_command(algo, layout, fast)
    
    if cmd is None:
        print(f"Unknown command: {algo}")
        print_help()
        sys.exit(1)
        
    print(f"Executing: {cmd}")
    os.system(cmd)
