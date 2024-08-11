res = 0
small = input()
big = input()

smallLen = len(small)
bigLen = len(big)

for idx in range(bigLen- smallLen +1):
    tempBig = big[idx: smallLen+idx]
    print(tempBig)
    if small == tempBig:
        res += 1
print(res)