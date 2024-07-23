# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
# 1. 변수이름 개떡같이 쓰지말기 !!!! 
def count_blood_types(blood_types):
    blood = {}
    
    for b in blood_types:
        if b not in blood:
            blood[b] = 1
        else:
            blood[b] += 1
    return blood
    

print(count_blood_types(blood_types)) 
# {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


#  if 문을 get 으로 
# 2. get() 메서드를 사용한 방법
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']

def count_blood_types3(blood_types):
    new = {}
    for k in blood_types:
        new[k] = new.get(k,0)+1  # get이 if문의 역할 수행하는 느낌 
        # new[k] = 키 할당     
    return new
        
print(count_blood_types3(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
