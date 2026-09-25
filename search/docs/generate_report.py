import os
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def create_report():
    doc = Document()
    
    # ---------------------------------------------------------
    # TITLE PAGE
    # ---------------------------------------------------------
    title = doc.add_heading('Artificial Intelligence (AI2002)', 0)
    title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    subtitle = doc.add_paragraph('Assignment 01: Pac-Man Search Project Report')
    subtitle.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph('\n')
    group_title = doc.add_paragraph('Group Members:')
    group_title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    m1 = doc.add_paragraph('Muhammad Hasaam (24i-3107)')
    m1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    m2 = doc.add_paragraph('Abdullah (24i-3001)')
    m2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    m3 = doc.add_paragraph('Umer (24i-3002)')
    m3.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_page_break()
    
    # ---------------------------------------------------------
    doc.add_heading('1. Introduction', level=1)
    doc.add_paragraph(
        "This comprehensive report details the implementation, execution, and critical analysis of various "
        "fundamental search algorithms applied to the Pac-Man agent environment. The core objective of this "
        "project was to design agents capable of autonomously navigating through increasingly complex mazes to "
        "achieve specific goals, such as reaching a single food pellet or efficiently consuming all food pellets "
        "in the maze."
    )
    doc.add_paragraph(
        "To achieve this, we implemented five distinct search algorithms: Depth-First Search (DFS), "
        "Breadth-First Search (BFS), Uniform-Cost Search (UCS), Greedy Best-First Search (GBFS), and A* Search. "
        "We systematically tested these algorithms across a variety of state-space formulations, ranging from "
        "simple position searches to highly complex multi-goal scenarios like the Corners Problem and Food Search."
    )
    
    doc.add_heading('1.1 Division of Labor', level=2)
    doc.add_paragraph(
        "As a group of three, we divided the project tasks to ensure a collaborative and balanced workload. "
        "The responsibilities were distributed as follows:"
    )
    doc.add_paragraph("• Muhammad Hasaam (24i-3107): Implemented the core uninformed search algorithms (DFS, BFS, UCS) and designed the custom adversarial maze (CustomSearch.lay) for algorithm testing.")
    doc.add_paragraph("• Abdullah (24i-3001): Implemented the informed search algorithms (Greedy Best-First Search, A* Search) and engineered the underlying heuristics (Manhattan, Euclidean) used to guide them.")
    doc.add_paragraph("• Umer (24i-3002): Handled the complex multi-goal formulations (Corners Problem, Food Search Problem, Closest Dot Agent) and compiled the final academic report and documentation.")
    
    # ---------------------------------------------------------
    # 2. STATE SPACE REPRESENTATION
    # ---------------------------------------------------------
    doc.add_heading('2. State Space Representation', level=1)
    
    doc.add_heading('2.1 Standard Search (PositionSearchProblem)', level=2)
    doc.add_paragraph(
        "In a standard pathfinding scenario, the objective is to find a path from Pac-Man's starting location "
        "to a single target location. Consequently, the state space is highly simplified. A 'state' is uniquely "
        "defined solely by Pac-Man's current (x, y) coordinates on the grid. The state space size is proportional "
        "to the number of walkable spaces in the maze. The starting state is the initial coordinate, and the goal "
        "state is reached when Pac-Man's coordinate matches the target coordinate."
    )
    
    doc.add_heading('2.2 Corners Problem', level=2)
    doc.add_paragraph(
        "The Corners Problem introduces a significantly more complex multi-goal formulation. Pac-Man must navigate "
        "the maze to visit all four corners. Because the agent must remember which corners it has already visited, "
        "tracking just the (x, y) position is no longer sufficient. A state in this problem is represented as a tuple: "
        "(current_position, visited_corners). The 'visited_corners' element is a boolean tuple that acts as a memory "
        "flag for the four corners. This state representation exponentially increases the total number of possible states, "
        "demonstrating the curse of dimensionality in search problems."
    )
    
    # ---------------------------------------------------------
    # 3. ALGORITHM ANALYSIS
    # ---------------------------------------------------------
    doc.add_heading('3. Algorithm Complexity & Theoretical Analysis', level=1)
    doc.add_paragraph(
        "Below is a theoretical breakdown of the five algorithms implemented in this project, assuming a branching factor "
        "of 'b', maximum depth 'm', and solution depth 'd'."
    )
    
    complexities = [
        ("Depth-First Search (DFS)", "Time: O(b^m)", "Space: O(bm)", 
         "DFS is implemented using a Last-In-First-Out (LIFO) Stack. It explores as deeply as possible along each branch before backtracking. "
         "While it is incredibly memory efficient (linear space), it is neither optimal nor complete (without cycle checking). "
         "In our tests, DFS often found highly convoluted, non-optimal paths because it simply takes the first valid path it stumbles upon."),
        
        ("Breadth-First Search (BFS)", "Time: O(b^d)", "Space: O(b^d)", 
         "BFS is implemented using a First-In-First-Out (FIFO) Queue. It explores the search tree level by level. "
         "This guarantees finding the shallowest goal node, making it strictly optimal for unweighted graphs (where all step costs are equal). "
         "However, its memory footprint grows exponentially, making it unsuitable for massive state spaces."),
         
        ("Uniform-Cost Search (UCS)", "Time: O(b^(1+floor(C*/e)))", "Space: O(b^(1+floor(C*/e)))", 
         "UCS utilizes a Priority Queue ordered by the cumulative path cost g(n). It behaves identically to BFS in unweighted graphs but "
         "is capable of finding the optimal path in graphs with varying step costs. It is complete and optimal but expands nodes in every direction "
         "like a contour map, which can be computationally expensive."),
         
        ("Greedy Best-First Search (GBFS)", "Time: O(b^m)", "Space: O(b^m)", 
         "GBFS uses a Priority Queue ordered exclusively by a heuristic function h(n) that estimates the distance to the goal. "
         "It aggressively pursues paths that 'look' closer to the goal. While extremely fast in practice, it completely ignores the cost already "
         "incurred, making it strictly sub-optimal and highly vulnerable to deceptive dead ends."),
         
        ("A* Search", "Time: O(b^d)", "Space: O(b^d)", 
         "A* Search intelligently combines the exact cost g(n) from UCS with the estimated cost h(n) from GBFS, using the evaluation function f(n) = g(n) + h(n). "
         "As long as the heuristic is admissible (never overestimates) and consistent, A* is both complete and optimally efficient. It is the gold standard for pathfinding in this project.")
    ]
    
    for algo, time, space, desc in complexities:
        doc.add_heading(algo, level=2)
        doc.add_paragraph(f"• {time}")
        doc.add_paragraph(f"• {space}")
        doc.add_paragraph(desc)
        
    doc.add_page_break()
    
    # ---------------------------------------------------------
    # 4. CUSTOM MAZE ANALYSIS (GBFS vs A*)
    # ---------------------------------------------------------
    doc.add_heading('4. Custom Maze Analysis: The Weakness of GBFS', level=1)
    doc.add_paragraph(
        "To practically demonstrate the theoretical differences between Greedy Best-First Search and A* Search, "
        "we designed a custom layout named 'CustomSearch.lay'. This maze was meticulously constructed to exploit the "
        "blind spots in GBFS's heuristic-only approach."
    )
    doc.add_paragraph(
        "The maze features a prominent, deceptive corridor. Physically, this corridor heads directly toward the goal "
        "coordinates, drastically reducing the Manhattan Distance heuristic h(n). However, it ultimately results in a massive "
        "dead end. GBFS, guided entirely by h(n), blindly rushes into this trap and is forced to expand hundreds of unnecessary nodes "
        "before backtracking."
    )
    
    doc.add_heading('4.1 GBFS Execution', level=2)
    doc.add_paragraph("As seen below, GBFS takes the bait. It explores the entire right-side dead end because it visually looks closer to the goal:")
    if os.path.exists('image/gbfs.png'):
        doc.add_picture('image/gbfs.png', width=Inches(6))
    else:
        doc.add_paragraph("[MISSING: image/gbfs.png]")
    
    doc.add_heading('4.2 A* Search Execution', level=2)
    doc.add_paragraph(
        "A*, on the other hand, factors in the growing path cost g(n). As it steps deeper into the trap, f(n) increases. "
        "It quickly realizes the trap is inefficient, abandons the dead end early, and finds the optimal path:"
    )
    if os.path.exists('image/astar.png'):
        doc.add_picture('image/astar.png', width=Inches(6))
    else:
        doc.add_paragraph("[MISSING: image/astar.png]")
        
    doc.add_page_break()
    
    # ---------------------------------------------------------
    # 5. STANDARD ALGORITHMS ON CUSTOM MAZE
    # ---------------------------------------------------------
    doc.add_heading('5. Standard Algorithms on Custom Maze', level=1)
    doc.add_paragraph(
        "For completeness, we also tested the blind (uninformed) search algorithms on our custom maze to observe "
        "their behavior without heuristic guidance."
    )
    
    doc.add_heading('5.1 Depth-First Search (DFS)', level=2)
    doc.add_paragraph("DFS finds a solution, but as expected, it is a highly inefficient, winding path. It blindly follows walls until it hits the target.")
    if os.path.exists('image/dfs.png'):
        doc.add_picture('image/dfs.png', width=Inches(6))
        
    doc.add_heading('5.2 Breadth-First Search (BFS)', level=2)
    doc.add_paragraph("BFS reliably finds the optimal path. However, because it radiates outward in all directions evenly, the red search nodes show that it exhaustively explored a massive portion of the maze to guarantee optimality.")
    if os.path.exists('image/bfs.png'):
        doc.add_picture('image/bfs.png', width=Inches(6))

    doc.add_heading('5.3 Uniform-Cost Search (UCS)', level=2)
    doc.add_paragraph("Because step costs are uniform (1) in this maze, UCS behaves identically to BFS, expanding the exact same nodes and returning the same optimal path.")
    if os.path.exists('image/ucs.png'):
        doc.add_picture('image/ucs.png', width=Inches(6))

    doc.add_page_break()
    
    # ---------------------------------------------------------
    # 6. HEURISTIC DESIGN AND ADVANCED TASKS
    # ---------------------------------------------------------
    doc.add_heading('6. Heuristic Design and Advanced Tasks', level=1)
    doc.add_paragraph(
        "The final phase of the project required designing custom admissible and consistent heuristics for complex multi-goal scenarios."
    )
    
    doc.add_heading('6.1 Corners Problem (Task 6)', level=2)
    doc.add_paragraph("We implemented a state representation that tracks visited corners and designed a custom heuristic that estimates the distance to the farthest unvisited corner. This drastically reduced the number of expanded nodes compared to standard UCS.")
    
    if os.path.exists('image/task6-tiny.png'):
        doc.add_picture('image/task6-tiny.png', width=Inches(5))
    if os.path.exists('image/task6-medium.png'):
        doc.add_picture('image/task6-medium.png', width=Inches(5))

    doc.add_heading('6.2 Eating All The Dots (Task 7)', level=2)
    doc.add_paragraph("The Food Search problem required A* to find an optimal path that consumes every single dot. Our heuristic calculates the maximum distance to the furthest dot, sometimes utilizing maze distance approximations to remain admissible while providing strong guidance.")
    if os.path.exists('image/task7.png'):
        doc.add_picture('image/task7.png', width=Inches(6))

    doc.add_heading('6.3 Suboptimal Search: Closest Dot Agent (Task 8)', level=2)
    doc.add_paragraph("Finding the true optimal path for all dots is NP-Hard. As a practical alternative, we implemented an agent that repeatedly uses BFS to find and eat the nearest dot. While not strictly optimal overall, it computes a highly efficient path in a fraction of the time.")
    if os.path.exists('image/task8.png'):
        doc.add_picture('image/task8.png', width=Inches(6))
        
    # ---------------------------------------------------------
    # 7. CONCLUSION
    # ---------------------------------------------------------
    doc.add_heading('7. Conclusion', level=1)
    doc.add_paragraph(
        "This project successfully demonstrated the fundamental trade-offs in search algorithms. We proved that while uninformed algorithms like BFS guarantee optimality, they do so at a severe memory and computational cost. "
        "Conversely, Greedy Best-First Search sacrifices optimality for incredible speed but is easily fooled by complex obstacles. "
        "Ultimately, A* Search, when paired with a well-designed, admissible heuristic, provided the perfect balance—yielding optimal solutions with highly efficient node expansion."
    )

    doc.save('report.docx')
    print("Super detailed report.docx successfully generated.")

if __name__ == '__main__':
    create_report()
