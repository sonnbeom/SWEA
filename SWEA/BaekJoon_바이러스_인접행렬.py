from collections import deque

node = int(input())
edge = int(input())

arr = [[0] * (node+1) for _ in range(node+1)]
visited = [False] * (node+1)

for i in range(edge):
    a,b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

q = deque([1])
visited[1] = True
count = 0
while q:
    temp = q.popleft()
    for i in range (1, node+1):
        if not visited[i] and arr[temp][i] == 1:
            q.append(i)
            visited[i] = True
            count += 1
print(count)
    