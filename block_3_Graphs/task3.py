# 3. Write a program for breadth-first search in a graph.

from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.adj_list:
            self.adj_list[start_vertex] = []
        self.adj_list[start_vertex].append(end_vertex)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()

            if current_vertex not in visited:
                print(current_vertex, end=' ')
                visited.add(current_vertex)

                # Enqueue neighbors of the current vertex
                if current_vertex in self.adj_list:
                    queue.extend(self.adj_list[current_vertex])

# Example usage:
# Create a graph and add edges
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

# Perform BFS starting from vertex 0
print("BFS Traversal:")
graph.bfs(0)
