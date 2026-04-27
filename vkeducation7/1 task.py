n, m = map(int, input().split())
def cycle(graph, n):
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
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            if dfs(vertex, -1):
                return True
    return False
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(cycle(graph, n))

#Повторное посещение смотрим через массив neighbour