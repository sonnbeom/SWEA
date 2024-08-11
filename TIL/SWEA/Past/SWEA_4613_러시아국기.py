w = "W"
r = "R"
b = "B" 

n, m = map(int, input().split())

flag = [list(input()) for _ in range(m)]
# for _ in range(m):
#     temp = input()
#     flag.append(list(temp))

res = n * m
white = 0
for w in range(n-2):
    for l in range(m):
        if flag[w][l] != "W":
            white += 1
    blue = 0
    for b in range(w+1, n-1):
        for l in range(m):
            if flag[b][l] != "B":
                blue += 1
        red = 0
        for r in range(b+1, n):
            for l in range(m):
                if flag[r][l] != "R":
                    red += 1
        res = min(res, red + blue + white)
print(res)
