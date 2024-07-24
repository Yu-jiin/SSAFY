class Person:
    # 클래스 변수 count
    count = 0

    def __init__(self, name):
        # 인스턴스 변수 name
        self.name = name
        Person.count += 1 # 가수가 몇 명인지 확인하고 싶다면
        # 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있음. 

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2

##########################

class Circle:
    pi = 3.14 # 클래스 변수 변경은 클래스 변수만 가능 

    def __init__(self, r):
        self.r = r
        
c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14  c1.pi = c1가 본인에게서 pi 변수가 있는지 확인 
print(c2.pi) # 3.14          없으면, 본인을 만든 클래스에 찾으러 올라간다

# c1의 인스턴스 변수 pi 생성 
c1.pi = 100

c2.pi = 5 # 인스턴스 변수 변경 
print(Circle.pi) # 3.14
print(c1.pi) # 100
print(c2.pi) # 5


