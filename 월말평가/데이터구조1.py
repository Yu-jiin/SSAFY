# 문자열 조회/ 탐색
str = 'banana'

print(str.find('b')) # 0
#  str.find('b') = b의 첫번째 위치 반환, 없으면 -1

print(str.index('n')) # 2
#  str.index('n') n의 첫번째 위치를 반환, 없으면 오류 

print(str.isupper()) # False
#  str.isupper() 대문자 여부

print(str.islower()) # True 
#  str.islower() 소문자 여부 

print(str.isalpha()) # True
#  str.isalpha() 알파벳 문자 여부 

# 문자열 조작 메서드
print(str.replace('b', 'a')) # aanana

str1 = '   jiin is now sleepy'
print(str1.strip())
# str1.strip() 문자열의 시작과 끝에 있는 공백, 문자 제거

print(str1.split(' ')) # ['', '', '', 'jiin', 'is', 'now', 'sleepy']
# str1.split() 공백이나 특정 문자를 기준으로 분리

str2 = ['Hello','Jiin']
print('-'.join(str2)) # Hello-Jiin
# '-'.join(str2) 문자열을 연결한 문자열을 반환 !

# 메서드는 이어서 사용 가능 !!! 
text = 'heLLo, JiIn!!'
new_text = text.swapcase().replace('!!','@@')
print(new_text) # HEllO, jIiN@@

# --------------------------------------------
# 리스트 값 추가 및 삭제 메서드

list1 = ['jiin','is','24','tired']
list1.append('아오')
print(list1) # ['jiin', 'is', '24', 'tired', '아오']
#  append는 리스트에 요소를 추가하지만, 그 자체로는 값 반환 X
# append는 리스트를 직접 수정하기에, 그 결과 변수에 저장할 필요 X 

list2 = [6,8,54,1]
list2.extend(list1)
print(list2) # [6, 8, 54, 1, 'jiin', 'is', '24', 'tired', '아오']

list2.insert(0, '추가')
print(list2) # ['추가', 6, 8, 54, 1, 'jiin', 'is', '24', 'tired', '아오']
# .insert(i,x) 리스트의 지정한 인덱스 i위치에 x 삽입 

list2.remove('아오')
print(list2)
