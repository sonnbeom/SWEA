n = int(input())
input_list = input()
ans = -1 * 2**31

def calculate(num1, st, num2):
    if st == '+':
        res = num1 + num2
    elif st == '-':
        res = num1 - num2
    else:
        res = num1 * num2
    return res

def dfs(index, value):
    global ans
    if index == n-1:
        ans = max(value, ans)
        return
    if index + 2 < n:
        next_value = calculate(value, input_list[index+1], int(input_list[index+2]))
        dfs(index+2, next_value)
    if index + 4 < n:
        next_next_value = calculate(int(input_list[index+2]), input_list[index+3], int(input_list[index+4]))
        next_value = calculate(value, input_list[index+1], next_next_value)
        dfs(index+4, next_value)
dfs(0, int(input_list[0]))
print(ans)
