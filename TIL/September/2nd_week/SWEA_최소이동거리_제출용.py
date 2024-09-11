


def get_minimum_distance(start):
    global min_cost

    q = []
    q.append((start, 0))

    while q:
        node, cost_sum = q.pop(0)
        for cost, next in graph[node]:
            if cost + cost_sum > min_cost:
                continue
            if next < node:
                continue
            if next == node_cnt:
                min_cost = min(min_cost, cost_sum + cost)
                continue
            q.append((next, cost_sum + cost))


t = int(input())
for tc in range(1, t+1):

    node_cnt, edge = map(int, input().split())

    graph = []
    for i in range(node_cnt + 1):
        graph.append([])

    for i in range(edge):
        a, b, cost = map(int, input().split())
        graph[a].append([cost, b])
        graph[b].append([cost, a])

    min_cost = int(1e9)

    get_minimum_distance(0)
    print(f'#{tc} {min_cost}')
