data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
best = ''
for data in data_1:
    if data.isupper() or data.isspace():
        best += data
print(best)

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

result = []
for data3 in "내힘들다":
    result.append(data_2.find(data3))  
print(result)
result.sort()
print(result)

result1 = ''
for num in result:
    result1 += data_2[num]
    
print(result1)

            
