
str = 'Hello, world!'

def reverse_string(str):
    return ''.join(reversed(str))
    
    
print(reverse_string(str))

# reversed는 파이썬 내장함수로 주어진 시퀀스 뒤집어 반환 

# 슬라이싱으로 뒤집기
def slicing(str):
    return str[::-1]
print(slicing(str))