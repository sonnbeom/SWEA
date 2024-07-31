t = int(input())
for testCase in range(1, t+1):
    def selectionSort(arr):
        n = len(arr)
        for i in range(n-1):
            minIdx = i
            for j in range(i+1, n):
                if arr[j] < arr[minIdx]:
                    minIdx = j
            temp = arr[i]
            arr[i] = arr[minIdx]
            arr[minIdx] = temp
        return arr

    n = int(input())
    arr = list(map(int, input().split()))
    res = selectionSort(arr)
    print(f'#{testCase}', *res)
