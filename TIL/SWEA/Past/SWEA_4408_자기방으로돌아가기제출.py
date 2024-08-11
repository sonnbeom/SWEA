def transfer(req):
    if req == 1:
        return 1
    elif req % 2 == 1:
        return (req // 2) + 1
    else:
        return req // 2
def bigFirst(a, b):
    if a >= b:
        return (a, b)
    else:
        return(b, a)

t = int(input())
for tc in range(1, t+1):

    res = 1
    count_list = [0 for _ in range(201)]

    n = int(input())

    for i in range(n):
        a, b = map(int, input().split())
        fi = transfer(a)
        se = transfer(b)
        big, small = bigFirst(fi, se)

        for j in range(small, big+1):
            count_list[j] += 1
        
    print(f'#{tc} {max(count_list)}')