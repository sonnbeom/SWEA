# import sys
# sys.stdin = open("input.txt", "r")
ans = 1

def is회문(arg):
    global ans
    tmp = arg[::-1]
    if arg == tmp and len(arg) > ans:
        ans = len(arg)
        print(ans, arg)


arr = [list(map(str, input())) for _ in range(8)]
n = 8
# for i in range(n):
#     for j in range(i, n):
#         tmp = ans
#         tempStr = ''
#         for k in range(j, n):
#             if k > ans:
#                 tempStr += arr[0][k]
#         is회문(tempStr)
# print(ans)

for t in range(n):
    for i in range(n):
        for j in range(i, n):
            tempStr = ''
            for k in range(n):
                tempStr += arr[t][k]
                if k >= ans:
                    is회문(tempStr)
                
print(ans)