graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': [],
}

def bfs(graph, node):
    visited = []
    queue = []

    queue.append(node)
    visited.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end= " \n")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
        print(queue)


bfs(graph, 'A' )


