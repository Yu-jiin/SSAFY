# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# input 값 
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1

# 표준 입력 예제
# '''
# a = int(input())                        정수형 변수 1개 입력 받는 예제
# b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
# d = float(input())                      실수형 변수 1개 입력 받는 예제
# e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
# h = input()                             문자열 변수 1개 입력 받는 예제
# '''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    num = map(int, input().split())
    sum = 0
    for n in num: 
        if n % 2 == 1:
            sum = sum + n
    print(f'#{test_case} {sum}')
    
    pass

# num이 map 이니까 반복문으로 각각 풀어줘야해 

T = int(input())

for test_case1 in range(1, T + 1):
    num = map(int,input().split())
    sum = 0
    for n in num:
        if n % 2 == 1:
            sum += n
    print(sum)