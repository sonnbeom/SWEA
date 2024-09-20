def get_num(small_idx, big_idx):
    res_min = min_num
    res_max = max_num
    for i in range(small_idx, big_idx+1):
        if req[i] > res_max:
            res_max = req[i]
        elif req[i] < res_min:
            res_min = req[i]
    res.append((res_min, res_max))


n, m = map(int, input().split())

req = [0 for _ in range(n+1)]

max_num = 1
min_num = 1000000000
for i in range(1, n+1):
    a = int(input())
    req[i] = a

trial_list = []

for i in range(m):
    a, b = map(int, input().split())
    trial_list.append((a, b))
res = []
for small_idx, big_idx in trial_list:
    get_num(small_idx, big_idx)
for small_num, big_num in res:
    print(small_num, end = ' ')
    print(big_num)