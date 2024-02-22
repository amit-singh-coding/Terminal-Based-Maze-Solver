import random
def generate_maze(rows, cols, start, end):
    maze = [["🔴"] * cols for _ in range(rows)]
    stack = [(0, 0)]
    visited = set()

    while stack:
        current = stack[-1]
        x, y = current

        maze[x][y] = "🔵" # Mark the current cell as visited

        if current == end:
            break

        neighbors = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in visited]

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()

    return maze

#Maze Solver-----> 
from collections import deque
def maze_solver(maze):
    if not maze or not maze[0]:
        return []

    n, m = len(maze), len(maze[0])
    start = (0, 0)
    end = (n - 1, m - 1)
    path = []
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start, path)])

    while queue:
        (current_row, current_col), current_path = queue.popleft()

        if not (0 <= current_row < n and 0 <= current_col < m) or maze[current_row][current_col] == "🔴" or visited[current_row][current_col]:
            continue

        visited[current_row][current_col] = True
        current_path.append((current_row, current_col))

        if (current_row, current_col) == end:
            return current_path

        # Explore in all possible directions (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            next_row, next_col = current_row + dr, current_col + dc
            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col] and maze[next_row][next_col] == "🔵":
                queue.append(((next_row, next_col), current_path[:]))

    return []

maze=[
        ['🔵', '🔵', '🔵', '🔴', '🔴'],
        ['🔴', '🔵', '🔵', '🔵', '🔵'],
        ['🔴', '🔴', '🔵', '🔴', '🔵'],
        ['🔴', '🔴', '🔴', '🔵', '🔵'],
        ['🔴', '🔴', '🔴', '🔴', '🔵']]
while True:
    user_input2=int(input("""
      1. Generate New puzzle
      2. Print the path
      3. Exit the Game
      Enter your choice (1/2/3): """))
    if user_input2==1:
        n=int(input("Enter the size of Maze(n*n): "))
        start = (0, 0)
        end = (n - 1, n - 1)
        maze=generate_maze(n, n, start, end) 
        # Print the generated maze
        for row in maze:
            print(row)
        print("Maze generated!")                          
    elif user_input2==2:
        result_path = maze_solver(maze)
        if len(result_path)>0:
            for lis in result_path:
                r=lis[0]
                c=lis[1]
                maze[r][c]="🟢"
            print("------------------------------------------------------------------------------")    
            for row in maze:
                print(row)
        else:
            print("NOTE FOUND PERFECT PATH")    
    else:
        print("Thanks You")
        break
#third commit 

           