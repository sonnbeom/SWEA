m, n, h = map(int, input().split())
x = m
y = n
'''
m은 가로 n은 세로 h는 높이
왼, 오, 위, 아래 = 델타 탐색
위, 아래 => 앞 뒤 배열에서 같은 idx를 가진 값을 기반
3차원 배열인가..?
'''

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

arr = []
for i in range(h):
    tmp = []
    for j in range(m):
        tmp_list = list(map, int(input().split()))
        tmp.append(tmp_list)
    arr.append(tmp)
