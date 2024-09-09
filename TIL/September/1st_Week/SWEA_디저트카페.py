'''
00 01
10 11


'''
dx = [1, 1, -1, -1] #우상 우하 좌상 좌하
dy = [-1, 1, -1, 1]

def get_dessert(y,x,start_y,start_x, cnt):
    if cnt != 1 and y == start_y and x == start_x:
        pass


max_cnt = 0
n = int(input())
cafe = list(map((int, input().split())))
visited = [False for _ in range(n) for _ in range(n)]
