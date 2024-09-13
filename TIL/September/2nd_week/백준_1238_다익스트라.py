import heapq

def dijkstra(start):
    distance = [int(1e9) for _ in range(node_cnt+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        tmp_distance, node_now = heapq.heappop(q) #거리가 가장 가까운 노드를 꺼냄
        if distance[node_now] >= tmp_distance: # distance에 있는 값보다 작아야 갱신할 필요가 있음
            for next_node, plus_distance in graph[node_now]:
                if tmp_distance + plus_distance < distance[next_node]: # distance에 있는 값보다 작다면
                    distance[next_node] = tmp_distance + plus_distance # distance 갱신
                    heapq.heappush(q, (tmp_distance + plus_distance, next_node)) # 최소 거리 갱신을 위해 거리 더한 값에 노드를 힙큐에 넣음
    return distance

node_cnt, edge, X = map(int, input().split())
graph = [[] for _ in range(node_cnt+1)]

for _ in  range(edge):
    start, goal, cost = map(int, input().split())
    graph[start].append([goal, cost])

ans = dijkstra(X) # 파티 장소에서 각자 집으로 가는 걸 알 수 있다.
ans[0] = 0
print(ans)

for i in range(1, node_cnt+1): #각 노드들이 파티에 갈려고 하는 로직
    if i != X:
        res = dijkstra(i)
        ans[i] += res[X]
print(ans)
print(max(ans))