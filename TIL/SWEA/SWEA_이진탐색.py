
def getBinarySearchCount(left, right, target):
    count = 0
    
    while left < right:
        
        mid = int((left+right)/2)
        
        if mid == target:
            break
        elif mid < target:
            left = mid
            count += 1
        else: #mid > target:
            right = mid
            count += 1
    return count

right, a, b = map(int, input().split())

resA = getBinarySearchCount(1, right, a)
resB = getBinarySearchCount(1, right, b)
if resA < resB:
    print("A")
elif resA > resB:
    print("B")
else:
    print(0)