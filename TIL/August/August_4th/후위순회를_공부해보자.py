arr=' 12345678'

def postorder(now):
    if now > len(arr)-1:
        return
    postorder(now*2)
    postorder(now*2+1)
    print(arr[now])

postorder(1)

li = [10, 11]
print(li.pop())