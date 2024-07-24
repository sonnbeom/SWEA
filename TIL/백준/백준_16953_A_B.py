a, b = map(int, input().split())
count = 0

check = True

while(True):
    if a == b:
        break
    elif (b-1)%10 == 0:
        b = (b-1)/10
        count += 1
    elif b/2 != 0 and b%2 == 0:
        b /= 2
        count += 1
    else:
        count = -1
        break

if count == -1:
    print(count)
else:
    print(count+1)

