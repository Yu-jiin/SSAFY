class gamma:
    order = 1
    
class gameData:
    balls = [[10,10], [40,50]]

class conn:
    @staticmethod
    def send(angle, power):
        print('성공입니다.')
    
# ===================위는 무시==============================================================


import math       # 필요 라이브러리

# ===================기본 정보==============================================================
gamma.order       # 1이면 내차례(선공)
Ball_r = 5.73 / 2 # 공의 반지름
W = 254           # 당구대 세로
H = 127           # 당구대 가로
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]] # 홀의 위치

# ===================함수 만들기============================================================

def shot():
    A = (a_1, a_2) = (gameData.balls[0][0], gameData.balls[0][1]) # 내 공의 위치
    B = (b_1, b_2) = (gameData.balls[1][0], gameData.balls[1][1]) # 내가 쳐야 할 공의 위치
    
    # 목적지 정하기(하드코딩) (방법 매우 많음)
    target = None
    if (a_1 != b_1) and (a_2 != b_2):
        if (a_1 < b_1) and (a_2 < b_2): target = HOLES[5]
        elif (a_1 < b_1) and (a_2 > b_2): target = HOLES[2]
        elif (a_1 > b_1) and (a_2 < b_2): target = HOLES[1]
        elif (a_1 > b_1) and (a_2 > b_2): target = HOLES[0]
                    
    elif a_1 == b_1 == 127:
        if a_2 < b_2: target = HOLES[4]
        else: target = HOLES[3]
    
    # 내가 공을 맞추고 싶은 위치 구하기
    dx, dy = target[0] - B[0], target[1] - B[1]
    dist = math.sqrt(dx**2 + dy**2)
    New_B = (b_1 - Ball_r * dx / dist, b_2 - Ball_r * dy / dist)
    
    # 각도 구하기 
    angle = math.atan2(New_B[1] - A[1], New_B[0] - A[0])

    # 힘은 어떻게 구할지 모르겠음. 직접 봐야 알듯.
    power = 100
    
    conn.send(angle, power) # 공을 치라는 명령.
    return

if gamma.order == 1: shot()