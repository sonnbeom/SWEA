import sys
sys.stdin = open("input.txt",'r')

dx = [1, -1, 0]
dy = [0, 0, -1]

for t in range(10):
    a = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    x = arr[99].index(2)
    y = 99
    direc = 0

    while y > 0:
        now_x = x + dx[direc]
        now_y = y + dy[direc]

        if 0 <= now_x < 100 and 0 <= now_y < 100 and arr[now_y][now_x] == 1:
            arr[now_y][now_x] = 0
            x = now_x
            y = now_y
            direc = 0
        else:
            direc = (direc+1) % 3
    
    print(f'#{t} {x}')

    



