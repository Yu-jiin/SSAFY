
# 팩토리얼 재귀 함수
def fac(num):
    if num == 0:
        return 1
    else:
        return num * fac(num-1)

result_1 = fac(5)
print(result_1) # 120 완료 


# basd(밑)과 exponent(지수)를 인자로 받아 제곱 값을 반환하는 함수 power 작성
def power(base,exponent):
    '''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
    if exponent == 0:
        return 1
    else:
        return base*power(base,exponent-1)

result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8



# 자연수를 입력받아, 각 자릿수의 합을 반환하는sum_of_digits 를 작성하시오
def sum_of_digits(num):
    '''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
    if num < 10:
        return num
    else:
        return (num % 10) + (sum_of_digits(num//10))

result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6


    