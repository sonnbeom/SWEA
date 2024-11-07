# 이제 슬슬 라이브러리를 많이 써보자 시간 단축이 많이 된다.
# zip을 통해 각 배열의 순서대로 꺼낸다. tuple이 응답이다
# 리스트 컴프레션으로 해당 값을 리스트로 변환해서 리턴한다.
def rotate(arr):
    rotate_tuple = zip(*arr[::-1])
    return [list(e) for e in rotate_tuple]

# 배열의 idx 차이를 어떻게 처리할 것이냐를 고민함. 주어진 스티커와 노트북 사이 숫자 차이
# stikcer를 기준으로 주어진 인자를 더하자.
# 거꾸로도 가능하지만 sticker가 1이냐 0이냐가 더 중요하기 때문에 stikcer를 기준으로 삼았다.
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
                #넣을 수 있냐?
                res_can = is_can(y, x, sticker)
                # 그렇다면 삽입
                if res_can:
                    insert(y, x, sticker)
                    return
        # 안 되면 회전이요
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