# AI Assignment #1
## Problem Solving by Search

### Project Description
This project implements two informed search algorithms using the Romania road map to find the shortest path to Bucharest.

### Implemented Algorithms
1. Greedy Best-First Search
2. A* Search

### Requirements
- Python 3.x
- Visual Studio Code (or any Python IDE)

### Project Files
- `main.py`: Contains the Romania road map, heuristic values, search algorithms, and experiments.
- `README.md`: Contains the project description and instructions for running the program.

### How to Run
1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python main.py
```

### Experiments
The program performs the following experiments:

1. Greedy Best-First Search and A* from Arad.
2. Greedy Best-First Search and A* from Timisoara.
3. A* using a zero heuristic (h = 0).
4. A* using a doubled heuristic (2 × h).
5. Additional A* experiments from Timisoara.
6. Additional Greedy experiments using h = 0 and 2 × h.
7. Heuristic admissibility test using eight cities.

### Performance Metrics
- **Path:** The route from the starting city to Bucharest.
- **Path Cost:** The total road distance in kilometers.
- **Nodes Expanded:** Number of nodes expanded during the search.
- **Max Frontier:** Maximum number of entries in the frontier during the search.

### Goal
The goal state is Bucharest.

### Heuristic
The heuristic function uses straight-line distances from each city to Bucharest.

### Output
The program prints the search paths, path costs, expanded nodes, maximum frontier sizes, and heuristic admissibility results.

### Programming Language
Python 3
