'''
1. bfs를 돌아서

1이 나온다 ->
좌우상하에 0이 없다면 1로 둘러쌓인 것임 고로 0으로 처리리
아니라면 idx 처리

2. 다시 전체 탐색을 돌아서
좌, 우, 상, 하를 돈다.
범위 체크를 하면서
거리를 재는데 2 이상이면 멈춘다
거리, 출발 노드, 도착 노드를 리스트에 담는다

3. 유니온 파인드 시전

4. 최소 비용 카운트, 출발 노드, 각 노드를 넣고 for문을 돌며 체크
'''
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
num = 1
def bfs(ty, tx):
    q = deque()
    q.append((ty, tx))
    visited[ty][tx] = True
    land[ty][tx] = num
    while q:
        y, x = q.popleft()
        zero_cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 인덱스 체크
            if not(0 <= nx < M and 0 <= ny < N):
                continue
            # 주위 0 체크
            if land[ny][nx] == 0:
                zero_cnt += 1

            if land[ny][nx] != 0 and not visited[ny][nx]:
                land[ny][nx] = num # 노드 번호 지정
                q.append((ny, nx))
                visited[ny][nx] = True
        # 주위의 0이 없으면 거리를 측정할 공간이 아님
        if zero_cnt == 0:
            land[y][x] = 0

def get_bridge(y, x):
    o_y = y
    o_x = x
    self = land[y][x]
    for i in range(4):
        distance = 0
        y = o_y
        x = o_x
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= nx < M and 0 <= ny < N):
                break
            distance += 1
            y = ny
            x = nx
            if land[ny][nx] == self:
                break
            if distance <= 2 and land[ny][nx] != 0 and land[ny][nx] != self:
                break
            if distance >= 3 and land[ny][nx] != 0:
                node_list.append((distance-1, land[o_y][o_x], land[ny][nx]))
                break


def find_parent(node, parent):

    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)
    return parent[node]

def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def is_connection_bfs(start):
    qu = deque()
    qu.append(start)
    visited_linked[start] = True
    while qu:
        node = qu.popleft()
        for node_in in is_link_node[node]:
            if not visited_linked[node_in]:
                visited_linked[node_in] = True
                qu.append(node_in)

node_list =[]
for y in range(N):
    for x in range(M):
        if not visited[y][x] and land[y][x] != 0:
            bfs(y, x)
            num += 1
for y in range(N):
    for x in range(M):
        if land[y][x] != 0:
            get_bridge(y, x)
parent = [0 for _ in range(num)]
for i in range(1, num):
    parent[i] = i

node_list.sort()
total_cost = 0
is_link_node = [[] for _ in range(num)]
visited_linked = [False for _ in range(num)]
#  비용 측정

for cost, a, b in node_list:
    if find_parent(a, parent) != find_parent(b, parent):
        union(a, b, parent)
        total_cost += cost
        is_link_node[a].append(b)
        is_link_node[b].append(a)


is_connection_bfs(1)
visited_linked[0] = True

if visited_linked.count(False) >= 1:
    print(-1)
else:
    print(total_cost)

