

# === Vertex Class ===
class Vertex:
    """ Represents vertex of graph """

    __slots__ = '_element'

    def __init__(self, element):
        """ Associate object to this vertex as element"""
        self._element = element

    def element(self):
        """ Return element associated to vertex.  """
        return self._element

    def __hash__(self):
        """ The key that uniquely identifies this vertex. """
        return hash(id(self))

# === Edge Class ===
class Edge:
    """ Represents an edge of graph """

    """ head of edge, tail of edge, item associated to edge. """
    __slots__ = '_from', '_to', '_element'

    def __init__(self, u, v, element):
        self._from = u
        self._to = v
        self._element = element

    def endpoints(self):
        """ Returns (u,v) tuple of edge endpoints """
        return (self._from, self._to)

    def opposite(self, v):
        """ Returns other endpoint of edge. """
        return self._to if v is self._from else self._from

    def element(self):
        return self._element

class Graph:
    """ An implementation of a graph using an adjacency map. """

    """ A map where:
            keys are vertices, and
            values are secondary incident map (stores edges incident to vertex.)
    """
    __slots__ = '_outgoing', '_incoming'

    def __init__(self, directed=False):
        self._outgoing = {}
        # Graph is undirected, _incoming points to _outgoing.
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """ Return True if directed, False if undirected. """
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """ Returns the number of vertices in the graph. """
        return len(self._outgoing)

    def vertices(self):
        """ Returns an iteration of all vertices of the graph. """
        return self._outgoing.keys()

    def edge_count(self):
        """ Returns the number of edges present in graph. """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)

        # If graph is undirected, edges are counted twice in the above.
        return total if self.is_directed() else total // 2

    def edges(self):
        """ Returns all edges of graph. """
        result = set() # Set will avoid adding double edges for undirected graph.
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """ Return edge from u to v, None if d.n.e."""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """ Returns the number of outgoing edges incident to vertex v. If graph is directed, outgoing should
        be set to False if degree of incoming edges are wanted."""

        adj = self._outgoing if outgoing else self._incoming
        return len(adj)

    def incident_edges(self, v, outgoing=True):
        """ Returns all outgoing or incoming edges incident to vertex v. Outgoing should be set to
        False if incoming edges are wanted.
        """

        adj = self._outgoing if outgoing else self._incoming

        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """ Insert and return a new vertex with element x."""
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v


    def insert_edge(self, u, v, x=None):
        """ Insert and return a new edge with element x."""
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_vertex(self, v):
        """ Remove a vertex and return its element."""
        result = Vertex.element(v)

        # remove vertex by removing all edges incident to it
        self._outgoing[v] = None
        if self.is_directed():
            self._incoming[v] = None
        return result

    def remove_edge(self, e):
        """ Remove an edge and return its element."""
        result = Edge.endpoints(e)
        u = result[0]
        v = result[1]
        # Remove endpoint vertices
        self._outgoing[u][v] = None
        self._incoming[v][u] = None

        return result






































