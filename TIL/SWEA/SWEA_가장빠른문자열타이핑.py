countCheck = 0
a, b = input().split()
A = a
# n = 긴 값 길이 req
def recur(n, big, sm):
    global A
    global countCheck
    if n <= len(sm):
        return
    for i in range(n-len(sm)+1):
        if big[i:i+len(sm)] == sm:
            temp = big[:i] + big[i+len(sm):]
            A = temp
            countCheck += 1
            recur(n-len(sm),temp, sm)
            break

recur(len(a), a, b)
# print(A)
# print(countCheck)
print(len(A) + countCheck)