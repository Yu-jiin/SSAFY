class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
# print(MyClass.instance_method(instance)) # 인스턴스는 쓰지마 ㅠ 되긴 하지만 
print(MyClass.class_method())
print(MyClass.static_method())

# 인스턴스가 할 수 있는 것
print(MyClass.instance_method(instance))
# 나머지가 다 되지만, 그래도 인스턴스 매서드만 사용하자 