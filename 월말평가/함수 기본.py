#  함수

# 두수의 합을 구하는 함수
def sum1(x,y):
    return x + y

a = sum1(3,5)
print(a)    

# 입력된 이름 값에 인사하는 메시지
def greet(name):
    return name + ' 안녕' 
    # message = name + '안녕' print(message)
print(greet('J'))

# 매개변수 - 함수를 정의할때 함수가 받을 값을 나타내는 변수
# 인자 - 함수 호출할 때 실제로 전달 되는 값 
#  위 함수에서 name 은 매개변수 J는 인자


# 임의의 인자 목록 - 정해지지 않은 개수의 인자를 처리하는 인자
# 매개변수 앞에 * *args 로 사용 여러개를 tuple로 처리 
def calcu_sum(*args):
    result = sum(args)
    print(result)

calcu_sum(1,2,3) # 6

# 임의의 키워드 인자 목록 - 정해지지 않은 개수의 인자
# 매개변수 앞에 ** 를 붙여 사용하며 여러개를 dict로 처리
def print_info(**kwargs):
    print(kwargs)
print_info(name = 'Eve', age = '25') # {'name': 'Eve', 'age': '25'}


def func(pos1,pos2,default_arg = 'default', *args, **kwargs):
    print(pos1) # 1
    print(pos2) # 2
    print(default_arg) # 3
    print(args) # (4,5,6)
    print(kwargs) # {'key1' : 'value, 'key2' = 'value2'}
    
func(1,2,3,4,5,6,key1='value1', key2='value2')

