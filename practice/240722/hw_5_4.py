# 아래 함수를 수정하시오.
def find_min_max(my_list):
    ma = max(my_list)
    mi = min(my_list)
    result = []
    result.append(mi)
    result.append(ma)
    return tuple(result) ## list 를  tuple 로 변환 

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
