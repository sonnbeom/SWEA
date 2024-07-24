# 1. 내장함수를 활용해서 출력해보기!
def reverse_string(req):
    temp = list(req)
    temp.reverse()
    return ''.join(temp)

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

# 1. 내장함수를 활용하지 않고 직접 구현해보기
def reverse_string(req):
    result = ""
    for char in req:
        result = char + result
    return result

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH