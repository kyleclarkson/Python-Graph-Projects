from Graph import Graph
import Traversal

G = Graph()
Graph.read_from_csv("")

u = G.insert_vertex('1')
v = G.insert_vertex('2')
w = G.insert_vertex('3')
x = G.insert_vertex('4')

G.insert_edge(u,v)
G.insert_edge(v,w)
G.insert_edge(u,x)
G.insert_edge(x,w)

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