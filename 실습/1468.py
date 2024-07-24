# 내장 함수를 이용해 풀어보자
def remove_duplicates(req):
    return set(req)

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# 내장 함수를 이용하지 않고 풀어보자
def remove_duplicates(req):
    new_lst = []
    for num in req:
        if num not in new_lst:
            new_lst.append(num)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
