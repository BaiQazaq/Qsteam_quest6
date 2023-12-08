# 2. Implement Dijkstra's algorithm for finding the shortest path in a weighted graph.
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, weight):
        if start not in self.vertices:
            self.vertices[start] = []
        self.vertices[start].append((end, weight))

    def dijkstra(self, start):
        # Priority queue to store vertices with their distances
        priority_queue = [(0, start)]
        # Dictionary to store the minimum distance to each vertex
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 7)

start_vertex = 'A'
distances = graph.dijkstra(start_vertex)

for vertex, distance in distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex}: {distance}")
