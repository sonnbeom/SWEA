from itertools import combinations

answer = 0

n, c = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, n+1):
    li = list(combinations(arr, i))
    for l in li:
        if sum(l) <= c:
            answer += 1

print(answer+1)
