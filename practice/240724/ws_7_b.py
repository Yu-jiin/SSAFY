# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0
    
    def __init__(self,name):
        self.name = name
        Myth.type_of_myth += 1
        
    @staticmethod
    def description(explain):
        return explain
    

myth1 = Myth('daugun')
myth2 = Myth('greek & rome')


print(myth1.name)
print(myth2.name)
print(Myth.type_of_myth)
explain = '신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.'
result = Myth.description(explain)
print(result)  