# 예시 이차원 배열
arr = [[1, 2], [1, 2, 3, 4], [1], [1, 2, 3]]

# 각 배열의 크기로 정렬 (내림차순)
sorted_arr = sorted(arr, key=len, reverse=True)

print(sorted_arr)
n= 5
arr2 = [[]for _ in range(n+1)]

arr2[0].append(1)
arr2[0].append(1)
arr2[0].append(1)
arr2[0].append(1)
print(arr2)