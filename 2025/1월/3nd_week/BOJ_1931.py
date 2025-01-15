import heapq
n = int(input())

q = []
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(q, (e, s))

past, s = heapq.heappop(q)
cnt = 1
while q:
    e, s = heapq.heappop(q)
    if s >= past:
        cnt += 1
        past = e
print(cnt)
