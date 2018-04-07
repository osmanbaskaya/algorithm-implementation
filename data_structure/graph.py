from collections import defaultdict as dd
from random import sample
from itertools import count


class Vertex:

    id_generator = count(0)

    def __init__(self, value):
        self.value = value
        self.id = next(Vertex.id_generator)

    def __repr__(self):
        return "<< {} value={} >>".format(self.id, self.value)

    def __str__(self):
        return "<< {}, value={} >>".format(self.id, self.value)


class Graph:

    def __init__(self, V, E):
        self.V = V
        # create adjacency-list from Edges, E
        self.adj_list = dd(set)
        for v1, v2 in E:
            self.adj_list[v1].add(v2)
            self.adj_list[v2].add(v1)

    def get_neighbors(self, k):
        node_id = k
        if isinstance(k, Vertex):
            node_id = k.id

        return self.adj_list[node_id]


def generate_simple_graph(num_vertices, num_edges):
    V = [Vertex(i) for i in range(num_vertices)]
    vertex_ids = [v.id for v in V]
    E = list(zip(sample(vertex_ids, num_edges), sample(vertex_ids, num_edges)))
    return Graph(V, E)


if __name__ == '__main__':
    G = generate_simple_graph(10, 4)
    print(G.V)
    print(G.adj_list)
    print(G.get_neighbors(6))
