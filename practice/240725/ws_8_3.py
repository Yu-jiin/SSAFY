# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self, m):
        super().__init__()
        self.m = m

    def meow(self):
        print(f'{self.m}!')
    
cat1 = Cat("야옹")
cat1.meow()
