# find
text = 'banana'
print(text.find('a')) # 1
print(text.find('z')) # -1

# index
print(text.index('a')) # 1
# print(text.index('z')) #
 
# isupper
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper()) # T
print(string2.isupper()) # T


# islower
print(string1.islower()) # F
print(string2.islower()) # F

# isalpha
string1 = 'Hello'
string2 = '123heksjfi85'

print(string1.isalpha()) # T
print(string2.isalpha()) # F

# replace
text = 'Hello, world!'

# strip
text = '  Hello, world!  '

# split
text = 'Hello, world!'

# join
words = ['Hello', 'world!']

# capitalize
text = 'heLLo, woRld!'

# title
# upper
# lower
# swapcase


# # 참고
# # isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
# print("isdecimal() 메서드 예시:")
# print("'12345'.isdecimal():", '12345'.isdecimal())
# print("'123.45'.isdecimal():", '123.45'.isdecimal())
# print("'-123'.isdecimal():", '-123'.isdecimal())
# print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
# print("'½'.isdecimal():", '½'.isdecimal())
# print("'²'.isdecimal():", '²'.isdecimal())
# print()

# # isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
# print("isdigit() 메서드 예시:")
# print("'12345'.isdigit():", '12345'.isdigit())
# print("'123.45'.isdigit():", '123.45'.isdigit())
# print("'-123'.isdigit():", '-123'.isdigit())
# print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
# print("'½'.isdigit():", '½'.isdigit())
# print("'²'.isdigit():", '²'.isdigit())
# print()

# # isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
# print("isnumeric() 메서드 예시:")
# print("'12345'.isnumeric():", '12345'.isnumeric())
# print("'123.45'.isnumeric():", '123.45'.isnumeric())
# print("'-123'.isnumeric():", '-123'.isnumeric())
# print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
# print("'½'.isnumeric():", '½'.isnumeric())
# print("'²'.isnumeric():", '²'.isnumeric())
