# 내장함수 이용 안하고 min,max,len,sum 만들기
numbers = [ 7,8,11,-45,96,2,15]

# len 만들기
def find_len(number):
    count = 0
    for num in numbers:
        count += 1
    return count
len = find_len(numbers) #7
print(len)

# min 만들기 
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print(min_value)

def find_min(i):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num 
    return min_value
result = find_min(numbers)
print(result)

# max 만들기
def find_max(i):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
result1 = find_max(numbers)
print(result1)


# sum 함수 만들기
def find_sum(i):
    sum_value = 0
    for num in numbers:
        sum_value += num
    return sum_value
result2 = find_sum(numbers)
print(result2)

print(sum(numbers))