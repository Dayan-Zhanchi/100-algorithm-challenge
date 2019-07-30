# Kruskal
[Kruskal](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) can also be used to find a minimum spanning tree. It runs in O(m * log n), where m is the number of edges and n the number of nodes.
Unlike Prims that uses a priority queue to sort the edges and greedily pick the edge with the lowest cost, Kruskal uses a disjoint set data structure called union find to keep track of the nodes. The
 edges
have to be sorted first in O(m * log m) with for example merge sort and then for each edge add to the union find if they don't have the same root. This way the union find makes sure that nodes already
 stored will not be
added, and since the algorithm also greedily picks out the edge with the lowest cost, a mst is guaranteed to be found.

![Kruskal visualization](KruskalDemo.gif)