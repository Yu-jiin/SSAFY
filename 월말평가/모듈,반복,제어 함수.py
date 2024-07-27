#  모듈 - 한 파일로 묶인 변수와 함수 모음
#         특정한 기능을 하는 코드가 작성된 파이썬 파일

# math 모듈의 sqrt 함수는 주어진 숫자의 제곱근(square root)을 계산하여 반환하는 함수
# 모듈 사용하려면 무조건 import 
import math
print(math.sqrt(4))

from math import sqrt # 두개로 사용 가능 
# 모듈명.변수명 !! 

#  패키지 - 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것
#  pip = 외부 패키지들을 설치하도록 도와주는 파이썬 패키지 관리 시스템
#  requests = api 이용하게 해주는 외부 패키지 pip 로 install
#  pip install requests 

#  제어문 = 조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

#  조건문 = 주어진 조건식을 평가하여 해당 조건이 참인 경우에만 코드블록 실행
#  if, elif, else

#  반복문 = 주어진 코드 블록 여러 번 반복
#  for - 특정 작업 반복 , while - 주어진 조건이 참인 동안 반복  
#  반복 가능한 객체 - 시퀀스 뿐만 아니라 비시퀀스인 dict, set 도 포함
 
my_dict = {
    'x' : 10,
    'y' : 20,
    'z' : 30
}
for key in my_dict:
    print(key) # x,y,z 출력 
    print(my_dict[key]) # 10,20,30 출력

numbers = [1,2,3,-10,5]
for i in range(len(numbers)): # range 꼭 붙이자 지인아...
# # range(len(numbers))는 [0, 1, 2, 3, 4]를 생성합니다. 
    numbers[i] = numbers[i]*2
print(numbers) # [2, 4, 6, -20, 10]

# 중첩된 반복문
#  안쪽 반복문은 바깥족 리스트 각 항목에 대해서 실행
outers = ['A','B']
inners = ['c','d']
for out in outers:
    for inn in inners:
        print(out,inn)
# A c
# A d
# B c
# B d

elements = [['A','B'],['C' ,'D']]
for element in elements:
    for ele in element:
        print(ele) 
# A
# B
# C
# D


# while = 조건식이 거짓이 될때까지 반복 
#  양의 정수가 되는 값 받기
# 조건식이 true 가 될때까지 반복
    # number = int(input('양의 정수 입력해주세요 : '))
    # # 그러면 조건식을 num <= 0 으로 해야겠지 ?
    # while number <= 0:
    #     if number <0:
    #         print('음수임')
    #     else:
    #         print('0은 양의 정수가 아님')
    #     number = int(input('양의 정수 입력해주세요 : '))
    # #  while 은 input에서 좀 적절함 몇번 반복인지 모르니까 

# -9999 입력하면 프로그램 종료하게 만들기
    # number = int(input('양의 정수 입력해주세요 : '))
    # while number <= 0:
    #     if number == -9999:
    #         print('프로그램 종료')
    #         break
    #     if number <0:
    #         print('음수임')
    #     else:
    #         print('0은 양의 정수가 아님')
    #     number = int(input('양의 정수 입력해주세요 : '))

# 리스트에서 첫번째 짝수 찾은 후 반복 종료하기 만들기
numbers = [1,3,5,6,7,9,10,11]
found_even = False
for num in numbers:
    if num %2 == 0:
        found_even = True
        print(num)
        break
if not found_even:
    print('못찾음')

# 리스트에서 홀수만 출력하기
for num in numbers:
    if num % 2==0:
        continue
    print(num)

# List Comprehension 
n = [1,2,3,4,5]
squared_n = [i**2 for i in n]
print(squared_n) #[1, 4, 9, 16, 25]

for _ in range(5):
    print("Hello, World!")
# _반복변수의 값을 사용하지 않겠다

# 2차원 배열 생성 list comprehension 사용
data1 = [[0]*(5) for _ in range(5)]
print(list(data1))

result = [i for i in range(10) if i % 2 == 0]
print(result)


# 내장 함수 help 사용하면 모듈에 무엇이 들어있는지 확인 가능
# enumerate = iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
fruits = ['apple','banana','cherry']
for index,fruit in enumerate(fruits):
    print(f'{index} : {fruit}')
# 0 : apple
# 1 : banana
# 2 : cherry