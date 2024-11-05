arr = []
arr.append([1,2,3])
arr.append([4,5,6])

def rotate(arr):
    list_tuple = zip(*arr[::-1])
    res = [list(e) for e in list_tuple]
    print(res)


    # reversed_list = arr[::-1]
    # print(reversed_list)
    # list_tuple = zip(*reversed_list)
    # print(list_tuple)
    # list_list = [list(e) for e in list_tuple]
    # print(list_list)

rotate(arr)
