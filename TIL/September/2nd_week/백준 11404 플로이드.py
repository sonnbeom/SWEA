INF = int(1e9)

node_cnt = int(input())
m = int(input())

graph = [[INF for _ in range(node_cnt+1)] for _ in range(node_cnt+1)] # 0번째는 비워!

for i in range(1, node_cnt+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(cost, graph[a][b])

for k in range(1, node_cnt+1):
    for a in range(1, node_cnt+1):
        for b in range(1, node_cnt+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, node_cnt+1):
    for b in range(1, node_cnt+1):
        if graph[a][b] == INF:
            print('0', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()