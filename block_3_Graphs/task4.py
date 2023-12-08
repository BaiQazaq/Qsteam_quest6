# 4. Create a depth-first search algorithm for a graph.
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.adj_list:
            self.adj_list[start_vertex] = []
        self.adj_list[start_vertex].append(end_vertex)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_vertex)
        print(start_vertex, end=' ')

        if start_vertex in self.adj_list:
            for neighbor in self.adj_list[start_vertex]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

# Example usage:
# Create a graph and add edges
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

# Perform DFS starting from vertex 0
print("DFS Traversal:")
graph.dfs(0)
