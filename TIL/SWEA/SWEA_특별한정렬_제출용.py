t = int(input())
for testCase in range(1, t+1):
    def bubbleSort(arr, n):
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr
        

    n = int(input())
    arr = list(map(int, input().split()))

    sortedList = bubbleSort(arr, len(arr))

    cenIdx = n // 2 
    if n % 2 == 1:
        cenIdx+1

    res = []
    for i in range(cenIdx):
        if len(res) == 10:
            break
        res.append(sortedList.pop())
        res.append(sortedList.pop(0))

    print(f'#{testCase}', *res)