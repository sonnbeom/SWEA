arr=' 12345678'
# 길이: 9

def postoreder(node):
    if node > len(arr)-1:
        return
    postoreder(node*2)
    postoreder(node*2+1)
    print(node)
postoreder(1)