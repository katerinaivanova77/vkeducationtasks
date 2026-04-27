n, m = map(int, input().split())
def tree(graph, n):
    visited = [False] * (n + 1)
    def dfs(vertex, parent):
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False
    has_cycle = dfs(1, -1)
    if has_cycle:
        return False
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            return False
    return True
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(tree(graph, n))

#Проверяется связность графа и отсутствие циклов, а дерево это и есть неориентированный связный граф без циклов