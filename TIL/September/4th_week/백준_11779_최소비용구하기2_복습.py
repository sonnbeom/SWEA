import heapq

def dijkstra(start):
    total_cost = [int(1e9) for _ in range(node_cnt+1)]
    total_cost[start] = 0

    q = []
    heapq.heappush(q, (0, start)) # 출발 노드, 거리

    while q:
        cost, node = heapq.heappop(q)
        if cost > total_cost[node]:
            continue
        for next_node, plus_cost in graph[node]:
            tmp_cost = plus_cost + cost
            if tmp_cost < total_cost[next_node]:
                total_cost[next_node] = tmp_cost
                prev_node_list[next_node] = node
                heapq.heappush(q, (tmp_cost, next_node))
    return total_cost


node_cnt = int(input())
edge = int(input())

graph = [[] for _ in range(node_cnt+1)]

for i in range(edge):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start, target = map(int, input().split())

prev_node_list = [0 for _ in range(node_cnt+1)]
path = [target]
prev_node = target
total_cost = dijkstra(start)
while prev_node != start:
    prev_node = prev_node_list[prev_node]
    path.insert(0, prev_node)

print(total_cost[target]) # 타겟 지점까지 최소 비용
print(len(path)) # 도시 갯수
print(*path)

