from collections import deque


def get_distance(graph, start, n, summits, intensity):
    temp = int(1e9)
    response = []
    q = deque()
    q.append((start, 0))  # 시작 노드, 비용, 산봉우리인감?
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    while q:
        node, cost = q.popleft()
        if cost > intensity:  # 비용이 인텐시티보다 비쌈
            continue

        for next_node, next_cost in graph[node]:
            if next_cost > intensity:
                continue
            elif visited[next_node]:
                continue
            elif next_node in summits:
                cost = max(cost, next_cost)
                if cost <= temp:
                    response.append((next_node, cost))
                temp = min(temp, cost)
            else:
                visited[next_node] = True
                cost = max(next_cost, cost)
                q.append((next_node, cost))

    return response


def solution(n, paths, gates, summits):
    intensity = int(1e9)
    num = n
    graph = [[] for _ in range(n + 1)]

    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))
    for g in gates:
        res = get_distance(graph, g, n, summits, intensity)
        print(f'res = {res}')
        for node, d in res:
            if d < intensity:
                intensity = d
                num = node
            elif d == intensity:
                num = min(node, num)
    print(f'답은 말이죵 {[num, intensity]}')
    return [num, intensity]


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])