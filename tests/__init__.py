from Graph import Graph
import Traversal

# Test creating graph
G = Graph()
u = G.insert_vertex('u')
v = G.insert_vertex('v')
w = G.insert_vertex('w')
x = G.insert_vertex('x')

G.insert_edge(u,v)
G.insert_edge(v,w)
G.insert_edge(u,x)
G.insert_edge(x,w)

print("=== Testing hardcoded graph ===")
print("Vertex count: ",G.vertex_count())
print("Edge count: ", G.edge_count())

print("Edges incident to u: ", len(list(G.incident_edges(u))))
print("Edges incident to v: ", len(list(G.incident_edges(v))))

print("Vertices of G: ", [v.element() for v in G.vertices()])
# Test DFS
print("DFS test:")
dfs_discovered = {u: None}
Traversal.DFS(G, u, dfs_discovered)
# Print vertices of path
path = Traversal.construct_vertex_path(u, w, dfs_discovered)
result = [vertex.element() for vertex in path]
print("Vertices in u-w path:")
print(*result, sep=",")

# Print edges of path
print("Edges in u-w path:")
path = Traversal.construct_edge_path(u, w, dfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")

# Test BFS
print("BFS test:")
bfs_discovered = {u: None}
Traversal.BFS(G, u , bfs_discovered)
# Print vertices of path.
path = Traversal.construct_vertex_path(u, w, bfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")
# Print edges of path.
path = Traversal.construct_edge_path(u, w, bfs_discovered)
result = [edge.element() for edge in path]
print(*result, sep=",")

print("\n")

"""
    === Test reading graph from csv file ===
"""
print("=== Testing reading graph from csv file ===")

exit(1)

G = Graph.read_from_csv("../graph_files/g1.csv")
print("Vertices of G: ", [v.element() for v in G.vertices()])

root = G.get_vertex('1')
print(type(root))
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