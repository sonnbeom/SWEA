n = int(input())
dp = []
if n % 5 == 0:
    print(n//5)
else: 
    answer = 0
    while n > 0:
        n -= 3
        answer += 1
        if n % 5 == 0:
            answer += n//5
            print(answer)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print()
            break
