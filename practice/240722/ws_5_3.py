# 아래 함수를 수정하시오.
def sort_tuple(my_list):
    new_tuple = ()
    
    a = list(my_list)
    a.sort()
    print(a)
        
    return tuple(a)

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
