import queue

adj_list = []
distances = []
visited = []
def main():
    global distances, visited
    n = int(input())
    while n:
        nodes = int(input())
        distances = [float('inf')] * nodes
        visited = [False] * nodes
        for i in range(nodes):
            number_of_edges_of_current_node = int(input())
            edge_list = []
            for j in range(number_of_edges_of_current_node):
                node, weight = map(int, input().split(' '))
                edge_list.append((node - 1, weight))
            adj_list.append(edge_list)
        djikstra(0)
        print_all_path_costs()
        n -= 1


def djikstra(source_node):
    distances[source_node] = 0
    pq = queue.PriorityQueue()
    pq.put((0, source_node))
    while not pq.empty():
        dist_to_a, node_a = pq.get()
        if visited[node_a]: continue
        visited[node_a] = True
        for edge in adj_list[node_a]:
            node_b, weight = edge[0], edge[1]
            if distances[node_a] + weight < distances[node_b]:
                distances[node_b] = distances[node_a] + weight
                pq.put((distances[node_b], node_b))


def print_all_path_costs():
    for i in range(len(distances)):
        print("1 to %s: %s" % (i + 1, distances[i]))

if __name__ == '__main__':
    main()