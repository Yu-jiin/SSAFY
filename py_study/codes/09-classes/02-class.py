# 클래스 정의 
# 클래스는 속성과 메서드로 이루어져있다. 
class Person:
    blood_color = 'red'
    
    # 초기값이 필요하다는 함수 라는 의미 
    def __init__(self,name):
        self.name = name
        
    def singing(self):
        return f'{self.name}이 노래합니다 '

# 인스턴스 생성
singer1 = Person('iu')
# 함수와 구분하기 위해 클래스는 Pascal Case 로 작성 

# (인스턴스) 메서드 호출
print(singer1.singing())

# 속성(변수) 접근
print(singer1.blood_color)

print(singer1.name)


# main.py


# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,width,height) :
        self.width = width
        self.height = height


shape1 = Shape(5, 3)
print(shape1.width, shape1.height)