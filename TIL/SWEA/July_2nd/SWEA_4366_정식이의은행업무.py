e_input = input()
sam_input = input()
ans = 0
e = []
eLen = 0
sam = []
samLen = 0
for i in e_input:
    eLen += 1 
    e.append(int(i))
for i in sam_input:
    samLen += 1
    sam.append(int(i))


tmp = 1
tempE = 1
samSum = 0
eSum = 0



for i in range((eLen-1), -1, -1):
    num = e[i]
    eSum += num * tempE
    tempE *= 2
for i in range((samLen-1), -1, -1):
    num = sam[i]
    samSum += num * tmp
    tmp *= 3



def check(req):
    global ans
    if req in temp:
        ans = req
        return True
    return False

t = 1
temp = []
for i in range((samLen-1), -1, -1):
    num = sam[i]
    if num == 2:
        r = samSum - t
        k = samSum - (t*2)
        temp.append(r)
        temp.append(k)
    elif num == 1:
        r = samSum - t
        k = samSum + t
        temp.append(r)
        temp.append(k)
    else:
        r = samSum + t
        k = samSum + (t*2)
        temp.append(r)
        temp.append(k)
    t *= 3

t = 1
for i in range((eLen-1), -1, -1):
    num = e[i]

    if num == 1:
        k = eSum - t
        if check(k):
            break
    else:
        k = eSum + t
        if check(k):
            break
    t *= 2

print(ans)
'''
배열을 만들고

방문 배열을 만든다. [][]
y에는 0 1 2 만 넣는다
212

212 18 3 2 = 23

210 18 3 0 = 21
211 18 3 1 = 22

222 18 6 2 = 26
202 18 0 2 = 20

112 14 
012 6

1010 8 0 2 0 = 10
1110 = 14
0010 = 2
1000 = 8
1011 = 11

'''