def func(node_cnt):
    pass

n, c = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(1, n+1):
    func(i)