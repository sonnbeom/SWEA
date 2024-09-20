def func():
    global ans
    if len(req) >= 2:
        big_num = req[0]
        small_num = req[1]
        tmp_plus = big_num + small_num
        tmp = big_num * small_num
        if tmp > tmp_plus:
            ans += tmp
            req.pop(0)
            req.pop(0)
        else:
            ans += big_num
            req.pop(0)
    else:
        ans += req[0]
        req.pop(0)

N = int(input())

req = [0 for _ in range(N)]

for i in range(N):
    a = int(input())
    req[i] = a

req.sort(reverse=True)
ans = 0

is_minus_sort = False

while req:
    if len(req) >= 2:
        big_num = req[0]
        small_num = req[1]
        if big_num < 0 and not is_minus_sort: # 큰 숫자가 음수라면 음수로 정렬
            req.sort()
            is_minus_sort = True

        elif small_num < 0 and not is_minus_sort: #두번째 숫자가 음수이고 음수로 정렬 안 한 경우
            if big_num == 0: # 0 -1 -2 -3 일 경우 0을 마지막으로 넣어야 한다 2 -1 -2 -3일 경우 그대로 함수를 진행
                tmp = req.pop(0)
                req.sort()
                req.append(tmp)
                is_minus_sort = True
    func()

print(ans)
