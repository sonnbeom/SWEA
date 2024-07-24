
#1. 첫번째 인자에 두번째 인자가 몇개 있는지 내장함수를 써서 알아보기

# 아래 함수를 수정하시오.
def count_character(param, reqChar):
    return param.count(reqChar)

result = count_character("Hello, World!", "o")


print(result)  # 2

#1. 첫번째 인자에 두번째 인자가 몇개 있는지 count 내장함수를 쓰지 않고 구현해보기
def count_character(param, reqChar):
    answer = 0
    for char in param:
        if char == reqChar:
            answer += 1
    return answer
    
result = count_character("Hello, World!", "o")

print(result)  # 2