t = int(input())
for testCase in range(1, t+1):
    
    def getBinarySearchCount(left, right, target):
        res = 0
        
        while left < right:
            
            mid = int((left+right)/2)
            
            if mid == target:
                break
            elif mid < target:
                left = mid
                res += 1
            else: #mid > target:
                right = mid
                res += 1
        return res

    right, a, b = map(int, input().split())

    resA = getBinarySearchCount(1, right, a)
    resB = getBinarySearchCount(1, right, b)
    if resA < resB:
        print(f'#{testCase} A')
    elif resA > resB:
        print(f'#{testCase} B')
    else:
        print(f'#{testCase} 0')