# 1. Write a program to find the shortest path between two vertices in a graph.

import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, weight):
        if start not in self.vertices:
            self.vertices[start] = []
        self.vertices[start].append((end, weight))

    def dijkstra(self, start, end):
        # Priority queue to store vertices with their distances
        priority_queue = [(0, start)]
        # Dictionary to store the minimum distance to each vertex
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex == end:
                path = []
                while current_vertex in distances:
                    path.insert(0, current_vertex)
                    current_vertex = distances[current_vertex][1]
                return path, current_distance
            print("SELF - ", self.vertices, "****- ", self.vertices[current_vertex])
            print("DISTANCES - ", distances)
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight
                print("Current distance - ", current_distance)
                print("Neigbor - ", neighbor, "Weght - ", weight)
                print("Distance - ",distance, "neigbor - ", distances[neighbor])
                if distance < distances[neighbor]:
                    distances[neighbor] = (distance, current_vertex)
                    heapq.heappush(priority_queue, (distance, neighbor))

        return None  # No path found

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 7)

start_vertex = 'A'
end_vertex = 'E'
shortest_path, shortest_distance = graph.dijkstra(start_vertex, end_vertex)

if shortest_path:
    print(f"Shortest path from {start_vertex} to {end_vertex}: {shortest_path}")
    print(f"Shortest distance: {shortest_distance}")
else:
    print(f"No path found from {start_vertex} to {end_vertex}")
