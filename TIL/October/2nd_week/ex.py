a = [1,2,3]
b = 4
c = max(b, max(a))
print(c)

a.remove(2)
print(a)

import itertools

d = [1,2,3,4,5,6]
d_len = len(d)//2
import copy
com = list(itertools.combinations(d, 3))
print(com)
s = set()
for co in com:
    co = tuple(co)
    if co not in s:
        other = copy.deepcopy(d)
        for c in co:
            if c in other:
                other.remove(c)
        other = tuple(other)
        print(f'other = {other} co= {co}')
        s.add(tuple(other))
        s.add(co)
print(s)

