def func(weight, value):
    for i in range(len(dp)):
        idx = i + weight
        if idx < len(dp):
            dp[idx] = max(dp[idx], dp[i] + value)
        else:
            return

n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]

bag = []
for _ in range(n):
    w, v = map(int, input().split())
    bag.append(((w,v)))

bag.sort()
for w, v in bag:
    func(w, v)
    print(dp)

print(max(dp))