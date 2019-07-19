import queue
import random
import networkx as nx


def main():
    graphs = initialize_graphs()
    graph1 = graphs[0]
    graph2 = graphs[1]
    print_final_graph(prims(graph1))
    print_final_graph(prims(graph2))


def prims(graph):
    pq = queue.PriorityQueue()
    visited = [False] * graph.number_of_nodes()
    nodes = list(graph.nodes)
    source_node = nodes[random.randint(0, len(nodes) - 1)] - 1
    pq.put((0, source_node, source_node))
    print(source_node)
    mst = []
    while not all(visited):
        weight, curr_node, prev_adj_node = pq.get()
        if visited[curr_node]: continue
        visited[curr_node] = True
        if curr_node != prev_adj_node:
            mst.append((curr_node, prev_adj_node, weight))
        adj_edges = graph.adj[curr_node + 1]

        for node, weight in adj_edges.items():
            if visited[node - 1]: continue
            pq.put((weight['weight'], node - 1, curr_node))
    return mst


def initialize_graphs():
    # it seems that the networkx graph stores the nodes and edge associations as a dictionary
    # making it work like an adjacency list when trying to retrieve edges connected to a given node
    # https://github.com/networkx/networkx/blob/master/networkx/classes/graph.py on line 351 and the function adj, the description of the structure is given
    graphs = []
    graph1 = nx.Graph()
    graph1.add_weighted_edges_from([(1, 2, 3), (1, 5, 5)])
    graph1.add_weighted_edges_from([(2, 3, 5), (2, 5, 6)])
    graph1.add_weighted_edges_from([(3, 4, 9), (3, 6, 3)])
    graph1.add_weighted_edges_from([(4, 6, 7)])
    graph1.add_weighted_edges_from([(5, 6, 2)])

    graph2 = nx.Graph()
    graph2.add_weighted_edges_from([(1, 2, 2), (1, 3, 3), (1, 4, 7)])
    graph2.add_weighted_edges_from([(2, 3, 5), (2, 5, 4)])
    graph2.add_weighted_edges_from([(3, 4, 9), (3, 5, 8)])
    graph2.add_weighted_edges_from([(4, 5, 3)])

    graphs.append(graph1)
    graphs.append(graph2)
    return graphs


def print_final_graph(graph):
    [print("(%s, %s, %s)" % (x + 1, y + 1, z)) for x, y, z in graph]
    tot_edge_cost = 0
    for _, _, edge_cost in graph:
        tot_edge_cost += edge_cost
    print("MST edge cost: %s" % tot_edge_cost)


if __name__ == '__main__':
    main()
