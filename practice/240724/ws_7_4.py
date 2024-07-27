# 아래 클래스를 수정하시오.
class Shape:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_info(self):
        print(f'Width : {self.x}')
        print(f'Height : {self.y}')
        area = self.x * self.y
        print(f'Area : {area}')
        perimeter = (self.x + self.y)
        print(f'Perimeter : {perimeter}')
        

shape1 = Shape(5, 3)
shape1.print_info()
