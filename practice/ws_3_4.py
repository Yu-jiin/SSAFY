# 다수의 유저를 등록하고자 한다.
# 주어진 유저 정보 리스트와 모든 유저를 등록하고,
# 반환된 유저 정보를 하나의 리스트에 담아 출력

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

increase_user()

def create_user(name,age,address):
    increase_user()
    user_info = {
        'name' : name,
        'age' : age,
        'address' : address
    }
    print(f'{name}님 환영합니다. ')
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# total = zip(name,age,address)
# print(list(total)) 내가 한 실수 

many_user = list(map(create_user,name,age,address))
# name, age, address의 하나씩 가져와서 create_user의 인자로 사용 

print(many_user)
