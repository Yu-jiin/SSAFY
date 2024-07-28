
str = 'hello'
    #  01234

print(str[2:4]) # ll
print(str[:3]) # hel 0부터 3까지
#  [ x : y ] x 부터 y-1 까지 
print(str[3:]) # lo 3부터 끝까지 
print(str[0:5:2]) # hlo  
print(str[::-1]) # elleh = 반대로

my_list = [1, 'a', 3, 'b', 5]
#          0   1   2   3   4
print(my_list[1]) # a
print(my_list[2:4]) # 3 b
print(my_list[:3]) # 1 a 3
print(my_list[0:5:2]) # 1 3 5

my_list1 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

print(len(my_list1)) # 5
print(my_list1[4][-1]) # !!!
print(my_list1[-1][1][0]) # w
#  맨 뒤에 리스트 ['hello', 'world', '!!!'] 
#  1번째 'world' 의 0번째 = w 

my_list[0] = 100
print(my_list)

#  튜플 = (( ))로 표기
#  튜플은 불변 ( 변경 불가 제발 )
my_tuple = (1,'a',3,'b',5)
#           0  1  2  3  4

# range(시작 값, 끝 값, 증가 값)
my_range = range(5)
print(my_range) # range(0, 5)
# range는 list로 형 변환 시에 출력 값 확인 가능하다
print(list(my_range)) # [0, 1, 2, 3, 4]

# 딕셔너리 - key 는 변경 불가능한 자료형만 사용 가능 !!!
#            value 는 모든 자료형 가능 {}로 표기
my_dict = {}
my_dict1 = {
    'key' : 'value'
}
my_dict2 = {
    'apple' : 12,
    'list' : [1,2,3]
}

print(my_dict1) # {'key': 'value'}
print(my_dict2) # {'apple': 12, 'list': [1, 2, 3]}

print(my_dict2['apple']) # 12
print(my_dict2['list']) # [1,2,3]
my_dict2['banana'] = 50  # 추가
print(my_dict2)
my_dict2['apple'] = 20 # 변경
print(my_dict2)


# set 중괄호로 표기하지만
# 빈 세트 만들기는
set0 = set()
set2 = {3,6,9}
set1 = {1,2,3}
print(set1 | set2) # 합집합 1 2 3 6 9 합집합 || 
print(set1 - set2) # 차집합 1 2  
print(set1 & set2) # 교집합 3

# None 값 없음
# Boolean True False 

print(3 > 1) # True 
#  Collection == set 비스무리

# 불변  str tuple 스트링 튜플 제발 기억해
# 시퀀스 = str list tuple
# 비시퀀스 = dict set  

# 암시적 형변환 - 정수와 실수의 연산에서 Boolean, Numeric Type 

# 멤버십 연산자 in / not in
# 시퀀스형 연산자 + 결합연산자   * 반복연산자 
print('hi'*3)
print([1,2]*2)

