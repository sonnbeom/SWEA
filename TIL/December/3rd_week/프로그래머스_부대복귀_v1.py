from collections import deque


def get_distance(roads, d, start, n):
    if start == d:
        return 0
    response = int(1e9)
    visited = [False for _ in range(len(roads))]
    q = deque()
    q.append((start, 0))  # 시작, 거리
    while q:
        node, cnt = q.popleft()
        if cnt >= response:
            continue
        elif node == d:
            response = min(response, cnt)
        else:
            for i in range(len(roads)):
                r = roads[i]
                if visited[i]:
                    continue
                if r[0] == node:
                    q.append((r[1], cnt + 1))
                    visited[i] = True
                elif r[1] == node:
                    q.append((r[0], cnt + 1))
                    visited[i] = True
    if response == int(1e9):
        return -1
    else:
        return response


def solution(n, roads, sources, destination):
    answer = []
    for source in sources:
        ans = get_distance(roads, destination, source, n)
        answer.append(ans)
    return answer