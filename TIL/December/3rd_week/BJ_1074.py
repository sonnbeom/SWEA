n, r, c = map(int, input().split())
ans = 0

while n != 0:
    n -= 1
    nn = 2 ** n
    # 2사분면
    if r < nn and c < nn:
        ans += nn * nn * 0

    # 1사분면
    elif r < nn and c >= nn:
        ans += nn * nn * 1
        c -= nn

    # 3사분면
    elif r >= nn and c < nn:
        ans += nn * nn * 2
        r -= nn

    else:
        ans += nn * nn * 3
        r -= nn
        c -= nn

print(ans)