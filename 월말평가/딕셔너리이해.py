

def get_value_from_dict(my_dict, name):
    return my_dict.get(name)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice



def intersection_sets(a,b):
    return a.intersection(b)

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)