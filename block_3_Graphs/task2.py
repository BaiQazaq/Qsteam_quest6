# 2. Implement graph representation using an adjacency list.

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Create an empty list for each vertex to store its neighbors
        self.adj_list = {vertex: [] for vertex in range(num_vertices)}

    def add_edge(self, start_vertex, end_vertex):
        # Add an edge between start_vertex and end_vertex
        # For an undirected graph, you'd also add end_vertex to the neighbors of start_vertex
        self.adj_list[start_vertex].append(end_vertex)
        self.adj_list[end_vertex].append(start_vertex)

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

# Example usage:
# Create a graph with 4 vertices
graph = Graph(4)

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

# Display the adjacency list
graph.display()
