def calculate(i):
    if len(tree[i]) == 2:
        return int(tree[i][1])
    else:
        l = calculate(int(tree[i][2]))
        r = calculate(int(tree[i][3]))

        a = tree[i][1]
        if a == '+':
            return l + r
        elif a == '-':
            return l - r
        elif a == '*':
            return l * r
        elif a == '/':
            return l / r

n = int(input())
tree = [0 for _ in range(n+1)]

for i in range(n):
    tmp = input().split()
    tree[int(tmp[0])] = tmp
print(calculate(1))