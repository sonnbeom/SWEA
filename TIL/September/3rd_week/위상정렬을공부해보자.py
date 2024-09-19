from collections import deque

node_cnt, edge = map(int, input().split())
# 모든 노드에 대한 진입 차수는  0으로 초기화
indegree = [0 for _ in range(node_cnt+1)]
graph = [[] for _ in range(node_cnt+1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b) # 노드 A에서 B로 이동 가능
    indegree[b] += 1 # 진입 차수를 1 증가

def topology_sort():
    result = []
    q = deque()

    # 처음 시작 시에 진입차수가 0인 노드를 큐에 삽입입
    for i in range(1, node_cnt+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # 해당 노드와 연결된 노드의 진입차수를 감소시켜줌
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수가 0이 되는 노드들은 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    print(result)

topology_sort()