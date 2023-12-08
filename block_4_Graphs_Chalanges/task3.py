# 3. Create a function to detect a cycle in a directed graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, recursion_stack):
        visited[v] = True
        recursion_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[v] = False
        return False

    def is_cyclic(self):
        num_vertices = len(self.graph)
        visited = [False] * num_vertices
        recursion_stack = [False] * num_vertices

        for vertex in range(num_vertices):
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, recursion_stack):
                    return True

        return False

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

if graph.is_cyclic():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
