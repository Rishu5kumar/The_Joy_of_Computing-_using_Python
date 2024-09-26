# Any two people of the world are separated on an average of six people

# Graph is a group of points and lines(edges) between the points(nodes)

# connected graph:- Atleast one path exists between any two nodes
'''
Edge list representation:-

An edge list is a data structure used to represent a graph as a list of its edges. Each edge is defined by its start and end vertices, typically represented as a pair of numbers or vertices. The edge list can be viewed as a two-column matrix, where each row represents an edge with its source and destination vertices.

G=(1,2) (2,3) (3,4)
so edge list are:- 1 2, 2 3, 3 4
'''

import networkx as nx
import numpy

G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes)
print(N)

spll = []
for u in N:
    for v in N:
        if u!=v:
            l = nx.shortest_path_length(G,u,v)
            print("Shortest path between",u,"and",v,"is of length:",l)
            spll.append(l)

min_spl = min(spll)
max_spl = max(spll)
avg_spl = numpy.average(spll)

print("Minimum shortest path length:",min_spl)
print("Maximum shortest path length:",max_spl)
print("Average shortest path length:",avg_spl)
