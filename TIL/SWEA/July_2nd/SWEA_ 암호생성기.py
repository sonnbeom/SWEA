arr = list(map(int, input().split()))

q = []
for i in range(8):
    q.append(arr[i])
t = 1
while True:
    tmp = q.pop(0)
    tmp -= t
    if tmp <= 0:
        tmp = 0
        q.append(tmp)
        break
    q.append(tmp)
    t += 1
    if t == 6:
        t = 1

print(*q)