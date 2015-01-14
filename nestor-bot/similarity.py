""" Thanks to the code to cc_pattern examples from Tom DeSmedt"""

from pattern.graph import Graph
from pattern.db import Datasheet, pd
from pattern.graph import MODULE  # path to pattern/graph/commonsense.csv
data = pd(MODULE, "commonsense.csv")
data = Datasheet.load(data)


# Create the graph:
g = Graph()
for concept1, relation, concept2, context, weight in data:
    g.add_node(concept1)
    g.add_node(concept2)
    g.add_edge(concept1, concept2, type=relation, weight=min(int(weight) * 0.1, 1.0))

cache = {} # Cache results for faster reuse.

PROPERTIES = [e.node1.id for e in g.edges if e.type == 'is-property-of']
PROPERTIES = dict.fromkeys(PROPERTIES, True)


def field(node, depth=3, fringe=2):
    """ Returns the semantic field of the given node as a list of nodes.
    """
    def traversable(node, edge):
        return edge.node2 == node and edge.type == 'is-a'
    g = node.graph.copy(nodes=node.flatten(depth, traversable))
    g = g.fringe(depth=fringe)
    g = [node.graph[n.id] for n in g if n != node]
    return g


def halo(node, depth=2):
    """ Returns the halo of the given node as a list of nodes.
    """
    return node.flatten(depth)


def properties(node):
    """ Returns a list of nodes that are properties of the given node,
        sorted by betweenness centrality.
    """
    if node.id in cache:
        return cache[node.id]
    g = node.graph.copy(nodes=halo(node))
    p = (n for n in g.nodes if n.id in PROPERTIES)
    p = reversed(sorted(p, key=lambda n: n.centrality))
    p = [node.graph[n.id] for n in p]
    cache[node.id] = p
    return p


def similarity(node1, node2, k=3):
    g = node1.graph
    h = lambda id1, id2: 1 - int(g.edge(id1, id2).type == 'is-property-of')
    w = 0.0
    for p1 in properties(node1)[:k]:
        for p2 in properties(node2)[:k]:
            p = g.shortest_path(p1, p2, heuristic=h)
            w += 1.0 / (p is None and 1e10 or len(p))
    return w / k


def nearest_neighbors(node, candidates=[], k=3):
    """ Returns the list of candidate nodes sorted by similarity.
    """
    w = lambda n: similarity(node, n, k)
    return sorted(candidates, key=w, reverse=True)


def semantic_similarity(name):
    return nearest_neighbors(g[name], field(g["person"]))[:3]
