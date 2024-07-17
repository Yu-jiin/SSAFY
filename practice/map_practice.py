## map 이해하기 

def square(x):
    return x ** 2

numbers = [1,2,3,4,5]
square_num = map(square,numbers)
print(list(square_num))


def add(x,y):
    return x + y

numbers_2 = [10,20,30,40,50]
add_num = map(add,numbers,numbers_2)
print(list(add_num))

## 람다 식

hap = lambda x, y: x + y

result = hap(3,5)
print(result)    