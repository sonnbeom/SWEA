'''

1. 5를 먼저 채운다.
2. 맨 위 꼭짓점 좌표를 구한다
3. y - 1한 좌표부터 양쪽을 델타 탐색하며 5라면 그걸 5로 색칠하고 양쪽으로 보내서 BFS탐색

다른 방법

테두리
1
2
3
4 하고 나머지 5로 채워
'''
dx = [1, 1, -1, -1] # 대각 우상 대각 우하 대각 좌하 좌상
dy = [-1, 1, 1, -1]
n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
# arr = [[0 for _ in range(n)] for _ in range(n)]


def divide_city(arr, y, x, d1, d2):
    end = [(y-d1, x+d1),  (y, x +d1+d2), (y+d2-d1, x+d1), (y, x)]
    # arr[y][x] = 5
    for i in range(4):
        while True:
            ny = y + dy[i]
            nx = x + dx[i]
            if ny == end[i][0] and nx == end[i][1]:
                arr[ny][nx] = 5
                break
            elif 0 <= nx < n and 0 <= ny < n:
                arr[ny][nx] = 5
                y, x = ny, nx



