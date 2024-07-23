# 아래 함수를 수정하시오.
def get_value_from_dict(dic, k):
    
    
    result = dic.get(k)
    return result


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice
