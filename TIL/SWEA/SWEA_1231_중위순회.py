n = int(input())

arr = []
def check(num):
    if num in arr:
        return True
    else:
        return False
        
for i in range(n):
    tmp = list(input().split())
    num = tmp[0]
    if check(num):
        