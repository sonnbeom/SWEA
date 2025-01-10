from collections import deque
dy = 1
dx = [-1, 0, 1]
n = int(input())
arr = []
def get_min_value(n, arr):
    min_value = int(1e9)
    dp_min = [[int(1e9) for _ in range(3)] for _ in range(n)]
    q = deque()
    for i in range(3):
        q.append((0, i, arr[0][i]))

    while q:
        y, x, cnt = q.popleft()

        for i in range(3):
            ny = y + 1
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < 3):
                continue
            next_cnt = cnt + arr[ny][nx]
            if next_cnt >= dp_min[ny][nx]:
                continue
            else:
                dp_min[ny][nx] = next_cnt
            if ny == n - 1:
                min_value = min(min_value, next_cnt)
            else:
                q.append((ny, nx, next_cnt))
    return min_value

def func(n, arr):
    max_value = int(-1e9)

    dp_max = [[int(-1e9) for _ in range(3)] for _ in range(n)]
    q = deque()
    for i in range(3):
        q.append((0, i, arr[0][i]))

    while q:
        y, x, cnt = q.popleft()

        for i in range(3):
            ny = y + 1
            nx = x + dx[i]
            if not(0 <= ny < n and 0 <= nx < 3):
                continue
            next_cnt = cnt + arr[ny][nx]
            if next_cnt <= dp_max[ny][nx]:
                continue
            else:
                dp_max[ny][nx] = next_cnt
            if ny == n - 1:
                max_value = max(max_value, next_cnt)
            else:
                q.append((ny, nx, next_cnt))
    del dp_max
    
    min_value = get_min_value(n, arr)
    return max_value, min_value

for i in range(n):
    li = list(map(int, input().split()))
    arr.append(li)


print(func(n, arr))