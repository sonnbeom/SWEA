from collections import deque
import itertools
from copy import deepcopy


# 완탐 그 자체
# 정사각형 기준 상단, 우측, 하단, 좌측을 4개에 따라 탐색하였다. 이걸 하나의 함수로 만들기에는 범위가 다르기에 불가능하다 판단
# 좌측에서 우측으로 간다고 가정 => 가장 우측에 있는 값은 다음 블럭에서 사용해야하므로 past에 저장
# 그리고 한칸씩 밀어낸다.
past = -1
def func(arr, sy, sx, by, bx):
    # 몇번 반복할지는 여기서 판단 유노 y,x 1씩 차감
    while True:
        if sy == by: #대각선으로 1칸씩 좁히면 정사각형이므로 결국 한 지점에서 만난다.
            break

        for i in range(4): # 방향을 구분지어야 한다.
            rotate(arr, sy, sx ,by, bx, i)
        # 대각선 이동
        sy += 1
        sx += 1
        bx -= 1
        by -= 1

def rotate(arr, sy, sx, by, bx, idx):
    global past
    li = []

    # 첫번째에는 past가 없다.post의 값을 주기만 하면 된다.
    if idx == 0:
        for i in range(sx, bx+1):
            li.append(arr[sy][i])
        past = li.pop(-1)

        for i in range(sx+1,bx+1):
            arr[sy][i] = li.pop(0)

    # 새로운 past를 갱신하기 전 새로 갱신할 past를 new_past에 저장
    # idx 0과 다른 점은 past 값이 갱신되어야 하고 이 값을 넣어준다는 것이다.
    # 마지막에 이전 past를 갱신했다면 past를 new_past로 갱신
    elif idx == 1:
        for i in range(sy+1, by+1):
            li.append(arr[i][bx])

        new_past = li.pop(-1)

        for i in range(sy+1, by+1):
            if i == sy+1:
                arr[i][bx] = past
            else:
                arr[i][bx] = li.pop(0)

        past = new_past

    # 위와 동
    elif idx == 2:
        for i in range(sx, bx):
            li.append(arr[by][i])
        new_past = li.pop(0)
        for i in range(sx, bx):
            if i == bx-1:
                arr[by][i] = past
            else:
                arr[by][i] = li.pop(0)

        past = new_past

    # 새로 past를 갱신할 필요는 없다. 초기화만 해주면 된다.
    else:
        for i in range(sy+1, by):
            li.append(arr[i][sx])
        for i in range(sy, by-1):
            arr[i][sx] = li.pop(0)
        arr[by-1][sx] = past
        past = 0

# 배열 정보
n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    li = list(map(int, input().split()))
    arr.append(li)
# 회전 정보
rotate_info = []
for _ in range(k):
    li = list(map(int, input().split()))
    rotate_info.append(li)

# 순열을 돌린다.
permutations = itertools.permutations(rotate_info, k)
answer = int(1e9)
for permu in permutations:
    new_arr = deepcopy(arr)
    for r, c, s in permu:
        func(new_arr, r - s - 1, c - s - 1, r + s - 1, c + s - 1)
    for i in range(n):
        response = min(answer, sum(new_arr[i]))

print(answer)


