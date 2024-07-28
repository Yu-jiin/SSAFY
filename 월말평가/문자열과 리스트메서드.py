data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'

answer = ''
for data in data_1:
    if data.isupper() or data.isspace():
        answer += data
print(answer)

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []

find_str = '내힘들다'
for find in find_str:
    result = data_2.find(find)
    arr.append(result)
print(arr)

arr.sort()
print(arr)

answer2 = ''
for num in arr:
    answer2 += data_2[num]
print(answer2)

