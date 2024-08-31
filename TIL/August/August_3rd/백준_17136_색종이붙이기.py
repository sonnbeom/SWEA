paper = [list(map(int, input().split())) for _ in range(10)]
remain = [5, 5, 5, 5, 5]
total = 25

def check(y, x, k):
    for i in range(y, y+k+1):
        for j in range(x, x+k+1):
            if paper[i][j] != 1:
                return False
    return True

def back_tracking(y, x, cnt):
    global total, remain
    if y >= 10:
        total = min(cnt, total)
        return
    if x >= 10:
        back_tracking(y+1, 0, cnt)
        return
    if paper[y][x] == 1:
        for k in range(5):
            if remain[k] == 0:
                continue
            if y + k >= 10 or x + k >= 10:
                continue
            if not check(y, x, k):
                break
            for i in range(y, y+k+1):
                for j in range(x, x+k+1):
                    paper[i][j] = 0
            remain[k] -= 1
            back_tracking(y, x+k+1, cnt+1)
            remain[k] += 1
            for i in range(y, y+k+1):
                for j in range(x, x+k+1):
                    paper[i][j] = 1
    else:
        back_tracking(y, x+1, cnt)
back_tracking(0, 0, 0)

if total != 25:
    print(total)
else:
    print(-1)
