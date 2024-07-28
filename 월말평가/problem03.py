############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):
    if int(len(user_data.get('id')) == 0) | int(len(user_data.get('password')) == 0):
        valid = 'False'
    else:
        valid = 'True'
    return valid

# 데이터가 없다면 ? not 
def is_user_data_valid(user_data):
    if not user_data['id'] or not user_data['password']:
        valid = 'False'
    else:
        valid = 'True'
    return valid 

# def more_valid_test(user_data):
#     id = user_data['id']
#     password = user_data['password']
#     if not id or not password:
#         vaild = 'False'

#     if len(id) < 5 or len(password):
#         vaild = 'False'
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 
# print(more_valid_test(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
# print(more_valid_test(user_data2)) # True
#####################################################