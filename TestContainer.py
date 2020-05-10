
class Node:
    """ A container object for vertices of graph. """
    __slots__ = "_label", "_vertex"

    def __init__(self, label):
        self._label = label

    def set_vertex(self, vertex):
        """ Set which vertex this node belongs to. """
        self._vertex = vertex

    def __str__(self):
        return str(self._label)

class Arc:
    """ A container object for edges of graph. """
    __slots__ = "_weight", "_edge"

    def __init__(self, weight=None):
        self._weight = weight

    def set_edge(self, edge):
        """ Set which edge this arc belongs to. """
        self._edge = edge

    def __str__(self):
        return str(self._edge.endpoints()[0].element())+"-"+str(self._edge.endpoints()[1].element())
