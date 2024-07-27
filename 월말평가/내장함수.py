numbers = [1,2,3,4,5]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers, reverse = True))

# map(function, iterable)
# 순호나 가능한 구조를 모든 요소에 함수를 적용하고, 그 결과를 map 으로 반환
number = [1,2,3]
result = map(str,number)
print(result)
print(list(result)) # 꼭 list 붙여주기 

# number1 = input().split()
# # split() 문자열 쪼개기 내장함수. 
# print(number1) # ['1', '2', '3']
# number2 = list(map(int,input().split()))
# print(number2) # [1,2,3]

# zip(*iterables) 임의의 iterable 을 모아 튜플을 원소로 하는 zip object 반환
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls,boys)
print(pair) # <zip object at 0x000001FFCC594880>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]


kr_scores = [10,20,30,50]
math_scores = [20,40,50,70]
en_scores = [40,20,30,50]
# 여러 개의 리스트를 동시에 조회할 때 
for student_s in zip(kr_scores,math_scores,en_scores):
    print(student_s)
# (10, 20, 40)  결과값 
# (20, 40, 20)
# (30, 50, 30)
# (50, 70, 50)


# 함수는 코드내부의 local scope를 그 외는 global scope
# local scope = 함수가 호출될 때 생성하고, 함수가 종료될 때 까지 함수 종료하면 끝



a = 1
b = 2
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a,b,c) # 10,2,500 enclosed 함수는 local 까지 접근 가능 
    local(500)
    print(a,b,c) #10,2,3 c는 local 함수가 종료되면서 사라져서 3
enclosed()
print(a,b) #1,2 전역변수 a,b 를 참고 
#  enclosed 함수는 local 까지 접근 가능 



# num = 0
# def increment():
#     print(num) 
#     # SyntaxError: name 'num' is used prior to global declaration
#     global num
#     num +=1

# print(increment)


num = 0
def increment():
    global num
    num +=1 
    # global 은 함수 선언하고 첫번째로 써줘야함 
increment() # 꼭 선언해주고 print 시켜줘야함 !! 
print(num) # 1

#  패킹 ! 
packed_values = 1,2,3,4,5
print(packed_values) # (1, 2, 3, 4, 5) 변수에 담긴 값들은 튜플로 묶임 
print(type(packed_values)) # <class 'tuple'>

n = [1,2,3,4,5]
a, *b, c = n
print(a) #1
print(b) #[2, 3, 4] *는 남은 요소들을 리스트로 패킹 
print(c) #5

# 언패킹 = * 붙이면 리스트 요소를 언패킹하여 인자로 전달 
def unpacked(x,y,z):
    print(x,y,z)
names = ['alice', 'jane', 'peter']
unpacked(*names) # alice jane peter

#  ** 언패킹 - 딕셔너리 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달
def my_unpaced(x,y,z):
    print(x,y,z)
my_dict = {'x' : 1, 'y' : 2, 'z' : 3}
my_unpaced(**my_dict) # 1 2 3

# * 패킹 연산자로 사용될 때, 인자를 하나의 튜플로 묶음
# * 언패킹 연산자로 사용될때 시퀀스, 반복 가능한 객체를 각각으 요소로 언패킹하여 인자로 전달

# ** 언패킹 연산자로 사용될 때 - 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달 

#  lamb da 표현식 
addition = lambda x, y : x+y
result = addition(3,5)
print(result)

n3 = [1,2,3,4,5]
square = list(map(lambda x : x**2, n3))
print(square)