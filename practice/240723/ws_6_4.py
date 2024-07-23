# 아래 함수를 수정하시오.
def get_keys_from_dict(my_dict):
    result = (my_dict.keys())
    a = []
    for re in result:
        a.append(re)
    return a


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']
