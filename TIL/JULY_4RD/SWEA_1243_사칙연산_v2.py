def postorder(now):
    global stack
    if tree[now]:
        postorder(left[now])
        postorder(right[now])

        if type(tree[now]) == int:
            stack += [tree[now]]
        else:
            r = stack.pop()
            l = stack.pop()
            if tree[now] == '+':
                stack += [1]


N = int(input())

tree = [0 for _ in range(N+1)]
left = [0 for _ in range(N+1)]
right = [0 for _ in range(N+1)]

for i in range(N):
    temp = input().split()
    if len(temp) == 4:
        tree[int(temp[0])] = temp[1]
        left[int(temp[0])] = int(temp[2])
        right[int(temp[0])] = int(temp[3])
    else:
        tree[int(temp[0])] = int(temp[1])
stack = []
postorder(1)