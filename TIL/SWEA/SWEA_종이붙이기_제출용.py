d = int(input())
for tc in range(1, d+1):
    t= int(input())//10

    tmp = 1
    ans = 3
    def getBoxCount(n):
        global ans
        global tmp
        if n == 1:
            ans = 1
            return
        elif n == 2:
            ans = 3
            return
        for i in range(n-2):
            temp = ans
            ans = ans + 2*tmp
            tmp = temp
    getBoxCount(t)
    print(f'#{tc} {ans}')

