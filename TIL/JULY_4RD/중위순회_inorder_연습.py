arr=' 12345678'
# 길이: 9
def inorder(node):
    if node > len(arr)-1:
        return
    inorder(node*2)
    print(arr[node])
    inorder(node*2+1)

inorder(1)