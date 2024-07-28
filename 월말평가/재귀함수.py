#  팩토리얼
# factorial 함수는 자기 자신을 재귀적으로 호출하여 n의 팩토리얼을 계산 
# 재귀호출은 n이 0이 될 때까지 반복되며, 종료 조건을 설정하여 재귀 호출 멈춤
def factorial(n):
    if n == 0:
        return 1
    else:
        # 10! = 10 * 9 * 8 * 7 *~~~~~~
        #   = 10 * 9!
        result = n * factorial(n-1)   
    return result   
print(factorial(5))


def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
print(fac(5))

# 피보나치 수열  n = (n-2) + (n-1) 가 핵심!! 
# 피보나치 수열의 index n의 값을 리턴
# 피보나치 수열 : 1,1,2,3,5,8,12,21,34
def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(6))
    
def fibo_list(n):
    for i in range(n):
        print(fibo(i), end= " ")
        
print(fibo_list(6))