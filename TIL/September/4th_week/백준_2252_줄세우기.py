'''

다음 노드를 다음 거에 넣으면 되긴 함
근데 문제 그 다음 노드에 넣으면 되는데 만약 존재한다면?
존재 한다면 삭제하고
없다면 그냥 넣자

pop하고 result에 넣을 때에도 이미 있다면 넣지마

result에 넣을 때
이미 있다면? -> 넣지 않고
존재하지 않는다면 -> 그냥 넣는다
'''

from collections import deque

def topology():
    result = []
    visited = [False for _ in range(n+1)]
    idx_store_list = [0 for _ in range(n+1)]
    q = deque()
    for i in range(1, n+1):
        if indgree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        idx = int(1e9)
        tmp_list = []
        flag = True
        for next_node in student[now]:
            tmp_list.append(next_node)
            if not visited[next_node]:
                result.append(next_node)
                i = len(result) - 1
                visited[next_node] = True
                idx_store_list[next_node] = i
                q.append(next_node)
            else:
                q.append(next_node)
                tmp_idx = idx_store_list[next_node]
                idx = min(idx, tmp_idx)
        if idx == int(1e9): #인덱스 갱신이 안 되면 그냥 첫번째에 넣는다.
            idx = 0
            flag = False
        if not visited[now]:
            result.insert(idx, now)
            visited[now] = True
            idx_store_list[now] = idx
            for i in tmp_list:
                idx_store_list[i] += 1
        else:
            if flag:
                now_node_idx = idx_store_list[now]
                result.remove(now)
                result.insert(idx, now)
                idx_store_list[now] = idx
                for i in tmp_list:
                    idx_store_list[i] += 1


    return result


n, m = map(int, input().split())

student = [[] for _ in range(n+1)]
indgree = [0 for _ in range(n+1)]

for i in range(m):
    small, big = map(int, input().split())
    indgree[big] += 1
    student[small].append(big)

ans = topology()
print(*ans)