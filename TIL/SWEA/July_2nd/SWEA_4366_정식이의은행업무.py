e_input = input()
sam_input = input()

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

temp = []
jinT = 1
samSum = 0
for i in sam:
    samSum += i * jinT
    jinT *= 3
r = 1
t = 1


for i in range(samLen):
    num = sam[i]
    if num == 2 and i == 0:
        r = samSum - t
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

print(*temp)
'''
배열을 만들고

방문 배열을 만든다. [][]
y에는 0 1 2 만 넣는다
212

212

210
211

222 
202 12

112 14
012 6



'''