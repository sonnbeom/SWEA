def find_parent(now):
    if parent[now] != now:
        parent[now] = find_parent(parent[now])
    return parent[now]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

node_cnt, edge = map(int, input().split())

parent = [0 for _ in range(node_cnt+1)]
for i in range(1, node_cnt+1):
    parent[i] = i

graph = []
for i in range(edge):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

total_cost = 0
cnt = 0
for cost, a, b in graph:
    if find_parent(a) != find_parent(b):
        union(a, b)
        total_cost += cost
        cnt += 1
        if cnt == node_cnt-1:
            break

print(total_cost)