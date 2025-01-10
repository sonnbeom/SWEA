from collections import deque
dy = 1
dx = [-1, 0, 1]
n = int(input())
arr = []
def func(n, arr):
    cnt_list = []
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
            if ny == n - 1:
                cnt_list.append(cnt + arr[ny][nx])
            else:
                q.append((ny, nx, cnt + arr[ny][nx]))

    return cnt_list

for i in range(n):
    li = list(map(int, input().split()))
    arr.append(li)
response = func(n, arr)

res = ''
res += str(max(response))
res += " "
res += str(min(response))
print(res)
