# 5. Implement a method to detect a cycle in an undirected graph.
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex not in self.adj_list:
            self.adj_list[start_vertex] = []
        if end_vertex not in self.adj_list:
            self.adj_list[end_vertex] = []

        self.adj_list[start_vertex].append(end_vertex)
        self.adj_list[end_vertex].append(start_vertex)

    def has_cycle(self):
        visited = set()

        for vertex in self.adj_list:
            if vertex not in visited:
                if self._has_cycle_util(vertex, visited, parent=None):
                    return True
        return False

    def _has_cycle_util(self, current_vertex, visited, parent):
        visited.add(current_vertex)

        for neighbor in self.adj_list[current_vertex]:
            if neighbor not in visited:
                if self._has_cycle_util(neighbor, visited, current_vertex):
                    return True
            elif parent is not None and neighbor != parent:
                # If the neighbor is already visited and not the parent, a cycle is detected
                return True

        return False

# Example usage:
# Create a graph with a cycle
graph_with_cycle = Graph()
graph_with_cycle.add_edge(0, 1)
graph_with_cycle.add_edge(1, 2)
graph_with_cycle.add_edge(2, 0)
graph_with_cycle.add_edge(1, 3)

# Check if the graph has a cycle
print("Graph with cycle:", graph_with_cycle.has_cycle())

# Create a graph without a cycle
graph_without_cycle = Graph()
graph_without_cycle.add_edge(0, 1)
graph_without_cycle.add_edge(1, 2)
graph_without_cycle.add_edge(2, 3)

# Check if the graph has a cycle
print("Graph without cycle:", graph_without_cycle.has_cycle())
