from itertools import permutations

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]

result = -1

order = [i for i in range(1, 9)]

for x in permutations(order):
    x = list(x)
    seq = x[:3] + [0] + x[3:]
    num = 0
    score = 0
    for i in range(n):
        out = 0 
        p1 = p2 = p3 = 0
        while out < 3:
            if game[i][seq[num]] == 0:
                out += 1
            elif game[i][seq[num]] == 1:
                score += p3
                p1, p2, p3 = 1, p1, p2
            elif game[i][seq[num]] == 2:
                score += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif game[i][seq[num]] == 3:
                score += p2 + p3 + p1
                p1, p2, p3 = 0, 0, 1
            elif game[i][seq[num]] == 4:
                score += p2 + p3 +p1 + 1
                p1, p2, p3 = 0, 0, 0
            num += 1
            if num == 9:
                num = 0
    result = max(result, score)
print(result)