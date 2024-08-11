for tc in range(1, 11):
    n, t = input().split()
    n = int(n)
    arr = list(map(int, t))
    def recur(leng):
        for i in range(leng):
            if len(arr) < leng:
                break
            if arr[i] == arr[i+1]:
                arr.pop(i)
                arr.pop(i)
                recur(leng-2)

    recur(n-1)
    res = ''
    for i in arr:
        res += str(i)
    print(f'#{tc} {res}')