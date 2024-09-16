'''
1. 이차원 배열을 만든다.
2. 이차원 배열을 for문을 돌며
방문하지 않았다면
해당 값에 노드가 있다면 idx, node 출력
그리고 n개의 방문 배열에 방문 체크

3. 방문 배열의 갯수의 0이 아니라면
if문을 돌며 방문 배열 idx 출력
'''

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
visited[0] = True

arr = [[] for _ in  range(n+1)]

way = []

for i in range(m):
    a, b = map(int, input().split())
    way.append((a, b))

for a, b in way:
    if len(arr[a]) == 0:
        arr[a].append(b)
    elif len(arr[a]) >= 1:
        t = min(arr[a][0], b)
        arr[a][0] = b
ans = []
tmp_list = []
for i in range(1, n+1):
    if len(arr[i]) == 1 and not visited[arr[i]]:
        ans.append(i)
        ans.append(arr[i][0])
        visited[i] = True
        visited[arr[i][0]] = True

    else:
        tmp_list.append(i)

if visited.count(False) > 0:
    if len(tmp_list) > 0:
        for num in tmp_list:
            if not visited[num]:
                ans.append(num)
print(*ans)