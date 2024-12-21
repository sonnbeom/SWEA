def solution(n, tops):
    num = 10007

    left = [0 for _ in range(n)]
    other = [0 for _ in range(n)]

    left[0] = 1
    if tops[0] == 1:
        other[0] = 3
    else:
        other[0] = 2

    for i in range(1, n):
        if tops[i] == 1:
            left[i] = left[i - 1] + other[i - 1]
            other[i] = left[i - 1] * 2 + other[i - 1] * 3
        else:
            left[i] = left[i - 1] + other[i - 1]
            other[i] = left[i - 1] + other[i - 1] * 2
        left[i] %= num
        other[i] %= num

    return (left[-1] + other[-1]) % num