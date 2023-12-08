# 1. Represent a graph using an adjacency matrix.

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Create a num_vertices x num_vertices matrix initialized with zeros
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start_vertex, end_vertex):
        # Add an edge between start_vertex and end_vertex
        # For an undirected graph, you'd also set adj_matrix[end_vertex][start_vertex] to 1
        self.adj_matrix[start_vertex][end_vertex] = 1
        self.adj_matrix[end_vertex][start_vertex] = 1

    def display(self):
        for row in self.adj_matrix:
            print(row)

# Example usage:
# Create a graph with 4 vertices
graph = Graph(4)

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)

# Display the adjacency matrix
graph.display()
