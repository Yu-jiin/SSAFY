# break
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4

# continue
for i in range(10):
    if i % 2 == 0:
        continue # 짝수 건너 뛰어라 
    print(i)

# pass
for i in range(10):
    pass

# break 예시 1 - "프로그램 종료 조건 만들기"
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')


# break 예시 2 - "리스트에서 첫번째 짝수만 찾은 후 반복 종료하기"
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False
for number in numbers:
    if number % 2 == 0:
        print(f'첫번째 짝수 : {number}')
        found_even = True
        break
if found_even == False:
    print('짝수 못 찾음') ## 안에 짝수가 있기에 실행되진 않음 


# continue 예시 - "리스트에서 홀수만 출력하기"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)