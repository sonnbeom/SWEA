req = input()
res = 1
stack = []
for char in req:
    if char == '(' or char == '{':
        stack.append(char)
    elif char == ')':
        tmp = stack.pop()
        if tmp != '(':
            res = 0
    elif char == '}':
        tmp = stack.pop()
        if tmp != '{':
            res = 0
if len(stack) > 0:
    res = 0
print(res)