'''
1. past 값이 현재 k값과 더한 값에서 가장 가까운 노드를 찾는다.
'''
from collections import deque
def get_max_node(node, past):
    prev = 0
    for i in range(node, n):
        prev = planet[i]
        if past + k > planet[i]:
            return prev
    return -1
def up(start, past):

    q = deque()
    q.append(start)

    while q:
        node = q.popleft()
        max_node = get_max_node(node, past)
        if max_node == -1:
            pass # 가장 마지막에 노드에 이미 온 거임

n, k = map(int, input().split())
planet = list(map(int, input().split()))
maximum = planet[-1]
planet.sort()

visited_attack = [False for _ in range(n)]
visited_return = [False for _ in range(n)]

ans = 0
