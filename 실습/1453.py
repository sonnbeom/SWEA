# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, reqKey, reqValue):
    new_dict = dictionary.copy()
    for key, value in dictionary.items():
        new_dict[key] = value
    new_dict[reqKey] = reqValue
    
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
