import networkx as nx
import matplotlib.pyplot as plt
import heapq

nodes = [
    "Erfurt",
    "Kassel",
    "Frankfurt",
    "Hamburg",
    "Berlin",
    "Munchen",
    "Stuttgart",
]

edges = [
    ("Erfurt", "Kassel", 151),
    ("Erfurt", "Frankfurt", 261),
    ("Erfurt", "Hamburg", 360),
    ("Erfurt", "Berlin", 302),
    ("Erfurt", "Munchen", 399),
    ("Erfurt", "Stuttgart", 342),
    ("Kassel", "Erfurt", 151),
    ("Kassel", "Frankfurt", 176),
    ("Kassel", "Hamburg", 310),
    ("Frankfurt", "Erfurt", 261),
    ("Frankfurt", "Kassel", 176),
    ("Frankfurt", "Munchen", 393),
    ("Frankfurt", "Stuttgart", 206),
    ("Hamburg", "Erfurt", 360),
    ("Hamburg", "Kassel", 310),
    ("Hamburg", "Berlin", 290),
    ("Berlin", "Erfurt", 302),
    ("Berlin", "Hamburg", 290),
    ("Munchen", "Erfurt", 399),
    ("Munchen", "Frankfurt", 393),
    ("Munchen", "Stuttgart", 232),
    ("Stuttgart", "Erfurt", 342),
    ("Stuttgart", "Frankfurt", 206),
    ("Stuttgart", "Munchen", 232),
]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

distance = {}

for node in nodes:
    distance[node] = float('inf')

start = "Erfurt"
distance[start] = 0

heap = []

heapq.heappush(heap, (0, "Erfurt"))

def dijkstra(h):
    while h:

        (current_distance, city) = heapq.heappop(h)

        if current_distance > distance[city]:
            continue

        for neighbor in G.neighbors(city):
            weight = G[city][neighbor]['weight']
            new_distance = distance[city] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(h, (new_distance, neighbor))
    
dijkstra(heap)
print(distance)