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

def dfs(graph, node):
    stack = []
    visited = []

    stack.append(node)

    while stack:
        print("stack: ", stack)
        s = stack.pop(0)
        print(s, end= " ")
    
        for n in graph[s]:
            if n not in visited:
                stack.append(n)
                visited.append(n)
        print("visited: ", visited)

        




dfs(graph, 'A')