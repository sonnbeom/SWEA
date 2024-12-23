arr = [[0 for _ in range(8)] for _ in range(8)]
sx, sy, bx, by = 1, 1, 7, 4
for y in range(by-1, sy - 1, -1):
    for x in range(sx, bx):
        arr[y][x] += 1
for i in range(len(arr)):
    print(f'arr = {arr[i]}')