class Graph:
    def __init__(self, vertices):
        self.graph = vertices

    def bfs(self, start):
        visited = []
        queue = [start]

        while queue:
            print("\ncurrent queue: ", queue)
            print("visited: ", visited)
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend(self.graph[node])
        return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

bfs = Graph(graph)
print(bfs.bfs('A'))


   