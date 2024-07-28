############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def under_60(scores):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = []
    for score in scores:
        if score < 60:
            result.append(score)
        count = len(result)
    return count

def under_without_len(scores):
    pass
    c = []
    for score in scores:
        if score < 60:
            c.append(score)
    count = 0
    for i in c:
        count += 1
    return count

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(under_60([30, 60, 90, 70])) # 1
print(under_60([0, 10, 20, 30, 40, 50])) # 6
print(under_60([50, 70, 50, 45, 80, 80])) # 3
#####################################################
print(under_without_len([50, 70, 50, 45, 80, 80])) # 3