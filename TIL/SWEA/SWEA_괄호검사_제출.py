t = int(input())

for tc in range(1, t+1):
    req = input()
    res = 1
    stack = []
    for char in req:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            if not stack:
                res = 0
            else:
                tmp = stack.pop()
                if tmp != '(':
                    res = 0
        elif char == '}':
            if not stack:
                res = 0
            else:
                tmp = stack.pop()
                if tmp != '{':
                    res = 0
    if len(stack) != 0:
        res = 0
    print(f'#{tc} {res}')