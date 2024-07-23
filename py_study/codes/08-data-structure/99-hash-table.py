# 정수
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set)
# 재실행해도 해쉬함수가 바뀌지 않고 테이블 위치 순서는 변하지 않음 
# 정수는 항상 같은 해시값, 문자열은 아님 !! 


# 문자열
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
# print(my_str_set.pop())
# print(my_str_set.pop())
# print(my_str_set.pop())
# print(my_str_set.pop())
# print(my_str_set.pop())
# 정수와 달리 매번 값 순서가 다름
# 해쉬함수가 매번 재구성 !! 


print(hash(1)) # 1
print(hash(1)) # 1 
print(hash('a')) # 매번 달라짐
print(hash('a')) # 달라짐 근데 a 두개 주소값은 똑같긴함 

# print(hash(1))
# print(hash(1.0))
# print(hash('1'))
# print(hash((1, 2, 3)))

# TypeError: unhashable type: 'list'
# print(hash((1, 2, [3, 4])))
# TypeError: unhashable type: 'list'
# print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
# my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
# my_dict = {{3, 2}: 'a'}
