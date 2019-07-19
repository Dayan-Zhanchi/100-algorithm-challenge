# Prims algorithm for minimal spanning trees
[Prims algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) is used for finding the minimal spanning tree of a weighted graph, which is a subgraph of the original graph that contains all the vertices
of the graph, but not necessarily all the edges, and that has the minimum edge cost. It makes use of a priority queue, which makes most of the work, by prioritizing edges that are lower than the 
others, and so one only needs to iterate through all the adjacent nodes of a given node and add them to the priority queue and mark visited nodes. The stop condition for my implementation was when 
all vertices had been visited. It resembles Djikstra, except that at each point in the iteration it finds the minimum edge cost with the help of the priority queue, and not the minimum distance from 
the current node.

If you don't use a priority queue, then some work has to be done to find the minimum edge cost for a given node, which can be done by adding nodes adjacent to the current node at each 
iteration to a list and find the minimum edge cost in the list. 

When using a fibonacci heap and adjacency list, which I used, the time complexity is O(|E| + |V| * log|V|).

![Prims algorithm in process](PrimAlgDemo.gif)