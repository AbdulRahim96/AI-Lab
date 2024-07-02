import numpy as np
import heapq

# Initial matrix setup
array = np.ones((5, 5))
array[1:4, 1:2] = 0
array[1][2] = 0
array[1][3] = 5
array[4][0] = 4

# Print initial matrix
print("Initial matrix:")
print(array)

# Heuristic function (Manhattan distance)
def Heuristic(n, goal):
    return abs(n[0] - goal[0]) + abs(n[1] - goal[1])

# Get neighbors function
def get_neighbors(n, array):
    neighbors = []
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        neighbor = (n[0] + direction[0], n[1] + direction[1])
        if 0 <= neighbor[0] < array.shape[0] and 0 <= neighbor[1] < array.shape[1]:
            if array[neighbor] != 0:
                neighbors.append((neighbor, 1))
    return neighbors

# A* Algorithm implementation
def aStarAlgo(start_node, stop_node, array):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: None}

    while len(open_set) > 0:
        n = None
        
        # Node with the lowest f() is found
        for v in open_set:
            if n is None or g[v] + Heuristic(v, stop_node) < g[n] + Heuristic(n, stop_node):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] is not None:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            return path

        for (m, weight) in get_neighbors(n, array):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Define start and goal positions
start = (4, 0)
goal = (1, 3)

# Find path
path = aStarAlgo(start, goal, array)

# Update the matrix with the path
if path:
    for position in path:
        if array[position] == 1:
            array[position] = 2

# Print the updated matrix
print("\nMatrix after finding the path:")
print(array)
