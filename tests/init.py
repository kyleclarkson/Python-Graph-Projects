from Graph import Graph
from TestContainer import Node, Arc

def Test_Undirected():
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
    Graph.DFS(G, u, dfs_discovered)
    # Print vertices of path
    path = Graph.construct_vertex_path(u, x, dfs_discovered)
    result = [vertex.element() for vertex in path]
    print("Vertices in u-x path:")
    print(*result, sep=",")

    # Print edges of path
    print("Edges in u-x path:")
    path = Graph.construct_edge_path(u, x, dfs_discovered)
    result = [edge.element() for edge in path]
    print(*result, sep=",")

    # Test BFS
    print("BFS test:")
    bfs_discovered = {u: None}
    Graph.BFS(G, u , bfs_discovered)
    # Print vertices of path.
    path = Graph.construct_vertex_path(u, x, bfs_discovered)
    result = [edge.element() for edge in path]
    print(*result, sep=",")
    # Print edges of path.
    path = Graph.construct_edge_path(u, x, bfs_discovered)
    result = [edge.element() for edge in path]
    print(*result, sep=",")

    print("\n")

def Test_Directed():
    G = Graph(directed=True)

    vertices = {}
    # Create vertices
    for i in range(6):
        v = G.insert_vertex(Node(i))
        vertices[i] = v
        v.element().set_vertex(v)

    # Create edges
    # list of edges
    edges = [(0,1), (0,2),
             (1,2), (1,3),
             (2,3),
             (3,4), (3,5),
             (4,5)]

    for e in edges:
        edge = G.insert_edge(vertices[e[0]], vertices[e[1]], Arc())
        edge.element().set_edge(edge)

    print("=== Testing hardcoded graph ===")
    print("Vertex count: ", G.vertex_count())
    print("Edge count: ", G.edge_count())

    u = vertices[0]
    v = vertices[5]
    print("Edges incident to u: ", len(list(G.incident_edges(u))))
    print("Edges incident to v: ", len(list(G.incident_edges(v))))


    print("Vertices of G: ", [v.element().__str__() for v in G.vertices()])
    print("Edges of G: ", [e.element().__str__() for e in G.edges()])
    # Test DFS
    print("DFS test:")
    dfs_discovered = {u: None}
    Graph.DFS(G, u, dfs_discovered)
    # Print vertices of path
    path = Graph.construct_vertex_path(u, v, dfs_discovered)
    result = [vertex.element() for vertex in path]
    print("Vertices in 0-5 path:")
    print(*result, sep=",")

    # Print edges of path
    print("Edges in 0-5 path:")
    path = Graph.construct_edge_path(u, v, dfs_discovered)
    result = [edge.element() for edge in path]
    print(*result, sep=",")

    # Test BFS
    print("BFS test:")
    bfs_discovered = {u: None}
    Graph.BFS(G, u, bfs_discovered)
    # Print vertices of path.
    path = Graph.construct_vertex_path(u, v, bfs_discovered)
    result = [edge.element() for edge in path]
    print(*result, sep=",")
    # Print edges of path.
    path = Graph.construct_edge_path(u, v, bfs_discovered)
    result = [edge.element() for edge in path]
    print(*result, sep=",")

    print("\n")

def Test_DAG():
    G = Graph(directed=True)

    vertices = {}
    # Create vertices
    for i in range(6):
        v = G.insert_vertex(Node(i))
        vertices[i] = v
        v.element().set_vertex(v)

    # Create edges
    # list of edges
    edges = [(0,1), (0,2),
             (1,2), (1,3),
             (2,3),
             (3,4), (3,5),
             (4,5)]

    for e in edges:
        edge = G.insert_edge(vertices[e[0]], vertices[e[1]], Arc())
        edge.element().set_edge(edge)

    print("=== Testing DAG graph ===")
    print("Vertex count: ", G.vertex_count())
    print("Edge count: ", G.edge_count())

    print("Length of toposort: ", len(Graph.toplogical_sort(G)))
    assert len(Graph.toplogical_sort(G)) == G.vertex_count(), "Graph contains topo ordering!"
    edge = G.insert_edge(vertices[4],vertices[3], Arc())
    edge.element().set_edge(edge)

    print("Toposort length: ", len(Graph.toplogical_sort(G)))
    assert len(Graph.toplogical_sort(G)) != G.vertices(), "Graph does not contain topo ordering!"


if __name__ == '__main__':
    Test_DAG()
    # Test_Directed()
    # Test_Undirected()

"""
    === Test reading graph from csv file ===
"""
# print("=== Testing reading graph from csv file ===")
# del dfs_discovered
# del bfs_discovered
# # exit(1)
#
# G = Graph.read_from_csv("../graph_files/g1.csv", directed=True)
# print("Vertices of G: ", [v.element() for v in G.vertices()])
#
# root = G.get_vertex('1')
# # Test DFS
# dfs_discovered = {root: None}
# Traversal.DFS(G, u, dfs_discovered)
# # Print vertices of path
# path = Traversal.construct_vertex_path(u, w, dfs_discovered)
# result = [vertex.element() for vertex in path]
# print(*result, sep=",")
# # Print edges of path
# path = Traversal.construct_edge_path(u, w, dfs_discovered)
# result = [vertex.element() for vertex in path]
# print(*result, sep=",")
#
# # Test BFS
# bfs_discovered = {root: None}
# Traversal.BFS(G, u , bfs_discovered)
# # Print vertices of path.
# path = Traversal.construct_vertex_path(u, w, bfs_discovered)
# result = [edge.element() for edge in path]
# print(*result, sep=",")
# # Print edges of path.
# path = Traversal.construct_edge_path(u, w, bfs_discovered)
# result = [edge.element() for edge in path]
# print(*result, sep=",")