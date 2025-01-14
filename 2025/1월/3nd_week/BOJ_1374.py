from collections import deque
import heapq
n = int(input())

pools = []

q = []
for _ in range(n):
    num, s, e = map(int, input().split())
    heapq.heappush(q,([s, num, e]))





