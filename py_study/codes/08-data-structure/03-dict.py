# clear 딕셔너리의 모든 키/값 쌍을 제거
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {} 

# get 키 연걸된 값을 반환하거나 키가 없으면 None 혹은 기본 값 반환 
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) # Alice
print(person.get('country')) # None //dict 키 값 접근 방법은 
print(person.get('age')) # 25 //get 메서드 or 대괄호로 접근 두가지
print(person.get('country', 'Unknown')) # None 말고 Unknown 
# print(person['country']) 이건 키 값이 없으니 에러 발생 

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age'])
for k in person.keys():  # dict_keys 가 리스트이니
    print(k) # name        반복을 통해 풀어내기가 가능 
             # age

# values # 딕셔너리 값을 모은 객체 반환 
person = {'name': 'Alice', 'age': 25}
print(person.values()) # dict_values(['Alice', 25])
for k in person.values():
    print(k) # Alice
             # 25

# items # 딕셔너리 키/값 쌍을 모은 객체를 반환 
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
for k,v in person.items(): # 임시변수 두개 주면 각각으로 풀어짐 Unpacking
    print(k,v) # name Alice
               # age 25
    print(k)
    print(v)

# pop # 키를 제거하고 연결됐던 값을 반환(없으면 에러나 defualt 반환)
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
# print(person.pop('country')) # KeyError : 'country'

# setdefault   get메서드 플러스 알파 역할
# 알면 문제풀이에 유용하게 쓰임 .. !!! 
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country' , 'KOR')) # KOR
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOR'}

# update  마지막에 추가된 값으로 갱신 ! 
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}
person.update(other_person)
print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
person.update(age = 50, country = 'KOR')
print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOR'}

a = {}
b = {'name' : 'Alice', 'age' : 25}
a.update(b)
print(a)
b['name'] = 'Harry'
print(a)
print(b)