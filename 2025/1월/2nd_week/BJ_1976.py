def dfs(cost, node, graph, parent, dis, visited, past):
    print(f'cost = {cost} node = {node} past ={past}')
    if visited[node]:
        # print(f'cost = {cost} node = {node} past ={past}')
        dis[past] = max(dis[past], cost)
        return
    for next_node, next_cost in graph[node]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        dfs(cost+next_cost, next_node, graph, parent, dis, visited, node)
        visited[next_node] = False
def func(start, graph, n):
    dis = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for node, cost in graph[start]:
        dfs(cost, node, graph, node, dis, visited, node)
    print(f'start = {start} dis = {dis}')
    dis.sort(reverse=True)
    return dis[0] + dis[1]
def main():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    print(f'graph = {graph}')
    answer = 0
    for i in range(1, n+1):
        if len(graph[i]) <= 2:
            continue
        answer = max(func(i, graph, n), answer)
    return answer
print(main())