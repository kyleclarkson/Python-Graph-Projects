

def DFS(g, u, discovered):
    """ DFS traversal on undiscovered portion of graph G, from vertex u.

        Note: 'discovered' is a dictionary that maps each vertex v to edge (u,v) that
        made made v discovered (i.e. v was discovered from u.)
        The root of the DFS tree points to None.
     """

    for edge in g.incident_edges(u):
        v = edge.opposite(edge)

        if v not in discovered:
            discovered[v] = DFS(g, v, discovered)

def DFS_construct_path(u, v, discovered):
    """ Return u-v path from DFS search. Is empty if none exists. """

    path = []
    if v in discovered:
        path.append(v)
        v_prime = v
        while parent is not u:
            e = discovered[v_prime]
            parent = e.opposite(v_prime)
            path.append(parent)
            v_prime = parent
        # reverse path so it is u to v.
        path.reverse()
    return path