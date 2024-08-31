# li = [1,2,3]
# se = set(li)
# print(se)
#
# a = 22 // 5
# b = 43 // 5
# print(a, b)
import itertools
# for i in range(3, -1, -1):
#     print(i)

li = [1,2,3,4]

for a in itertools.combinations(li, 2):
    print(a)

w = [1,2,3]
w.sort(reverse=True)
print(w)