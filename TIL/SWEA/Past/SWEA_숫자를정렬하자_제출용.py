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

    def selectionSort(arr, n):
        for i in range(n-1):
            idx = i
            for j in range(i+1, n):
                if arr[idx] > arr[j]:
                    idx = j
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp
        return arr

    n = int(input())
    arr = list(map(int, input().split()))

    res = bubbleSort(arr, len(arr))

    print(f'#{testCase}', *res)