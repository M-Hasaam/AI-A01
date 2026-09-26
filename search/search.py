# search.py
# ---------


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import csv
import os
import time


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


# ======================== CSV TRACE LOGGER ========================

# Counts logger instances so files created within the same microsecond stay unique
_log_counter = 0

class CSVLogger:
    """
    Automated CSV trace logger for search algorithms.
    Writes step-by-step execution logs to the evidence/ directory.

    Mandatory CSV Columns:
    iteration, expanded_state, parent, action, generated_successors,
    frontier_before, frontier_after, explored, g, h, f
    """

    def __init__(self, algorithm_name, problem):
        """Initialize the CSV logger with algorithm name and problem reference."""
        self.algorithm_name = algorithm_name
        self.rows = []
        self.iteration = 0
        # Determine the evidence directory path (relative to search.py location)
        self.evidence_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evidence')
        os.makedirs(self.evidence_dir, exist_ok=True)
        # Build a unique filename from algorithm name, timestamp (with microseconds)
        # and a run counter, so repeated searches (e.g. ClosestDotSearchAgent's
        # many BFS calls) never overwrite each other's logs
        global _log_counter
        _log_counter += 1
        now = time.time()
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime(now))
        micros = int((now % 1) * 1_000_000)
        # Extract problem type name for more descriptive filenames
        problem_name = type(problem).__name__
        self.filename = os.path.join(
            self.evidence_dir,
            f"{algorithm_name}_{problem_name}_{timestamp}_{micros:06d}_{_log_counter:03d}.csv"
        )

    def log(self, expanded_state, parent, action, generated_successors,
            frontier_before, frontier_after, explored, g=0, h=0, f=0):
        """Log a single iteration/step of the search algorithm."""
        self.iteration += 1
        # Limit explored set serialization for large sets
        if len(explored) > 50:
            explored_str = f"[{len(explored)} states]"
        else:
            explored_str = str(explored)
        # Limit generated successors serialization
        gen_str = str(generated_successors[:10]) if len(generated_successors) > 10 else str(generated_successors)
        self.rows.append({
            'iteration': self.iteration,
            'expanded_state': str(expanded_state),
            'parent': str(parent),
            'action': str(action),
            'generated_successors': gen_str,
            'frontier_before': str(frontier_before),
            'frontier_after': str(frontier_after),
            'explored': explored_str,
            'g': g,
            'h': h,
            'f': f
        })

    def write(self):
        """Write all logged rows to the CSV file."""
        if not self.rows:
            return
        fieldnames = ['iteration', 'expanded_state', 'parent', 'action',
                      'generated_successors', 'frontier_before', 'frontier_after',
                      'explored', 'g', 'h', 'f']
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.rows)
        except Exception as e:
            print(f"Warning: Could not write CSV log: {e}")


def _get_frontier_states_stack(frontier):
    """Extract states from a Stack frontier for logging (full frontier)."""
    try:
        return [str(item[0]) for item in frontier.list]
    except Exception:
        return ['<unavailable>']


def _get_frontier_states_queue(frontier):
    """Extract states from a Queue frontier for logging (full frontier)."""
    try:
        return [str(item[0]) for item in frontier.list]
    except Exception:
        return ['<unavailable>']


def _get_frontier_states_pq(frontier):
    """Extract states from a PriorityQueue frontier for logging (full frontier)."""
    try:
        return [str(item[2][0]) for item in frontier.heap]
    except Exception:
        return ['<unavailable>']


# ======================== SEARCH ALGORITHMS ========================


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Initialize CSV logger
    logger = CSVLogger('DFS', problem)

    # Use a LIFO Stack as the frontier for DFS
    frontier = util.Stack()
    # Each element on the stack is (state, list_of_actions_to_reach_state, parent_state)
    startState = problem.getStartState()
    frontier.push((startState, [], None))
    # Explored set to track visited states (graph search)
    explored = set()

    while not frontier.isEmpty():
        state, actions, parent = frontier.pop()

        # Skip if already explored
        if state in explored:
            continue

        # Mark state as explored
        explored.add(state)

        # Get frontier snapshot before expansion
        frontier_before = _get_frontier_states_stack(frontier)

        # Goal test upon expansion
        if problem.isGoalState(state):
            # Log the goal state expansion
            logger.log(
                expanded_state=state, parent=parent,
                action=actions[-1] if actions else 'Start',
                generated_successors=[], frontier_before=frontier_before,
                frontier_after=frontier_before, explored=list(explored),
                g=len(actions), h=0, f=len(actions)
            )
            logger.write()
            return actions

        # Expand successors
        successors = problem.getSuccessors(state)
        generated = []
        for successor, action, stepCost in successors:
            if successor not in explored:
                frontier.push((successor, actions + [action], state))
                generated.append((successor, action))

        # Get frontier snapshot after expansion
        frontier_after = _get_frontier_states_stack(frontier)

        # Log this iteration
        logger.log(
            expanded_state=state, parent=parent,
            action=actions[-1] if actions else 'Start',
            generated_successors=generated, frontier_before=frontier_before,
            frontier_after=frontier_after, explored=list(explored),
            g=len(actions), h=0, f=len(actions)
        )

    logger.write()
    return []  # No solution found

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    # Initialize CSV logger
    logger = CSVLogger('BFS', problem)

    # Use a FIFO Queue as the frontier for BFS
    frontier = util.Queue()
    startState = problem.getStartState()
    frontier.push((startState, [], None))
    # Explored set to track visited states (graph search)
    explored = set()
    # Also track states currently in the frontier to avoid re-enqueuing
    frontierStates = set()
    frontierStates.add(startState)

    while not frontier.isEmpty():
        state, actions, parent = frontier.pop()

        # Skip if already explored (shouldn't happen with frontier check, but safe)
        if state in explored:
            continue

        # Mark state as explored
        explored.add(state)

        # Get frontier snapshot before expansion
        frontier_before = _get_frontier_states_queue(frontier)

        # Goal test upon expansion
        if problem.isGoalState(state):
            logger.log(
                expanded_state=state, parent=parent,
                action=actions[-1] if actions else 'Start',
                generated_successors=[], frontier_before=frontier_before,
                frontier_after=frontier_before, explored=list(explored),
                g=len(actions), h=0, f=len(actions)
            )
            logger.write()
            return actions

        # Expand successors
        successors = problem.getSuccessors(state)
        generated = []
        for successor, action, stepCost in successors:
            if successor not in explored and successor not in frontierStates:
                frontier.push((successor, actions + [action], state))
                frontierStates.add(successor)
                generated.append((successor, action))

        # Get frontier snapshot after expansion
        frontier_after = _get_frontier_states_queue(frontier)

        # Log this iteration
        logger.log(
            expanded_state=state, parent=parent,
            action=actions[-1] if actions else 'Start',
            generated_successors=generated, frontier_before=frontier_before,
            frontier_after=frontier_after, explored=list(explored),
            g=len(actions), h=0, f=len(actions)
        )

    logger.write()
    return []  # No solution found

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    # Initialize CSV logger
    logger = CSVLogger('UCS', problem)

    # Use a PriorityQueue ordered by cumulative path cost g(n)
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    # Each element is (state, actions, cost, parent_state)
    frontier.push((startState, [], 0, None), 0)
    # Explored set to track visited states
    explored = set()
    # Track best known cost to each state in the frontier for updates
    bestCost = {startState: 0}

    while not frontier.isEmpty():
        state, actions, cost, parent = frontier.pop()

        # Get frontier snapshot before expansion
        frontier_before = _get_frontier_states_pq(frontier)

        # Goal test upon expansion (dequeue)
        if problem.isGoalState(state):
            logger.log(
                expanded_state=state, parent=parent,
                action=actions[-1] if actions else 'Start',
                generated_successors=[], frontier_before=frontier_before,
                frontier_after=frontier_before, explored=list(explored),
                g=cost, h=0, f=cost
            )
            logger.write()
            return actions

        # Skip if already explored
        if state in explored:
            continue

        # Mark state as explored
        explored.add(state)

        # Expand successors
        successors = problem.getSuccessors(state)
        generated = []
        for successor, action, stepCost in successors:
            newCost = cost + stepCost
            if successor not in explored:
                # Only add/update if we found a cheaper path
                if successor not in bestCost or newCost < bestCost[successor]:
                    bestCost[successor] = newCost
                    frontier.push((successor, actions + [action], newCost, state), newCost)
                    generated.append((successor, action, newCost))

        # Get frontier snapshot after expansion
        frontier_after = _get_frontier_states_pq(frontier)

        # Log this iteration
        logger.log(
            expanded_state=state, parent=parent,
            action=actions[-1] if actions else 'Start',
            generated_successors=generated, frontier_before=frontier_before,
            frontier_after=frontier_after, explored=list(explored),
            g=cost, h=0, f=cost
        )

    logger.write()
    return []  # No solution found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def greedyBestFirstSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic value first (greedy)."""
    # Initialize CSV logger
    logger = CSVLogger('GBFS', problem)

    # Use a PriorityQueue ordered strictly by heuristic value h(n)
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    hVal = heuristic(startState, problem)
    # Each element is (state, actions, parent_state)
    frontier.push((startState, [], None), hVal)
    # Explored set to track visited states
    explored = set()

    while not frontier.isEmpty():
        state, actions, parent = frontier.pop()

        # Skip if already explored
        if state in explored:
            continue

        # Mark state as explored
        explored.add(state)

        hVal = heuristic(state, problem)

        # Get frontier snapshot before expansion
        frontier_before = _get_frontier_states_pq(frontier)

        # Goal test upon expansion
        if problem.isGoalState(state):
            logger.log(
                expanded_state=state, parent=parent,
                action=actions[-1] if actions else 'Start',
                generated_successors=[], frontier_before=frontier_before,
                frontier_after=frontier_before, explored=list(explored),
                g=len(actions), h=hVal, f=hVal
            )
            logger.write()
            return actions

        # Expand successors
        successors = problem.getSuccessors(state)
        generated = []
        for successor, action, stepCost in successors:
            if successor not in explored:
                hSucc = heuristic(successor, problem)
                frontier.push((successor, actions + [action], state), hSucc)
                generated.append((successor, action, hSucc))

        # Get frontier snapshot after expansion
        frontier_after = _get_frontier_states_pq(frontier)

        # Log this iteration
        logger.log(
            expanded_state=state, parent=parent,
            action=actions[-1] if actions else 'Start',
            generated_successors=generated, frontier_before=frontier_before,
            frontier_after=frontier_after, explored=list(explored),
            g=len(actions), h=hVal, f=hVal
        )

    logger.write()
    return []  # No solution found

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Initialize CSV logger
    logger = CSVLogger('AStar', problem)

    # Use a PriorityQueue ordered by f(n) = g(n) + h(n)
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    hVal = heuristic(startState, problem)
    # Each element is (state, actions, g_cost, parent_state)
    frontier.push((startState, [], 0, None), 0 + hVal)
    # Explored set to track visited states
    explored = set()
    # Track best known g-cost to each state for frontier updates
    bestCost = {startState: 0}

    while not frontier.isEmpty():
        state, actions, gCost, parent = frontier.pop()

        # Get frontier snapshot before expansion
        frontier_before = _get_frontier_states_pq(frontier)

        hVal = heuristic(state, problem)
        fVal = gCost + hVal

        # Goal test upon expansion (dequeue)
        if problem.isGoalState(state):
            logger.log(
                expanded_state=state, parent=parent,
                action=actions[-1] if actions else 'Start',
                generated_successors=[], frontier_before=frontier_before,
                frontier_after=frontier_before, explored=list(explored),
                g=gCost, h=hVal, f=fVal
            )
            logger.write()
            return actions

        # Skip if already explored
        if state in explored:
            continue

        # Mark state as explored
        explored.add(state)

        # Expand successors
        successors = problem.getSuccessors(state)
        generated = []
        for successor, action, stepCost in successors:
            newGCost = gCost + stepCost
            if successor not in explored:
                # Only add/update if we found a cheaper path
                if successor not in bestCost or newGCost < bestCost[successor]:
                    bestCost[successor] = newGCost
                    hSucc = heuristic(successor, problem)
                    fCost = newGCost + hSucc
                    frontier.push((successor, actions + [action], newGCost, state), fCost)
                    generated.append((successor, action, newGCost, hSucc, fCost))

        # Get frontier snapshot after expansion
        frontier_after = _get_frontier_states_pq(frontier)

        # Log this iteration
        logger.log(
            expanded_state=state, parent=parent,
            action=actions[-1] if actions else 'Start',
            generated_successors=generated, frontier_before=frontier_before,
            frontier_after=frontier_after, explored=list(explored),
            g=gCost, h=hVal, f=fVal
        )

    logger.write()
    return []  # No solution found


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
