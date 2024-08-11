t = int(input())
for testCase in range(1, t+1):
    res = 0
    small = input()
    big = input()

    smallLen = len(small)
    bigLen = len(big)

    for idx in range(bigLen- smallLen +1):
        tempBig = big[idx: smallLen+idx]
        if small == tempBig:
            res += 1
    print(f'#{testCase} {res}')