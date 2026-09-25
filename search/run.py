import sys
import os

COMMANDS = {
    "dfs": "python pacman.py -l CustomSearch -p SearchAgent -a fn=dfs",
    "bfs": "python pacman.py -l CustomSearch -p SearchAgent -a fn=bfs",
    "ucs": "python pacman.py -l CustomSearch -p SearchAgent -a fn=ucs",
    "gbfs": "python pacman.py -l CustomSearch -p SearchAgent -a fn=gbfs,heuristic=manhattanHeuristic",
    "astar": "python pacman.py -l CustomSearch -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic",
    "task6-tiny": "python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem",
    "task6-medium": "python pacman.py -l mediumCorners -p AStarCornersAgent",
    "task7": "python pacman.py -l trickySearch -p AStarFoodSearchAgent",
    "task8": "python pacman.py -l bigSearch -p ClosestDotSearchAgent",
    "all": "python autograder.py"
}

def print_help():
    print("Usage: python run.py [algorithm]")
    print("\nAvailable commands:")
    for key, cmd in COMMANDS.items():
        print(f"  {key:<6} -> Runs {cmd}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print_help()
        sys.exit(1)
        
    algo = sys.argv[1]
    cmd = COMMANDS[algo]
    
    # Check if user wants to skip animation
    if len(sys.argv) > 2 and sys.argv[2] == "--fast":
        cmd += " --frameTime 0"
        
    print(f"Executing: {cmd}")
    os.system(cmd)
