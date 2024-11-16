arr = []
arr.append([1,2,3])
arr.append([4,5,6])

def rotate(arr):
    list_tuple = zip(*arr[::-1])
    return [list(e) for e in list_tuple]

print(f'회전 전 arr = {arr}')
res = rotate(arr)
print(f'회전 후 res = {res}')