import sys

sys.setrecursionlimit(10 ** 8)
# d(아래) l(왼쪽)  r(우측) u(위)
dy = [1, 0, 0, -1]
dx = [0, -1, 1, 0]
alphabet = ['d', 'l', 'r', 'u']
response = ''


def dfs(n, m, y, x, ty, tx, k, cnt, answer):
    global response
    if k < cnt + abs(y - ty) + abs(x - tx):
        return
    if y == ty and x == tx and cnt == k:
        response = answer
        return
    for i in range(4):
        if is_valid(x + dx[i], y + dy[i], n, m) and not response:
            dfs(n, m, y + dy[i], x + dx[i], ty, tx, k, cnt + 1, answer + alphabet[i])


def is_valid(nx, ny, n, m):
    return 0 <= nx < m and 0 <= ny < n


def solution(n, m, x, y, r, c, k):
    miro = [[0 for _ in range(m)] for _ in range(n)]
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"
    miro[x - 1][y - 1] = 1
    miro[r - 1][c - 1] = -1
    dfs(n, m, x - 1, y - 1, r - 1, c - 1, k, 0, "")
    return response