n = int(input())
chul_p = 0
arr = []
is_can = True
check_num = 2000001
for i in range(n):
    p, c = map(int, input().split())
    arr.append((p, c))
    check_num = min(p, is_can)

for other_p, c in arr:
    if abs(other_p - chul_p) <= c:
        chul_p += 1
print(chul_p)