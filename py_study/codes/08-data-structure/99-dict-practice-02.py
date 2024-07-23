# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기

a = [1,2,6]
a.append(7)
print(a)

# # 1. [] 표기법을 사용한 방법
# def dict_invert(input_dict):
#     new = {}
#     for k,v in input_dict.items():
#         if v not in new:       
#             new[v] = [k] 
#         else:
#             # new[v].append(k)  둘 다 같은 값 반환 
#             new[v] = new[v] + [k]
#     return new


# 2. get 메서드를 사용한 방법
def dict_invert(input_dict):
    new = {}
    for k,v in input_dict.items():
        new[v] = new.get(k,[k])
    return new

# # 3. setdefault 메서드를 사용한 방법
# def dict_invert(input_dict):
#     pass


print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})
)  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
