def solution(req_num, req_bool):
    visited = [False for _ in range(n)]
    temp = []
    res = False
    idx = 0
    if req_bool:
        for i in range(n):
            temp.append(arr[i][req_num])
    else:
        for i in range(n):
            temp.append(arr[req_num][i])


    while temp:
        # 조건이 만족되었다!
        if idx >= n-1:
            res = True
            break

        if temp[idx] == temp[1]:
            idx += 1

        elif abs(temp[idx+1] - temp[idx]) > 1:
            break

        else:
            if temp[idx+1] > temp[idx]:
                temp_res = next_node_big(idx, temp, visited)
                if temp_res:
                    idx += 1
                else:
                    break
            else:
                temp_res = next_node_small(idx, temp, visited)
                if temp_res:
                    idx += l
                else:
                    break

    return res
def next_node_small(idx, temp, visited):
    res = False
    node = temp[idx+1]
    if idx + 1 + l < n:
        for i in range(idx+1, idx+1+l):
            if visited[idx]:
                return res
            if node != temp[i]:
                return res
            visited[i] = True
    else:
        return res
    res = True
    return res

def next_node_big(idx, temp, visited):
    res = False

    if idx + 1 - l >= 0:
        node = temp[idx]
        for i in range(idx + 1 - l, idx+1):
            if visited[i]:
                return res
            if node != temp[i]:
                return res
            visited[i] = True
    else:
        return res
    res = True
    return res
n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
# y 축으로 한번 돌고
for i in range(n):
    res_x = solution(i, True)
    if res_x:
        cnt += 1
        print(f'x i = {i}')
    res_y = solution(i, False)
    if res_y:
        cnt += 1
        print(f'y i = {i}')


print(cnt)

