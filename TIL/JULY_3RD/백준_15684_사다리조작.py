'''
n번 반복된다.
큰 사각형
안에 사각형
.
.
몇번을 도는지 알 수 없다
while문으로 돈다
시작 인덱스와 마무리 인덱스가 주어진다.
1, 5
4,5

1부터 5~
위치부터 y축 쭉 내려
다시 가로로 쭉
다시 위로 쭉
visited 가 가로 >= 2 세로 >= 2가 되어야 루프 계속
시작에서 대각선으로 이동
반복
if visited 가 가로 >= 2 세로 >= 2가 안 되면
리턴

이걸 조합으로 때려버려 그냥


'''
import itertools
import copy
dx = [1, 0, -1, 0] # 동남서북
dy = [0, 1, 0, -1]
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rotation_list = [list(map(int, input().split())) for _ in range(k)]

trial_list = list(itertools.permutations(rotation_list, k))

min_cnt = int(1e9)
for p in trial_list:
    cp_arr = copy.deepcopy(arr)
    for r, c, s in p:
        for i in range(s):
            top_r = r-s-1+i # r이 y
            top_c = c-s-1+i # c가 x
            bottom_r = r+s-1-i
            bottom_c = c+s-1-i
            y, x = top_r, top_c
            prev = cp_arr[y][x]
            for dir in range(4):
                while True:
                    nx = x + dx[dir]
                    ny = y + dy[dir]

                    if not (top_r <= ny <= bottom_r and top_c <= nx <= bottom_c):
                        break
                    tmp = cp_arr[ny][nx]
                    cp_arr[ny][nx] = prev
                    prev = tmp
                    y, x = ny, nx
    for y in cp_arr:
        min_cnt = min(min_cnt, sum(y))

print(min_cnt)

