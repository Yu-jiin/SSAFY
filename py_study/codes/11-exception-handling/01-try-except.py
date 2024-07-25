# try-except
try:
    result = 10 / 0
except ZeroDivisionError: # ZeroDivisonError 생략해도 값 똑같음 모든 예외에서 반응 
    print('0으로 나눌 수 없습니다.')

try:
    num = int(input('숫자 입력 : '))
except ValueError:
    print('숫자가 아닙니다. ')

# 복수 예외처리
# 100으로 나눌 값을 입력하고 출력하는 코드
try:
    x = int(input('100으로 나눌 값 입력해 : '))
    print(100 / num)
    y = 10 / x
except ValueError:
    print('숫자 입력해라')
except ZeroDivisionError:
    print('0 말고')
except:
    print('알 수 없는 에러가 발생 ')
else:
    print (f'결과 : {y}')
finally:
    print('프로그램 종료')