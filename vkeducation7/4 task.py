from collections import deque
n, m = map(int, input().split())
def dvud(graph, n):
    colors = [0] * (n + 1)
    for start in range(1, n + 1):
        if colors[start] == 0:
            colors[start] = 1
            queue = deque([start])
            while queue:
                vertex = queue.popleft()
                for neighbor in graph[vertex]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[vertex]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[vertex]:
                        return False
    return True
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(dvud(graph, n))

#Раскраска подходит, так как ребра соединяют вершины двух разных цветов и BFS строит эту раскраску постепено. Если цвета на ребре совпали, это запрещает нам добавлять их в разные доли, а тогда граф не двудольный, что позволяет таким образом проверить весь граф на двудольность.