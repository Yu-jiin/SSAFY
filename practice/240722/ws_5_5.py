# 아래 함수를 수정하시오.
# 홀수를 모두 제거하고 짝수만을 남긴 리스트 반환
# extend pop 함수 사용 
def even_elements(my_list):

    result = []
    index = 0
    
    while index < len(my_list):
        if my_list[index] % 2 == 0:
            result.extend([my_list[index]])
            index += 1
        else:
            my_list.pop(index)

            
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
