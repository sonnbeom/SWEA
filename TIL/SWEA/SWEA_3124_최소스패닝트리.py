def find_parent(parent ,x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

node, edge = map(int, input().split())
graph = []
for i in range(edge):
    a, b, cost = map(int, input().split())
    graph.append([cost, a, b])
graph.sort()
parent = []
for i in range(edge+1):
    graph.append([i])
costs = 0
for i in range(edge):
    cost, a, b = graph[i]
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent ,b)
    if a_parent != b_parent:
        union(parent, a_parent, b_parent)
        costs += cost
print(costs)


