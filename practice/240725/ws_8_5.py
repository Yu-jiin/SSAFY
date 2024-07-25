# 아래 클래스를 수정하시오.

class Dog:
    def __init__(self):
        pass
    def bark(self):
        print('멍멍 !')
        
class Cat:
    def __init__(self):
        pass
    def meow(self):
        print('야옹 !')
     
class Pet(Dog,Cat):

    def __init__(self,m):
        super().__init__()
        self.m = m
    
    def play(self):
        print('애완동물과 놀기')
        
    def make_sound(self):
        print(self.m)

sound = Pet('')

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
