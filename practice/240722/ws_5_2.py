# 아래 함수를 수정하시오.
def remove_duplicates(lst):
    
    new_lst = []
    
    for item in lst:
        if item not in new_lst: 
            new_lst.append(item)
    
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# 중복 제거를 빈 리스트에 값이 없다면 추가하는 형식으로 바꿔 생각 
 
