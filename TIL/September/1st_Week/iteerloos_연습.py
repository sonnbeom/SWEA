import itertools
li = [[0,1,2,3], [1,2], [[1,2],[0,2],[1,3]], [[0,1,2], [0,1,3]]]
l = itertools.combinations(li, 2)
k = itertools.permutations(li, 2)
print(list(l))
print(list(k))

ex = [1,2,3]

l = itertools.combinations(ex, 2)
k = itertools.permutations(ex, 2)
print(list(l))
print(list(k))