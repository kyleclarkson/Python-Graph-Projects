from copy import deepcopy

def DFS(g, u, discovered):
    """ DFS traversal on undiscovered portion of graph G, from vertex u.

        Note: 'discovered' is a dictionary that maps each vertex v to edge (u,v) that
        made v discovered (i.e. v was discovered from u.)
        The root of the DFS tree points to None.
     """

    for edge in g.incident_edges(u):
        v = edge.opposite(u)

        if v not in discovered:
            discovered[v] = edge
            DFS(g, v, discovered)

def construct_vertex_path(u, v, discovered):
    """ Return u-v vertex path from DFS search. Is empty if none exists. """

    path = []
    if v in discovered:
        path.append(v)
        v_current = v
        while v_current is not u:
            edge = discovered[v_current]
            parent = edge.opposite(v_current)
            path.append(parent)
            v_current = parent
        # reverse path so it is u to v.
        path.reverse()
    return path

def construct_edge_path(u, v, discovered):
    """ Return u-v edge path from DFS search. Is empty if none exists. """
    path = []
    if v in discovered:
        v_current = v
        while v_current is not u:
            edge = discovered[v_current]
            path.append(edge)
            parent = edge.opposite(v_current)
            v_current = parent

        path.reverse()
    return path

def BFS(g, s, discovered):
    """ BFS traversal on undiscovered portion of graph G, from vertex s.

        Note: 'discovered; is a dictionary that maps each vertex v to edge (u,v) that made
        v discovered (i.e. v was discovered from u.)
        The root of the BFS tree points to None.
    """
    # First level contains s only.
    current_level = [s]

    while len(current_level) > 0:
        next_level = []
        for u in current_level:
            for edge in g.incident_edges(u):
                v = edge.opposite(u)
                # Check that v is no discovered yet.
                if v not in discovered:
                    discovered[v] = edge
                    next_level.append(v)

        current_level = next_level

def floyd_warshall(g):
    """ Returns the transitive closure of input graph g. """

    closure = deepcopy(g)
    vertices = list(closure.vertices())
    n = len(vertices)

    for k in range(n):
        for i in range(n):
            # Check not loop edge and edge exists.
            if i != k and closure.get_edge(vertices[i], vertices[k]) is not None:
                for j in range(n):
                    # Check edge (k, j) exists
                    if i != j != k and closure.get_edge(vertices[k], vertices[k]) is not None:
                        # Add edge (i,j) to closure if  not present
                        if closure.get_edge(vertices[i], vertices[j]) is not None:
                            closure.insert_edge(vertices[i], vertices[j])
    return closure