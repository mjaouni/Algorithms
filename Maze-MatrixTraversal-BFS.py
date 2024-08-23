# The maze is represented as a grid, where 1 represents open paths and 0 represents walls.
# The robot starts at a given position, and you need to determine
# If there is a path from the start position to the end position.

# We will Breadth-First Search (BFS) approach to explore all possible paths in the maze

from collections import deque


def is_path_exists(maze, start_position, end_position):     # For a matrix of size m*n :Time complexity O(m*n).
    if not maze or not start_position or not end_position:
        return False, []

    rows, cols = len(maze), len(maze[0])

    # Directions:right,down,left,up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(start_position, [start_position])])
    visited = set()
    visited.add(start_position)

    while queue:
        (current_row, current_col), path = queue.popleft()

        if (current_row, current_col) == end_position:
            return True, path

        for dr, dc in directions:
            new_row, new_col = new_position = current_row + dr, current_col + dc

            if (0 <= new_row < rows and 0 <= new_col < cols and
                    maze[new_row][new_col] == 1 and
                    new_position not in visited):
                queue.append((new_position, path + [new_position]))
                visited.add(new_position)

    return False, []


# Usage
maze_fail = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

start = (0, 0)
end = (4, 4)

# Calling the function and printing the path
path_exists,path = is_path_exists(maze,start,end)

if path_exists:
    print("Path exists from start to end.")
    print("Path:", path)
else:
    print("No path exists from start to end.")