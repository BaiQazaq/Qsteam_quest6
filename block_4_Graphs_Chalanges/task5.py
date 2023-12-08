# 5. Implement a program to find strongly connected components in a graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(vertex)

    def transpose(self):
        transposed_graph = Graph()
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def fill_order(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.fill_order(neighbor, visited, stack)
        stack.append(vertex)

    def get_sccs(self):
        num_vertices = len(self.graph)
        stack = []
        visited = [False] * num_vertices

        # Fill the stack with the finishing times of vertices in the original graph
        for vertex in range(num_vertices):
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)

        # Transpose the graph
        transposed_graph = self.transpose()

        # Reset visited array for the second DFS
        visited = [False] * num_vertices

        # Perform DFS on the transposed graph in the order of finishing times
        sccs = []
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                scc = []
                transposed_graph.fill_order(vertex, visited, scc)
                sccs.append(scc)

        return sccs

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(1, 3)
graph.add_edge(3, 4)

sccs = graph.get_sccs()
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
