def main():
    graphs = initialize_graphs()
    sorted_graphs = list(map(lambda x: sorted(x, key=lambda y: y[2]), graphs))

    mst1 = kruskal(sorted_graphs[0])
    mst2 = kruskal(sorted_graphs[1])
    print_final_graph(mst1)
    print_final_graph(mst2)


def kruskal(graph):
    mst = []
    union_find = UnionFind(len(graph))
    for (a, b, cost) in graph:
        if not union_find.same(a, b):
            union_find.unite(a, b)
            mst.append((a, b, cost))

    return mst


def initialize_graphs():
    graph1 = [(1, 2, 3), (1, 5, 5), (2, 3, 5), (2, 5, 6), (3, 4, 9), (3, 6, 3), (4, 6, 7), (5, 6, 2)]
    graph2 = [(1, 2, 2), (1, 3, 3), (1, 4, 7), (2, 3, 5), (2, 5, 4), (3, 4, 9), (3, 5, 8), (4, 5, 3)]

    graphs = [graph1, graph2]
    return graphs


def print_final_graph(graph):
    [print("(%s, %s, %s)" % (x, y, z)) for x, y, z in graph]
    tot_edge_cost = 0
    for _, _, edge_cost in graph:
        tot_edge_cost += edge_cost
    print("MST edge cost: %s" % tot_edge_cost)


class UnionFind:
    def __init__(self, n):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def same(self, a, b):
        return self.__find(a) == self.__find(b)

    def __find(self, x):
        while x != self.link[x]:
            x = self.link[x]
        return x

    def unite(self, a, b):
        a = self.__find(a)
        b = self.__find(b)
        if self.size[a] < self.size[b]:
            a, b = self._swap(a, b)
        self.link[b] = a
        self.size[a] += self.size[b]

    @staticmethod
    def _swap(a, b):
        tmp = a
        a = b
        b = tmp
        return a, b


if __name__ == '__main__':
    main()
