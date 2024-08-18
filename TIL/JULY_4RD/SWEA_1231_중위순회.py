# n = int(input())
# string = [[] for _ in range(n+1)]
# tmp = []
# for i in range(n):
#     req = list(input().split())
#     string[int(req[0])].append(req[1])
#
# def inorder(now):
#     global tmp
#     if now > len(string) - 1:
#         return
#     inorder(now * 2)
#     tmp += string[now]
#     inorder(now*2+1)
#
# inorder(1)
# res = ''
# for s in tmp:
#     res += s
# print(res)
n = int(input())
string = ' '
res = ''
for i in range(n):
    req = list(input().split())
    string += req[1]

def inorder(now):
    global res
    if now > len(string) - 1:
        return
    inorder(now * 2)
    print(string[now])
    res += string[now]
    inorder(now*2+1)

inorder(1)

print(res)