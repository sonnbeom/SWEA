from collections import deque
def can_go(start, goal):
    visited = [False for _ in range(N+1)]
    visited[start] = True
    q = deque()
    q.append(start)
    res = False

    while q:
        node_now = q.popleft()
        if node_now == goal:
            res = True
            break
        for next_node in city[node_now]:
            if next_node == goal:
                res = True
                q.clear()
                break
            else:
                if visited[next_node]:
                    continue
                q.append(next_node)
                visited[next_node] = True

    return res

N = int(input())
M = int(input())
city = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    req = list(map(int,input().split()))
    idx = 1
    for r in req:
        city[i][idx] = r
        idx += 1
plan = list(map(int, input().split()))

for y in range(N+1):
    for x in range(N+1):
        if city[y][x] == 1:
            city[y][x] = x
start = plan[0]

go = False
for i in range(1, M):
    goal = plan[i]
    res_go = can_go(start, goal)
    if not res_go:
        go = False
        break
    if res_go:
        start = goal
        go = True
if go:
    print("YES")
else:
    print("NO")


