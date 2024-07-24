# 내장 함수 이용
def sort_tuple(req):
    new_tuple = ()
    
    return sorted(req)


result = sort_tuple((5, 2, 8, 1, 3))
print(result)

# 내장 함수 이용하지 않고 풀기 리스트로 변환하고 리스트 내장함수로 풀기
def sort_tuple(req):
    new_tuple = ()
    temp = list(req)
    temp.sort()
    tuple(temp)
    new_tuple = temp
    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)