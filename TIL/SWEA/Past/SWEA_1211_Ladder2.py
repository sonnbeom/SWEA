# import sys

# sys.stdin = open("ladder2.txt",'r')

# 좌 우 상 순서 : 사다리타기 룰
dx = [-1, 1, 0]
dy = [0, 0, -1]

# 00 01
# 10 11
arr = [list(map(int, input().split())) for _ in range(100)]

index_list = []

for i in range(1, 99):
    if arr[99][i] == 1:
        index_list.append(i)
    
# index_list.pop(0)
# index_list.pop(-1)

res_dic = {}
min_count = 100 * 101

for i in index_list:
    y = 99
    x = i
    count = 0
    direc = 0
    copy = [row[:] for row in arr]
    while y > 0:
        now_x = x + dx[direc]
        now_y = y + dy[direc]
        if 0 <= now_x < 100 and 0 <= now_y < 100 and copy[now_y][now_x] == 1:
            y = now_y
            x = now_x
            direc = 0
            # print(f'{i}번째 count는 {count}입니다 y는{y} x는 {x}')
            count += 1
            copy[now_y][now_x] = 0
        else:
            direc = (direc+1) % 3

    if count < min_count:
        min_count = count
    res_dic[x] = count

print(min_count)
