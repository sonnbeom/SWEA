def is_can(req_num, req_bool):

    temp = []
    res = True

    if req_bool:
        for i in range(n):
            temp.append(arr[i][req_num])
    else:
        for i in range(n):
            temp.append(arr[req_num][i])

    while temp:
        if len(temp) <= 1:
            break

        if temp[0] == temp[1]:
            temp.pop(0)

        elif abs(temp[0] - temp[1]) > 1:
            res = False
            break
        elif temp[0] != temp[1]:
            t = n - len(temp)
            if t + l < n:
                diff = temp[0] - temp[1]
                for i in range(1, l+1):
                    temp_diff = temp[0] - temp[i]
                    if temp_diff != diff:
                        res = False
                        break
                for _ in range(1, l+1):
                    temp.pop(0)
            else:
                res = False
                break
    return res


n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
# y 축으로 한번 돌고
for i in range(n):
    res_x = is_can(i, True)
    if res_x:
        cnt += 1
        print(f'x i = {i}')
    res_y = is_can(i, False)
    if res_y:
        cnt += 1
        print(f'y i = {i}')

print(cnt)



# x축으로 한번 돌고

