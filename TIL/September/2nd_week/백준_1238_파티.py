INF = int(1e9)

node_cnt, edge, x = map(int, input().split())

graph = [[INF for _ in range(node_cnt+1)] for _ in range(node_cnt+1)]

for i in range(edge):
    start, goal, cost = map(int, input().split())
    graph[start][goal] = cost

for i in range(1, node_cnt+1):
    graph[i][i] = 0

for k in range(1, node_cnt+1):
    for a in range(1, node_cnt+1):
        if graph[a][k] == INF:
            continue
        for b in range(1, node_cnt+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

ans = 0
for i in range(1, node_cnt+1):
    ans = max(ans, graph[i][x] + graph[x][i])

print(ans)