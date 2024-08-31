'''
input 예시
n = 5 m = 4
3 4
1 4
2 3
4 3

예상 출력 값: [False, True, True, True, True, False]

n = 5 m = 4
3 4
1 4
2 3
4 5

예상 출력 값: [False, True, True, True, True, True]

'''

from collections import deque
n = 5
m = 4
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a , b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        for node_in_list in arr[node]:
            if not visited[node_in_list]:
                q.append(node_in_list)
                visited[node_in_list] = True
bfs(1)

print(visited)


