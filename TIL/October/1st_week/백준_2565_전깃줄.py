n = int(input())

arr = [[]for _ in range(n+1)]
tower_a = []
tower_b = []
for i in range(n):
    a, b = map(int, input().split())
    tower_a.append(a)
    tower_b.append(b)

for i in range(n):
    pass