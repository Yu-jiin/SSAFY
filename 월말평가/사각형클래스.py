class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return self.x * self.y

    def calculate_perimeter(self):
        return (self.x + self.y)*2

shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)

pereimeter = shape1.calculate_perimeter()
print(pereimeter)


class StringRepeater:
    def __init__(self,string,count):
        self.string = string
        self.count = count

    def repeat_string(self):
        for _ in range(self.count):
            print(self.string)

answer = StringRepeater('Hello',3)
a = answer.repeat_string()

