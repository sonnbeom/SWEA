import itertools

n = int(input())
player = []
for i in range(n):
    temp = list(map(int, input().split()))
    player.append(temp)

permutation = itertools.permutations(range(1, 9), 8)
answer = 0

for p in permutation:
    p = list(p)
    score = 0
    seq = 0
    bat = p[:3] + [0] + p[3:]
    for i in range(n):
        out = 0
        p1 = p2 = p3 = home = 0
        while out < 3:
            a = bat[seq]
            b = player[i][a]

            if b == 0:
                out += 1
            elif b == 1:
                score += p3
                p3, p2, p1 = p2, p1, 1
            elif b == 2:
                score += p3 + p2
                p3, p2, p1 = p1, 1, 0
            elif b == 3:
                score += p3 + p2 + p1
                p3, p2, p1 = 1, 0, 0
            else:  # b == 4 (홈런)
                score += p3 + p2 + p1 + 1
                p3, p2, p1 = 0, 0, 0

            seq += 1
            if seq == 9:  # 타순이 끝나면 처음으로
                seq = 0

    answer = max(answer, score)

print(answer)
