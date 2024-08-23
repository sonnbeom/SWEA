
paper = [list(map(int, input().split())) for _ in range(10)]
total = 25
remain = [5, 5, 5, 5, 5]
def check(y, x, k):
    for ny in range(y, y+k+1):
        for nx in range(x, x+k+1):
            if paper[ny][nx] != 1:
                return False
    return True
def backtracking(y, x, cnt):
    global total, remain
    if y == 10:
        total = min(total, cnt)
        return
    if x == 10:
        backtracking(y+1, 0, cnt)
        return
    if paper[y][x] == 1:
        for k in range(5):
            if remain[k] == 0:
                continue
            if x+k >= 10 or y+k >= 10:
                continue
            if not check(y, x, k):
                break

            for ny in range(y, y+k+1):
                for nx in range(x, x+k+1):
                    paper[ny][nx] = 0

            remain[k] -= 1
            backtracking(y, x+k+1, cnt+1)
            remain[k] += 1

            for ny in range(y, y+k+1):
                for nx in range(x, x+k+1):
                    paper[ny][nx] = 1
    else:
        backtracking(y, x+1, cnt)
backtracking(0,0,0)
if total == 25:
    print(-1)
else:
    print(total)