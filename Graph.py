import math
import pandas as pd
from copy import deepcopy

from TestContainer import Node, Arc

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
        # return self._element().label()
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

    """ 
    _vertices: A map where keys are the vertex elements and values vertices themselves.
    _outgoing/_incoming: maps where:
            keys are vertices, and
            values are secondary incident map (stores edges incident to vertex.)
    """
    __slots__ = '_vertices','_outgoing', '_incoming'

    def __init__(self, directed=False):
        self._vertices = {}
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
        result = set() # 'set' will avoid adding double edges for undirected graph.
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_vertex(self, element):
        """ Return vertex corresponding to element key. """
        return self._vertices.get(element)

    def get_edge(self, u, v):
        """ Return edge from u to v, None if d.n.e."""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """ Returns the number of outgoing edges incident to vertex v. If graph is directed, outgoing should
        be set to False if degree of incoming edges are wanted."""

        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

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
        # Key is vertex element, value is vertex.
        self._vertices[v.element()] = v
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v


    def insert_edge(self, u, v, x=None):
        """ Insert and return a new edge with element x."""
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def remove_vertex(self, v):
        """ Remove a vertex and return its element."""
        result = Vertex.element(v)
        # remove vertex from vertices map
        del self._vertices[v.element()]

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
        del self._outgoing[u][v]
        del self._incoming[v][u]

        return result


    """ 
        =================================
        === Graph Operation Functions ===
        =================================
    """
    @staticmethod
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
                Graph.DFS(g, v, discovered)

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def toplogical_sort(g):
        """
        Returns a list of vertices corresponding to a topological ordering.
        Returns incomplete list of graph contains a cycle.
        """

        topo = []           # The toposort that will be returned, if exists.
        front_vtxs = []     # Vertices with no incoming edges.
        incount = {}

        # For each vertex u, count number of edges going into u.
        for u in g.vertices():
            # Get edges into vertex u
            incount[u] = g.degree(u, False)
            if incount[u] == 0:
                front_vtxs.append(u)

        # Move vertices form front_vtx list to topo list.
        while len(front_vtxs) > 0:
            u = front_vtxs.pop()
            topo.append(u)
            for e in g.incident_edges(u):
                v = e.opposite(u)
                incount[v] -= 1
                if incount[v] == 0:
                    front_vtxs.append(v)

        return topo



    """
    === Utility Methods ===
    """
    @staticmethod
    def read_from_xml(filepath, directed=False):
        """
        :param filepath:
        :param directed:
        :return:
        """
        pass

    @staticmethod
    def read_from_csv(filepath, directed=False):
        """
        :param filepath: The location of the CSV file.
        :param directed: Whether the graph should be directed or not. (This is not
            inferred by contents of file.)
        :return: A graph corresponding to csv file.

        === CSV values ===
        CSV file should be nxn shaped where the graph contains n vertices.
            Vertices will be labeled as strings 1,2, ..., n.
        [i,j] row,col value indicates edge.
            If empty, no edge.
            If contains value (e.g. real number, string) value is set as edge element.
        """
        # Read file as pandas dataframe
        df = pd.read_csv(filepath, header=None)
        array = df.to_numpy()

        result = Graph(directed=directed)
        # Create vertices
        num_vertices = df.shape[0]
        vtx_count = 1

        # Create vertices.
        for idx in range(num_vertices):
            # label vertices 1:n.
            v = result.insert_vertex(Node(str(vtx_count)))
            v.element().set_vertex(v)
            # vertices.append(Vertex(vtx_count))
            vtx_count += 1

        # Create edges.
        for i, j in [(i, j) for i in range(len(array)) for j in range(len(array[i]))]:
            if not math.isnan(array[i, j]):
                # Add edge (i,j) with element corresponding to value in array.
                u = result.get_vertex(str(i+1))
                v = result.get_vertex(str(j+1))
                e = result.insert_edge(u, v, Arc())
                e.element().set_edge(e)
        return result
# TODO
#   Test directed graph using manual creation.
#   Test read from csv.








































