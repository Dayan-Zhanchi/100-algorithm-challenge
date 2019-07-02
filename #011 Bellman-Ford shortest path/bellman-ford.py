class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight


edge_list = []
distances = []


def main():
    global edge_list, distances
    n = int(input())
    while n:
        nodes = int(input())
        edges = int(input())
        distances = [float('inf')] * nodes
        distances[0] = 0
        for _ in range(edges):
            edge = list(map(int, input().split(' ')))
            edge_list.append(Edge(edge[0], edge[1], edge[2]))

        if bellman_ford() == 1:
            print_all_path_costs()
        edge_list = []
        n -= 1
    return


def print_all_path_costs():
    for i in range(len(distances)):
        print("1 to %s: %s" % (i + 1, distances[i]))


def bellman_ford():
    for _ in range(len(edge_list)):
        for e in edge_list:
            distances[e.b - 1] = min(distances[e.b - 1], e.weight + distances[e.a - 1])

    # check for negative cycles
    for e in edge_list:
        if distances[e.a - 1] + e.weight < distances[e.b - 1]:
            return 0
    return 1


if __name__ == '__main__':
    main()
