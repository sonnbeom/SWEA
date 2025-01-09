def decide_cnt(i, sheep, wolf):
    if i == 0:
        return [sheep + 1, wolf]
    else:
        return [sheep, wolf + 1]


def dfs(visited, info, graph, cnt, node):
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        animal = decide_cnt(info[next_node], cnt[next_node][0], cnt[next_node][1])
        sheep = animal[0]
        wolf = animal[1]

        if cnt[next_node][0] - cnt[next_node][1] >= sheep - wolf:
            continue
        cnt[next_node][0] = sheep
        cnt[next_node][1] = wolf
        visited[next_node] = True
        dfs(visited, info, graph, cnt, next_node)
        visited[next_node] = False


def solution(info, edges):
    visited = [False for _ in range(len(info))]
    graph = [[] for _ in range(len(info))]
    cnt = [[0, 0] for _ in range(len(info))]
    cnt[0][0] = 1

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    dfs(visited, info, graph, cnt, 0)
    print(f'cnt = {cnt}')
