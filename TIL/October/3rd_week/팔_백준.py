l, r = input().split()

cnt = 0
l_idx = len(l)-1
r_idx = len(r)-1

while True:
    if l[l_idx] == r[r_idx] == "8":
        if l_idx -1 > 0:
            if l[l_idx-1] == r[r_idx-1]:
                cnt += 1
        else:
            if r_idx == 0:
                cnt += 1

    l_idx -= 1
    r_idx -= 1

    if l_idx < 0:
        break

print(cnt)