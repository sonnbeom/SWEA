arr = []
arr.append([1,2,3])
arr.append([4,5,6])

def rotate(arr):
    list_tuple = zip(*arr[::-1])
    res = [list(e) for e in list_tuple]
    print(res)

rotate(arr)