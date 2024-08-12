import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'E0001_1252952'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

def calculate_cushion_shot(white_x, white_y, target_x, target_y):
    # 쿠션을 고려한 최적 경로를 찾기 위한 함수입니다.
    
    best_shot = None
    best_hole = None
    best_angle = None
    best_distance = float('inf')

    # 쿠션 반사에 따른 각도를 고려하여 최적 경로를 계산합니다.
    for hole in HOLES:
        # 쿠션을 반사하여 홀에 도달하는 경우를 고려합니다.
        reflection_x = 2 * hole[0] - target_x
        reflection_y = 2 * hole[1] - target_y

        # 흰 공에서 반사된 공의 위치로의 각도를 계산합니다.
        angle_to_reflection = math.atan2(reflection_y - white_y, reflection_x - white_x)
        angle = math.degrees(angle_to_reflection)

        # 흰 공에서 쿠션 반사 위치까지의 거리 계산
        distance_to_reflection = math.sqrt((reflection_x - white_x)**2 + (reflection_y - white_y)**2)

        if distance_to_reflection < best_distance:
            best_distance = distance_to_reflection
            best_shot = (reflection_x, reflection_y)
            best_hole = hole
            best_angle = angle

    return best_shot, best_hole, best_angle, best_distance

while True:
    # 데이터를 수신합니다.
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # 수신된 게임 데이터를 분리하여 저장합니다.
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        # 데이터가 손상된 경우, 재전송을 요청합니다.
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been corrupted, Resend Requested.")
        continue

    # 플레이어 순서 신호 또는 연결 종료 신호를 확인합니다.
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # 공들의 위치를 출력합니다.
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    # 흰 공의 X, Y 좌표를 나타내는 변수입니다.
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # 선공인 경우 홀수 공, 후공인 경우 짝수 공을 타겟으로 설정합니다.
    if order == 1:  # 선공
        target_balls = balls[1:6:2]  # 1번, 3번, 5번 공
    else:  # 후공
        target_balls = balls[2:6:2]  # 2번, 4번 공

    for targetBall in target_balls:
        targetBall_x, targetBall_y = targetBall

        # 최적의 쿠션 반사 샷을 계산합니다.
        best_shot, best_hole, best_angle, best_distance = calculate_cushion_shot(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)

        # 흰 공에서 목표 공까지의 방향 각도
        angle_to_target = math.atan2(targetBall_y - whiteBall_y, targetBall_x - whiteBall_x)
        angle_to_target_deg = math.degrees(angle_to_target)

        # 최적의 홀로 직접 치는 샷과 쿠션 반사 샷을 비교합니다.
        direct_distance = math.sqrt((targetBall_x - whiteBall_x)**2 + (targetBall_y - whiteBall_y)**2)
        cushion_distance = best_distance

        if direct_distance < cushion_distance:
            # 직접 치는 샷이 더 나은 경우
            angle = angle_to_target_deg
            power = 100
        else:
            # 쿠션 반사 샷이 더 나은 경우
            angle = best_angle
            power = 100

        # 계산된 각도와 힘으로 공을 칩니다.
        merged_data = '%f/%f/' % (angle, power)
        sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

        # 흰 공의 새로운 위치를 업데이트합니다.
        whiteBall_x = targetBall_x
        whiteBall_y = targetBall_y

    # 마지막으로 8번 공을 처리합니다.
    targetBall_x = balls[5][0]
    targetBall_y = balls[5][1]
    best_shot, best_hole, best_angle, best_distance = calculate_cushion_shot(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
    radian = math.atan2(best_hole[1] - whiteBall_y, best_hole[0] - whiteBall_x)
    angle = math.degrees(radian)
    distance = math.sqrt((best_hole[0] - whiteBall_x)**2 + (best_hole[1] - whiteBall_y)**2)
    power = 100  # 8번 공은 최대 힘으로 칩니다.

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
