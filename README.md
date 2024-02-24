
# 🔷Terminal-Based Maze Solver🔷

A terminal-based Maze Solver generates a random maze, and finds a path from the start (0,0) to the end (n-1,n-1), and visualizes the maze and path in the terminal.


![Maze Solver Screenshot](https://github.com/amit-singh-coding/Terminal-Based-Maze-Solver/blob/main/maze_img.jpg)




## Specifications:

**Input:** 

1- Size of the maze (n*n).

2- Users choose to either print the path, generate another puzzle, or exit the game.

**Outpur:**

1- A visual representation of the generated maze in the terminal.

2-A visual representation of the path from start to end, if it exists

`->` Start (S) and End (E)

`->` Walls: ▓ (red) 

`->` Open Space: ◌ (blue)

`->` Path: ◍ (green)



## Prerequisites

- Basic understanding of arrays and loops.

- Familiarity with terminal-based input/output


## Code Components

**Libraries**

🎲 random : Used for generating random numbers for maze generation.

🖥️ os: Used for clearing the terminal screen ('cls' for Windows, 'clear' for Unix-like systems).


🧱 deque : Used for the deque in breadth-first search Algo.

**Data Structures Used**

`Stack :` Used in the Recursive Backtracking maze generation algorithm.

`Set :` Used for tracking visited cells in maze generation and pathfinding.

`deque :` Used for BFS algorithm.

`list ` Used for store the path 

**Algorithms**

+ Breadth-First Search (BFS)

+ Depth-First Search (DFS)

+ Recursion and backtracking
## Installation

1- Clone the repository: `git clone https://github.com/amit-singh-coding/Terminal-Based-Maze-Solver`

2- Navigate to the project directory: `cd Terminal-Based-Maze-Solver`

3- Run the program: `python maze_solver.py` 

