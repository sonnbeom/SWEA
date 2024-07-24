
'''
1. 주유소 비용 현재를 nowPrice
2. 다음 주유소 비용이 nowPrice보다 작다면
3. 그 전까지 sum += 더해준다.
4. 갱신이 되면 nowPrice를 min으로 치환하고 1, 2, 3과정을 반복한다.
'''

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

nowPrice = price[0]
total = nowPrice * distance[0]

for num in range(1, n-1):
    if price[num] < nowPrice:
        nowPrice = price[num]
    total += distance[num] * nowPrice
    print(num, "쨰 total:", total)
print(total)
