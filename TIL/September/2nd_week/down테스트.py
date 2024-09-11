def down(x, arr):
    tmp_list = []
    go = False
    idx = 0
    for i in range(h-1, -1, -1):
        # print(f'i ={i} x = {x}')
        if arr[i][x] == 0 and not go:
            go = True
            idx = i
        elif arr[i][x] != 0 and go:
            tmp_list.append(arr[i][x])
            arr[i][x] = 0

    if tmp_list:
        for tmp in tmp_list:
            arr[idx][x] = tmp
            idx -= 1

n, w, h = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(h)]

for i in range(w):
    down(i, arr)
print(arr)