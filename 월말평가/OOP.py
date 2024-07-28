# 클래스 - 파이썬에서 타입을 표현하는 방법 
#         데이터와 기능을 함께 묶는 방법을 제공

#  객체 - 클래스에서 정의한 것을 토대로 메모리에 할당
#         속성과 행동으로 구성된 모든 것
 
# 가수 클래스에 객체는 아이유, BTS
# 클래스로 만든 객체를 인스턴스라고 부름 
# 아이유는 객체, 아이유는 가수의 인스턴스 

name = 'Jiin'
print(type(name)) # <class 'str'>
# 우리가 사용한 데이터 타입은 모두 클래스

class Person:
    count = 0

    def __init__(self,name):
        self.name = name
        Person.count += 1 # Person.count 명심하자 
    
    def singing(self):
        return f'{self.name}이 노래합니다.'

singer = Person('jiin')
print(singer.singing()) # jiin이 노래합니다.
person = Person('hyunjin')
print(Person.count) # 2


# 클래스 메서드는 @classmethod 데코레이터 사용 

# 정적 static 메서드 
# 클래스와 인스터스와 상관없이 독립적으로 동작하는 메서드
# @staticmethod 

# 클래스가 사용할 것 - 클래스, 스태틱메서드 
# 인스턴스가 사용할 것 - 인스턴스메서드 