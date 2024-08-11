t = int(input())
for tc in range(1, t+1):
    n = int(input())
    score = list(map(int, input().split()))

    scoreVisited = [1] + [0] * sum(score)
    resScore = [0]

    for point in score:
        for i in range(len(resScore)):
            if not scoreVisited[point + resScore[i]]:
                scoreVisited[point + resScore[i]] = 1
                resScore.append(point + resScore[i])
    print(f'#{tc} {len(resScore)}')
