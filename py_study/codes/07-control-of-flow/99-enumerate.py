fruits = ['apple', 'banana', 'cherry']

# 1번째 인덱시 2번째 요소
for index, fruit in enumerate(fruits):
    print(f'인덱스 {index} : {fruit}')
    
# 인덱스 3으로 시작
for index, fruit in enumerate(fruits,3):
    print(f'인덱스 {index} : {fruit}')
