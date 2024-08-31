for tc in range(1, 11):
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
        res += string[now]
        inorder(now * 2 + 1)

    inorder(1)

    print(f'#{tc} {res}')