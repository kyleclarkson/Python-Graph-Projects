from Graph import Graph
from TestContainer import Node, Arc
import Traversal

# Test creating graph
G = Graph()

u = G.insert_vertex(Node('u'))
u.element().set_vertex(u)
v = G.insert_vertex(Node('v'))
v.element().set_vertex(v)
w = G.insert_vertex(Node('w'))
w.element().set_vertex(w)
x = G.insert_vertex(Node('x'))
x.element().set_vertex(x)

e = G.insert_edge(u, v, Arc())
e.element().set_edge(e)
e = G.insert_edge(v, w, Arc())
e.element().set_edge(e)
e = G.insert_edge(w, x, Arc())
e.element().set_edge(e)
e = G.insert_edge(u, x, Arc())
e.element().set_edge(e)

print("=== Testing hardcoded graph ===")
print("Vertex count: ", G.vertex_count())
print("Edge count: ", G.edge_count())

print("Edges incident to u: ", len(list(G.incident_edges(u))))
print("Edges incident to v: ", len(list(G.incident_edges(v))))

print("Vertices of G: ", [v.element().__str__() for v in G.vertices()])
print("Edges of G: ", [e.element().__str__() for e in G.edges()])
# Test DFS
print("DFS test:")
dfs_discovered = {u: None}
Traversal.DFS(G, u, dfs_discovered)
# Print vertices of path
path = Traversal.construct_vertex_path(u, x, dfs_discovered)
result = [vertex.element() for vertex in path]
print("Vertices in u-x path:")
print(*result, sep=",")

# Print edges of path
print("Edges in u-x path:")
path = Traversal.construct_edge_path(u, x, dfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")

# Test BFS
print("BFS test:")
bfs_discovered = {u: None}
Traversal.BFS(G, u , bfs_discovered)
# Print vertices of path.
path = Traversal.construct_vertex_path(u, x, bfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")
# Print edges of path.
path = Traversal.construct_edge_path(u, x, bfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")

print("\n")

"""
    === Test reading graph from csv file ===
"""
print("=== Testing reading graph from csv file ===")
del dfs_discovered
del bfs_discovered
# exit(1)

G = Graph.read_from_csv("../graph_files/g1.csv", directed=False)
print("Vertices of G: ", [v.element() for v in G.vertices()])

root = G.get_vertex('1')
# Test DFS
dfs_discovered = {root: None}
Traversal.DFS(G, u, dfs_discovered)
# Print vertices of path
path = Traversal.construct_vertex_path(u, w, dfs_discovered)
result = [vertex.element() for vertex in path]
print(*result, sep=",")
# Print edges of path
path = Traversal.construct_edge_path(u, w, dfs_discovered)
result = [vertex.element() for vertex in path]
print(*result, sep=",")

# Test BFS
bfs_discovered = {root: None}
Traversal.BFS(G, u , bfs_discovered)
# Print vertices of path.
path = Traversal.construct_vertex_path(u, w, bfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")
# Print edges of path.
path = Traversal.construct_edge_path(u, w, bfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")