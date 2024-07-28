############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    id = user_data['id']
    id = id[::-1]
    valid_id = id[0]
    print(valid_id)
    check = list(range(0,10))
    print(check)
    try:
        int(valid_id)
    except:
        return False
    if int(valid_id) in check:
        return True
    else:
        return False

    #  우선 문자열을 정수로 변환, 변환이 안되면 예외처리
    #  그런 다음 확인 
    # 정수로 변환안하면 문자열이라 비교 불가  

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################