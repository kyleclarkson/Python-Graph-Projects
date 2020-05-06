from Graph import Graph
import Traversal

G = Graph()

u = G.insert_vertex('u')
v = G.insert_vertex('v')
w = G.insert_vertex('w')

G.insert_edge(u,v, "u-v")
G.insert_edge(v,w, "v-w")

print(G.vertex_count())
print(G.edge_count())

print("Edges incident to u: ", len(list(G.incident_edges(u))))
print("Edges incident to v: ", len(list(G.incident_edges(v))))

discovered = {u: None}
Traversal.DFS(G, u, discovered)

path = Traversal.DFS_construct_vertex_path(u, w, discovered)
result = [vertex.element() for vertex in path]
print(*result, sep=",")

path = Traversal.DFS_construct_edge_path(u, w, discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")