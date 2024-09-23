'''
다익스트라란?
특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 찾을 때 쓰인다.
+이때 음의 간선을 포함할 수 없다

다익스트라는 다이나믹 프로그래밍이다
왜  why
최단 거리는 여러개의 최단 거리로 이루어져 있기 때문이다.
하나의 최단 거리를 구할 때 이전까지 구했던 최단 거리 정보를 그대로 사용한다.
'''
import heapq

def dijkstra(start):
    distance = [int(1e9) for _ in range(node_cnt+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0)) # 출발, 거리

    while q:
        node_now, tmp_distance = heapq.heappop(q)
        if distance[node_now] >= tmp_distance:
            continue
        for next_node, plus_distance in graph[node_now]:
            distance_sum = tmp_distance + plus_distance
            if distance_sum < distance[next_node]:
                distance[next_node] = distance_sum
                heapq.heappush(q, (next_node, distance_sum))
    return distance

node_cnt, edge, X = map(int(), input().split())
graph = [[] for _ in range(node_cnt+1)]

for _ in range(edge):
    start, goal, cost = map(int, input().split())
    graph[start].append((goal, cost))

ans = dijkstra(X)
ans[0] = 0

for i in range(1, node_cnt+1):
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]

print(max(ans))