import heapq
n, m = map(int, input().split())
def dijkstra(graph, n, start):
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    return distances
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))
start = int(input())
distances = dijkstra(graph, n, start)

for vertex in range(1, n + 1):
    if distances[vertex] == float('inf'):
        print(vertex, "unreachable")
    else:
        print(vertex, distances[vertex])

#Приоритетная очередь нужна, чтобы каждый раз вызывать вершину с минимальным расстоянием быстро. каждое добавление или извелечение из кучи т- O(logV), значит, будет получаться указанная сложность