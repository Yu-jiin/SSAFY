# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

# Dad 가 먼저 있으니 아빠 쪽에서 먼저 찾고, 없으면 Mom으로 
class FirstChild(Dad,Mom):  # 위의 모든 코드가 존재함 상속 받았기 때문 
    
    def __init__(self, name, age, address): # 추가 정보 받기 
        super().__init__(name, age, address)
        # super = 단순히 상위 클래스를 가져오는 것이 아닌 MRO에 따라 들고옴
        # 상위 클래스를 자연스럽게 들고오기 가능 
        
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # Dad 가 앞으니 XY
