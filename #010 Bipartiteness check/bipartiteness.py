graph = []
colored_vertices = []
visited = []


def main():
    global graph, colored_vertices, visited
    n = int(input())
    while n:
        vertices = int(input())
        colored_vertices = [-1] * vertices
        visited = [False] * vertices
        for _ in range(vertices):
            graph.append(list(map(int, input().split(' '))))
        print(check_bipartiteness(0))
        graph = []
        print(colored_vertices)
        n -= 1


def check_bipartiteness(vertex):
    if visited[vertex]: return True
    visited[vertex] = True
    # check adjacent vertices have same color and what color
    color = colored_vertices[graph[vertex][0]-1]  # retrieve the color of the very first adj vertex to the current vertex
    for adj_vertex in graph[vertex]:
        if colored_vertices[adj_vertex - 1] == -1:
            continue
        if colored_vertices[adj_vertex - 1] != color and colored_vertices[adj_vertex - 1] != -1:
            return False
        color = colored_vertices[adj_vertex - 1]
    # color the current vertex
    if color == -1:
        colored_vertices[vertex] = 0
    else:
        colored_vertices[vertex] = color ^ 1  # XOR toggling the value between 0 and 1
    for adj_vertex in graph[vertex]:
        if not check_bipartiteness(adj_vertex - 1):
            return False

    return True


if __name__ == '__main__':
    main()
