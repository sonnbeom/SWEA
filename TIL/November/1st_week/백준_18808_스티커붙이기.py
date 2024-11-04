# 세로 n 가로 m
n, m, k = map(int, input().split())

stickers = []

for _ in range(k):
    r, c = map(int, input().split())
    sticker = []
    for _ in range(r):
        temp_list = list(map(int, input().split()))
        sticker.append(temp_list)
    stickers.append(sticker)