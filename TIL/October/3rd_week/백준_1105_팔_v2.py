'''
1 20

18 29
80 88

800 804

8808 8880

2개

188 18

128 138

128 128
만약 십의 자리가 다르다면 일의자리는 비교할 필요가 없다

=> 앞의 자리 수와 뒤의 자리수가 다르다면 뒤를 비교할 필요가 없다는 얘기다

'''

l, r = input().split()

cnt = 0

left_len = len(l)
r_len = len(r)
# 0, 1, 2 128
print(left_len)
for i in range(left_len-1, -1, -1):
    print(f'i = {i}')
    if l[i] == '8' and r[i] == '8':
        if i > 0:
            if l[i-1] == r[i-1]:
                cnt += 1
        else:
            # if i < r_len-1 and
            cnt += 1
print(cnt)

