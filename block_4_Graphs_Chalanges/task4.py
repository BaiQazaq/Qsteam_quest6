# 4.  Write a method for topological sorting in a directed acyclic graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(v)

    def topological_sort(self):
        num_vertices = len(self.graph)
        visited = [False] * num_vertices
        stack = []

        for vertex in range(num_vertices):
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)

        return stack[::-1]

# Example usage:
graph = Graph()
graph.add_edge(5, 2)
graph.add_edge(5, 0)
graph.add_edge(4, 0)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

topological_order = graph.topological_sort()
print("Topological Order:", topological_order)
