"""Test all 5 algorithms on CustomSearch maze layout."""
import pacman
import layout as layoutModule
import search
import searchAgents

lay = layoutModule.getLayout('CustomSearch')
if lay is None:
    raise RuntimeError("Could not find CustomSearch layout")

gameState = pacman.GameState()
gameState.initialize(lay, 0)

tests = [
    ('DFS', search.dfs, None),
    ('BFS', search.bfs, None),
    ('UCS', search.ucs, None),
    ('GBFS', search.gbfs, searchAgents.manhattanHeuristic),
    ('A*', search.astar, searchAgents.manhattanHeuristic),
]

print("=" * 60)
print(f"{'Algorithm':<10} {'Path Cost':<12} {'Nodes Expanded':<16}")
print("=" * 60)

for name, fn, heur in tests:
    prob = searchAgents.PositionSearchProblem(gameState, warn=False, visualize=False)
    if heur:
        actions = fn(prob, heuristic=heur)
    else:
        actions = fn(prob)
    print(f"{name:<10} {len(actions):<12} {prob._expanded:<16}")

print("=" * 60)
