# 1. Positional Arguments
def greet(name,age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
greet('Jiin', 24)
greet(24,'Jiin') # 바꾸면 24님 Jiin 살 이시군요 
# greet('Jiin') 인자 값 누락 시 오류 

# 2. Default Argument Values
def greet(name, age=30):
    print(f'안녕하세요, {name}님! {age}살이시군요.')
    
greet('Bob') # 안녕하세요 Bob님 30살이시군요
greet('Charlie', 40) # 안녕하세요 Charlie님 40살이시군요

# 3. Keyword Arguments
def greet(name,age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='Dave', age=35) # 가능
greet( age=35, name='Dave') # 가능 
# greet(age=35, 'Dave') positional argument follows keyword argument

# 4. Arbitrary Argument Lists
def calculate_sum(param, *args):
    print(args)
    print(type(args))
    
    total = sum(args)
    print(f'합계: {total}')

calculate_sum(1,2,3,4,5) # 15

# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)
    
print_info(name='Eve', age = 30) #{'name : 'Eve', age = 30}

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
