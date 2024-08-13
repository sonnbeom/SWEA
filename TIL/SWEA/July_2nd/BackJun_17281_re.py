from itertools import permutations

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]

result = -1
order = [i for i in range(1, 9)]
for x in permutations(order):
    x = list(x)
    batter = x[:3] + [0] + x[3:]
    score = 0
    seq = 0

    for i in range(n):
        out = 0
        p1 = p2 = p3 = 0
        while out < 3:
            if game[i][batter[seq]] == 0:
                out += 1
            elif game[i][batter[seq]] == 1:
                score += p3
                p1, p2, p3 = 1, p1, p2
            elif game[i][batter[seq]] == 2:
                score += p3 + p2
                p1, p2, p3 = 0, 1, p1
            elif game[i][batter[seq]] == 3:
                score += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif game[i][batter[seq]] == 4:
                score += p1 + p2 + p3 + 1
                p1 = p2 = p3 = 0
            seq += 1
            if seq == 9:
                seq = 0
    result = max(result, score)
print(result)

        