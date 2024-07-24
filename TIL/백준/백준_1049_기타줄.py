n, m = map(int, input().split())

pack = []
one = []

for i in range(m):
    a, b = map(int, input().split())
    pack.append(a)
    one.append(b)

minPack = min(pack)
minOne = min(one)

if minPack < minOne * 6:
    if minPack < (n%6) * minOne:
        print((n//6) * minPack + minPack)
    else:
        print((n//6) * minPack + (n % 6) * minOne)
elif minPack >= minOne * 6:
    print(n * minOne)