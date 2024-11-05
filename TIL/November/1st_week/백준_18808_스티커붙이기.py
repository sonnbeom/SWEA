def rotate(arr):
    rotate_tuple = zip(*arr[::-1])
    return [list(e) for e in rotate_tuple]

def is_can(sy, sx, sticker):
    for y in range(len(sticker)):
        for x in range(len(sticker[0])):
            if sticker[y][x] == 0:
                continue
            ny = y + sy
            nx = x + sx
            if not(0 <= ny < n and 0 <= nx < m):
                return False
            if notebook[ny][nx] == 1:
                return False
    return True

def insert(sy, sx ,sticker):
    for y in range(len(sticker)):
        for x in range(len(sticker[0])):
            if sticker[y][x] == 0:
                continue
            ny = y + sy
            nx = x + sx
            notebook[ny][nx] = 1

def func(sticker):
    y_len = len(notebook)
    x_len = len(notebook[0])
    for i in range(4):
        for y in range(y_len):
            for x in range(x_len):
                res_can = is_can(y, x, sticker)
                if res_can:
                    insert(y, x, sticker)
                    return
        sticker = rotate(sticker)

n, m, k = map(int, input().split())
notebook = [[0 for _ in range(m)] for _ in range(n)]
stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    sticker = []
    for _ in range(r):
        temp_list = list(map(int, input().split()))
        sticker.append(temp_list)
    stickers.append(sticker)

while stickers:
    sticker = stickers.pop(0)
    func(sticker)

answer = 0
for i in range(n):
    answer += notebook[i].count(1)
print(answer)
