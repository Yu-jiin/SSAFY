#  비시퀀스 구조 - dict, set 
#  dict - 고유한 항목들의 정렬되지 않은 컬렉션

my_dict = {
    'name' : 'jiin',
    'age' : 24,
    'phone' : '010',
    'addr' : 'Busan'
}

# my_dict.claer() = 딕셔너리의 모든 키 / 값 쌍 제거 

# get은 키에 연결된 '값' 반환 없으면 None 
print(my_dict.get('name')) # 키에 연결된 값을 반환 없으면 None 

print(my_dict.get('feel','good')) # 키에 연결된 값을 반환하거나 없으면 good 반환 

print(my_dict.keys()) # dict_keys(['name', 'age', 'phone', 'addr']) 키 반환

print(my_dict.values()) # dict_values(['jiin', 24, '010', 'Busan']) 값을 반환 

print(my_dict.items()) # dict_items([('name', 'jiin'), ('age', 24), ('phone', '010'), ('addr', 'Busan')])
# 키 값 쌍 모은 객체 반환 

print(my_dict.pop('addr')) # Busan
# pop() 키를 제거하고 연결됐던 값 반환
# 없으면 error, default 값 반환 

print(my_dict.pop('feel','good')) # good
# pop(x,y) 키 x 를 제거하고 값 반환 x가 없으면 y반환

print(my_dict.setdefault('name')) # jiin
# 키와 연결된 값 반환 !!

print(my_dict.setdefault('feel','good')) # good
print(my_dict) # {'name': 'jiin', 'age': 24, 'phone': '010', 'feel': 'good'}
# 키와 연결된 값 반환, 없으면 키와 벨류 모두 추가하고 벨류 반환 

other_dict = {
    'name' : 'hyunjin'
}
my_dict.update(other_dict)
print(my_dict) # {'name': 'hyunjin', 'age': 24, 'phone': '010', 'feel': 'good'}

my_dict.update(country = 'Korea')
print(my_dict) # {'name': 'hyunjin', 'age': 24, 'phone': '010', 'feel': 'good', 'country': 'Korea'}
# 이렇게 추가도 가능 .. !! 

# set - 고유한 항목들의 정렬되지 않은 컬렉션 중복값 안됨 
my_set = {'jiin','24','Busan','Sad',1,2,84}

my_set.add('Me!!')
print(my_set) # {1, 2, 84, 'Me!!', 'Sad', 'jiin', '24', 'Busan'} 
# set는 순서 정렬 상관 없이 
my_set.add('jiin') # 중복값 절대 안돼 
print(my_set) # {1, 2, 'Sad', 'Busan', 84, 'jiin', 'Me!!', '24'}

# my_set.clear() 세트 모든 항목 제거

my_set.remove(1)
print(my_set) # {'jiin', '24', 2, 'Sad', 84, 'Me!!', 'Busan'}
# 만약에 제거할 값이 없을 경우 Key error 

my_set.pop() # 임의의 항목을 반환하고 해당 항목 제거 !! 
print(my_set) # {2, '24', 'jiin', 84, 'Me!!', 'Sad'} # Busan 제거 됐다악

# my_set.remove(2)
my_set.discard('afsdf')
print(my_set) # 제거하려는 값이 없어도 remove와 다르게 에러 없음 

update_list = ['happy','Grill']
my_set.update(update_list)
print(my_set) # {'jiin', '24', 'Me!!', 'happy', 84, 'Sad', 'Busan', 'Grill'}
# .update() 세트에 다른 iterable 요소 추가
i = {
    'a' : 1
}
my_set.update(i)
print(f'@@@@{my_set}') # @@@@{'Me!!', '24', 'a', 'Sad', 'happy', 'Busan', 84, 'jiin', 'Grill'} 이거도 가능

set1 = {1,2,348,3}
set2 = {'ac','bjd',1,2}

a = set1.difference(set2) # set1 - set2
print(a) # {3, 348}
print(set1- set2) # {3, 348}

b = set1.intersection(set2) # set1, set2에 모두 들어있는 요소 
print(b) # {1, 2}
print(set1 & set2) # {1, 2}

c = set1.issubset(set2)
print(c) # False
# set1의 항목이 모두 set2에 들어있으면 True

d = set1.union(set2)
print(d) # {1, 2, 3, 'bjd', 'ac', 348} 교집합 