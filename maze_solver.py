import random
def generate_maze(rows, cols, end):
    maze = [['▓'] * cols for _ in range(rows)]
    stack = [(0, 0)]
    visited = set()

    while stack:
        current = stack[-1]
        r, c = current 

        maze[r][c] = '◌' # Mark the current cell as visited

        if current == end:
            break

        four_dir = [(r, c - 1), (r, c + 1), (r + 1, c), (r - 1, c)]
        unvisited_neighbors=[]
        for dr, dc in four_dir:
            if dr in range(rows) and dc in range(cols):
                unvisited_neighbors.append((dr, dc))

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()
    return maze 


# Maze solver Using B. F. S Algo-------------------------------------------------------------->
from collections import deque

def bfs(maze, start, end):
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        row, col = current

        if current == end:
            return path + [end]

        if row >=0 and row < n and col >=0 and col < m and maze[row][col] == '◌' and visited[row][col] != True:
            visited[row][col] = True
            queue.append(((row + 1, col), path + [(row, col)]))
            queue.append(((row - 1, col), path + [(row, col)]))
            queue.append(((row, col + 1), path + [(row, col)]))
            queue.append(((row, col - 1), path + [(row, col)]))

    return None  # No path found

def print_maze(maze):
    maze[0][0]='S'
    maze[n-1][n-1]='E'
    for r in range(n):
        for c in range(n):
            if maze[r][c]=="S":
                print("\033[92mS\033[0m" , end=" ")

            elif maze[r][c]=='▓':    

                print("\033[91m▓\033[0m", end=" ")
            elif maze[r][c]=='◍':
                print("\033[92m◍\033[0m", end=" ")
            elif maze[r][c]=='◌': 
                print("\033[94m◌\033[0m", end=" ")
            elif maze[r][c]=='E': 
                print("\033[92mE\033[0m", end=" ")                        
        print()  

while True:
    user_input2=int(input("""
      1. Generate New puzzle
      2. Print the path
      3. Exit the Game
      Enter your choice (1/2/3): """))
    if user_input2==1:
        n=int(input("🟢-Enter the size of Maze(n*n): "))
        end = (n - 1, n - 1)
        maze = generate_maze(n, n, end)
        # Print the generated maze
        print_maze(maze)
        print("🟢-Maze generated!")                          
    elif user_input2==2:
        try:    
            n=len(maze)
            maze[0][0]="◌"
            maze[n-1][n-1]="◌"
            result_path = bfs(maze, (0,0), (n-1,n-1))
            if result_path :
                for lis in result_path:
                    r=lis[0]
                    c=lis[1]
                    maze[r][c] = '◍'
                maze[0][0]='S'
                maze[n-1][n-1]='E'    
                print_maze(maze)    
                print("------------------------------------------------------------------------------")    
            else:
                print("NOTE FOUND PERFECT PATH")  
        except:
            print("🔴-First Generate The Maze")  
    else:
        print("🟢-Thanks You")
        break 
#04          