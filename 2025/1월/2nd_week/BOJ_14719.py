def fill(x, fill_cnt):
    # 시작 끝, 스텝
    for i in range(len(block)-fill_cnt, len(block)):
        block[i][x] = 1
y, x = map(int, input().split())
block = [[0 for _ in range(x)] for _ in range(y)]
li = list(map(int, input().split()))

for i in range(len(li)):
    fill(i, li[i])
print(block)


