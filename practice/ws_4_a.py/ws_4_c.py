matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래에 코드를 작성하시오.
# matrix_len = len(matrix)

matrix_len = 0
for mat in matrix:
    matrix_len += 1
print(matrix_len)  ## 길이

for number in matrix:
    # print(number)
    pass
         
print('-----------------------------------')
temporary_len = 0
for number in matrix:
    for num in number:
        if len(number) != temporary_len:
            temporary_len += 1
        if len(number) == temporary_len:
            if temporary_len < 5:
                print(f'{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다. ')
            temporary_len = 0
            

print('-----------------------------------')
        
for i,each in enumerate(matrix):
    for index in range(0,len(each)):
        print(f'matrix의 {i},{index} 번째 요소의 값은 {each[index]} 입니다. ')

# print('----------------')
# for i, each in enumerate(matrix):
#     print(i)
#     print('----------------')
#     print(each)
#     print('----------------')
#     print(i,each)
print('----------------')
    
for index,each in enumerate(matrix):
    for i in range(0,len(each)):
        print(f'matrix의 {index},{i} 번째 요소의 값은 {each[i]} 입니다. ')