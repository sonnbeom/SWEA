
from collections import defaultdict
import heapq
INF = int(1e9)

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [INF] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight:
            continue
        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                prev_node[adj_node] = node
                heapq.heappush(q, (cost, adj_node))

dijkstra(start)
print(dist[end])

path = [end]
now = end
print(f'prev_node = {prev_node}')
while now != start:
    now = prev_node[now]
    print(f'now = {now}')
    path.append(now)

print(f'path 뒤집기 전 = {path}')
path.reverse()
print(f'path = {path}')
print(len(path))
print(' '.join(map(str, path)))