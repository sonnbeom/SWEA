n = int(input())
ans = -1 * 2**31
inputList = list(input())
def caculate(c, s, b):
    if s == '+':
        res = c + b
    elif s == '-':
        res = c- b
    else:
        res = c * b
    return res

def dfs(idx, value):
    global ans

    if idx == n -1:
        ans = max(value, ans)
        return
    
    if idx + 2 < n:
        next_value = caculate(value, inputList[idx + 1], int(inputList[idx + 2]))
        dfs(idx + 2, next_value)
    
    if idx + 4 < n:
        next_next_value = caculate(int(inputList[idx + 2]), inputList[idx + 3], int(inputList[idx + 4]))
        next_value = caculate(value, inputList[idx + 1], next_next_value)
        dfs(idx + 4, next_value)

dfs(0, int(inputList[0]))
print(ans)



