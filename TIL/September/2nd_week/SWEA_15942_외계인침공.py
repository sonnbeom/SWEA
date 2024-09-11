'''
1. 행성을 침략한다. 근데 이 갯수를 for문을 돌려서
m+1 ~ s개까지 돌려야 한다 => 제일 큰 값을 하면 되는 거 아닌가..? 라고 하기엔 동원을 안 하고 하는 경우도 존재할 것이다.

1. 가장 적은 행성부터 간다. => 동원을 최소화
2. 만약 동원이 필요하다 -> 가장 최근 인덱스부터 리턴 받아 함선에 더한다.
3. 만약 다 동원 했는데 침략이 불가다. -1 리턴

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
