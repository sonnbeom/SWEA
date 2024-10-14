import heapq
def dijkstra(start):
    cost_list = [int(1e9) for _ in range(n + 1)] # 각 노드로 가는 비용
    q = [(start, 0)]
    heapq.heapify(q)
    cost_list[start] = 0 #현재 노드에서 현재 노드로 가는 것에는 비용이 들지 않는다.
    while q:
        now_cost, node = heapq.heappop(q) #현재까지의 비용, 현재 노드가 어디인지
        if cost_list[node] < now_cost: # 현재까지의 비용이 최소값으로 저장되어있는 리스트를 조회 만약 현재까지의 비용이 크다면 현재 방식은 더 탐색할 필요가 없다.
            continue
        for next_node, next_cost in graph[node]: # 현 노드에서 다음 노드로 가는 경우의 수를 알아보기
            cost = next_cost + now_cost  #현재까지의 비용과 추가 비용
            if cost < cost_list[next_node]: ##현재까지의 비용과 추가 비용이 최소값으로 저장되어있는 리스트 값과 비교
                cost_list[next_node] = cost # 더 작다면 갱신
                heapq.heappush(q, (cost, next_node)) # 적은 비용의 루트이므로 heapq에 넣는다.
    return cost_list
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]


for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())

cost_list = dijkstra(start)
print(cost_list[end])