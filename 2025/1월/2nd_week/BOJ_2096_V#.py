n = int(input())
# 맨 처음 세개의 숫자를 입력받아 DP의 초기 값을 설정한다.
arr = list(map(int, input().split()))
max_dp = arr
min_dp = arr

for _ in range(n-1):
    arr = list(map(int, input().split()))
    max_dp = [
        max(max_dp[0], max_dp[1]) + arr[0],
        max(max_dp) + arr[1],
        max(max_dp[1], max_dp[2]) + arr[2]
    ]
    min_dp = [
        min(min_dp[0], min_dp[1]) + arr[0],
        min(min_dp) + arr[1],
        min(min_dp[1], min_dp[2]) + arr[2]
    ]

print(max(max_dp), min(min_dp))