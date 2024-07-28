number_of_people = 0
print(f'현재 가입된 유저 수 : {number_of_people}')

def increase_user():
    global number_of_people
    number_of_people += 1
    

def create_user(name,age,address):
    increase_user()
    user_info = {
        'name':name,
        'age':age,
        'address':address
    }
    print(f'{name} 님 환영합니다 ! ')
    return user_info

result = create_user(name='홍길동', age=30, address='서울')
print(result)
print(f'현재 가입 된 유저 수 : {number_of_people}')

