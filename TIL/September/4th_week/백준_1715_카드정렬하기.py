import heapq

n = int(input())

q = []
ans = 0

for i in range(n):
    heapq.heappush(q, int(input()))

while len(q) != 1:
    tmp = heapq.heappop(q) + heapq.heappop(q)
    ans += tmp
    heapq.heappush(q, tmp)

print(ans)