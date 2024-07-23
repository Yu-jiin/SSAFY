# add
my_set = {'a', 'b', 'c', 1, 2, 3} # 순서가 없음 set !! 
my_set.add(4)
print(my_set) # 4는 매번 순서 다르게 들어감 .. 왜이래 

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) # set() 빈 세트는 이렇게
              # dict 빈 딕은 {}

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set) # {'b', 1, 3, 'a', 'c'}
# my_set.remove(10) 없는 값 제거할라면 키 에러 

# pop 세트에서 임의의 요소를 제거하고 반환
# 리스트는 끝에걸 제거 dict은 위치 지정
# 근데 set에서의 pop은 임의의 요소 제거 .. and 반환 
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # 진짜 랜덤픽 b 
print(my_set) # {1, 2, 'a', 3, 'c'}

# discard 세트에서 항목x를 제거, remove와 달리 에러 없음 
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {'b', 1, 3, 'c', 'a'}
my_set.discard(10) # 10이 없고 제거할라해도 에러 X 

# update 세트에 다른 iterable 요소 추가 
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1,4,5])
print(my_set) # {'a', 2, 1, 'b', 'c', 3, 4, 5} -> hash 테이블에 배치된 순서대로 그러나 재실행하며 바뀜 
# 1은 중복이라 하나가 안들어가고 4,5 가 들어감 

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4} set1 - set2
print(set1.intersection(set2)) # {1, 3} 교집합 
print(set1.issubset(set2)) # set2에 없는 것들이 set1 에 있기에 False 
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) # False set1은 set2를 모두 포함하지 않는다
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9} 합집합 
  # 위는 해쉬테이블에 작성된 순대로 출력 정수는 왜 ? 
  # 

## 문자열이 없으니까 뭔가 정렬된 거 같음 .. 

