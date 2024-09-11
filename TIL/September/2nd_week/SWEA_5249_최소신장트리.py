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
node_cnt, edge  = map(int,input().split())
graph = []
for i in range(edge):
    a, b, cost = map(int,input().split())
    graph.append([cost, a, b])

parent = [0 for _ in range(node_cnt+1)]
for i in range(node_cnt+1):
    parent[i] = i

total_cost = 0
graph.sort()
for i in range(edge):
    cost, a, b = graph[i]
    if find_parent(a) != find_parent(b):
        union(a, b)
        total_cost += cost
print(total_cost)