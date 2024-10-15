def func(req, other):
    last_idx = 0
    req_cnt = 0
    for i in range(n):
        if arr[i] == other:
            last_idx = i
    for i in range(last_idx):
        if arr[i] == req:
            req_cnt += 1
    return req_cnt


n = int(input())
arr = list(input())

'''
정방향 R
정방향 B
역방향 R
역방향 B
'''
min_cnt = int(1e9)

min_cnt = min(func("R", "B"), min_cnt)
min_cnt = min(func("B", "R"), min_cnt)
arr.reverse()
min_cnt = min(func("R", "B"), min_cnt)
min_cnt = min(func("B", "R"), min_cnt)

print(min_cnt)