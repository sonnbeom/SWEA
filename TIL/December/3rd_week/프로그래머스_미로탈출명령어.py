# 격자의 가는 법 => dfs로 간다 =>
# BFS 로 간다 => 각 숫자에서 가장 적은 숫자를 가져온다.
#
from collections import deque
# d(아래) l(왼쪽)  r(우측) u(위)
def bfs(miro, k, sy, sx, n, m):
    answer = []
    dy = [1, 0, 0, -1]
    dx = [0, -1, 1, 0]
    q = deque()
    q.append((sy, sx, 0, ''))  # y, x, 이동 거리, 문자열
    while q:
        y, x, d, s = q.popleft()

        if d == k:
            if miro[y][x] == -1:
                answer.append(s)
                continue
            else:
                continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            new_s = s + str(i)
            q.append((ny, nx, d + 1, new_s))
    return answer


def transfer(req):
    answer = ''
    for i in range(len(req)):
        if req[i] == '0':
            answer += 'd'
        elif req[i] == '1':
            answer += 'l'
        elif req[i] == '2':
            answer += 'r'
        else:
            answer += 'u'
    return answer


def get_answer(req):
    if len(req) == 0:
        return "impossible"
    storage = []
    for r in req:
        temp = []
        for i in range(len(r)):
            temp.append(r[i])
        storage.append(temp)
    storage.sort()
    answer = storage[0]
    return transfer(answer)

def solution(n, m, x, y, r, c, k):
    miro = [[0 for _ in range(m)] for _ in range(n)]

    miro[x - 1][y - 1] = 1
    miro[r - 1][c - 1] = -1
    answer = bfs(miro, k, x - 1, y - 1, n, m)
    return get_answer(answer)