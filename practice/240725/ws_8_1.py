# 아래 클래스를 수정하시오.
class Animal:
    num_of_animals = 0
    def __init__(self):
        pass
        


class Dog(Animal):
    def __init__(self):
        super().__init__()
        Animal.num_of_animals += 1


class Cat(Animal):
    def __init__(self):
        super().__init__()
        Animal.num_of_animals += 1


class Pet(Dog,Cat):
    
    def __init__(self):
        super().__init__()
    
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animals}마리 입니다.'


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
