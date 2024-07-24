class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 함수의 매개변수 이름
        # 둘다 달라도 상관은 없다만 굳이 ?
        self.name = name
        print('인스턴스가 생성되었습니다. ')
    
    def greeting(self):
        print(f'안녕하세오 {self.name}입니다.') # 그냥 name 은 안됨 
        # instance 변수의 name을 출력 

person1 = Person('지인')
person1.greeting()
# Person.greeting(person1) 단축형 호출 풀어낸 방법 