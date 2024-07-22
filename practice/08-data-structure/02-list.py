# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print(my_list.append(4)) # None 
# 원본을 이미 바꾸었기 때문에 반환이 필요 없음 

# extend
my_list = [1, 2, 3]
my_list.extend([4,5,6])
print(my_list) # [1, 2, 3, 4, 5, 6]
# my_list.extend(5) # int 객체는 iterable 가 아님 
my_list.extend([5]) # 이건 가능 반복가능한 친구가 들어가야함 
print(my_list)
my_list.append([9,9,9]) 
print(my_list) # [1, 2, 3, 4, 5, 6, [9, 9, 9]]
#  extend 는 하나의 인자만 가능 !! 

# insert
my_list = [1, 2, 3]
my_list.insert(1,5)
print(my_list) # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list) # [1, 3]

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
print(item1) # 5
print(my_list) # [1, 2, 3, 4]
item2 = my_list.pop(0)
print(item2) # 1
print(my_list) # [2, 3, 4]

# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []

# ////////////////////////////////////////////////////////////////////

# index
my_list = [1, 2, 3]
index = my_list.index(2) # 2가 어디에 있나
print(index) # 1   0, 1 로 1위치

# count
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count) # 3  3 개수 세기 

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse()) # None 원본을 뒤집었기에 새로운 리스트 X 
print(my_list) # 원본이 뒤집어짐 [9, 1, 8, 2, 3, 1]

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)
