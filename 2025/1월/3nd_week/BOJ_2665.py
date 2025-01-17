from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def is_range_valid(y, x, n):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

def func(n, ty, tx):
    response = int(1e9)
    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]
    q = deque([[0, 0, 0]]) # y, x, 횟수

    while q:
        y, x, cnt = q.popleft()

        if cnt >= response:
            continue

        if y == ty and x == tx:
            response = min(response, cnt)
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 체크
            if not is_range_valid(ny, nx, n):
                continue
            # 0이면 벽 부수기
            new_cnt = cnt + 1 if arr[ny][nx] == 0 else cnt
            # 기존 값보다 더 비용이 든다면 가지 않는다
            if new_cnt >= dp[ny][nx]:
                continue
            q.append([ny, nx, new_cnt])
            dp[ny][nx] = min(dp[ny][nx], new_cnt)

    return response

n = int(input())
arr = []
for _ in range(n):
    l = list(map(int, input()))
    arr.append(l)

print(func(n, n-1, n-1))