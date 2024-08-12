import socket
import math

NICKNAME = 'E0001_1252952'
HOST = '127.0.0.1'
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
BALL_RADIUS = 2  # 공의 반지름

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

def find_best_hole(ball_x, ball_y):
    best_hole = None
    min_distance = float('inf')
    for hole in HOLES:
        distance_to_hole = math.sqrt((ball_x - hole[0])**2 + (ball_y - hole[1])**2) - BALL_RADIUS
        if distance_to_hole < min_distance:
            min_distance = distance_to_hole
            best_hole = hole
    return best_hole

def calculate_angle_and_power(white_x, white_y, target_x, target_y):
    # 각도 계산
    dx = target_x - white_x
    dy = target_y - white_y
    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)

    # 거리 계산
    distance = math.sqrt(dx**2 + dy**2)
    
    # 힘 조정 (거리 기반)
    power = min(100, max(0, 100 - distance * 0.5))
    
    return angle_degrees, power

while True:
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been corrupted, Resend Requested.")
        continue

    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    if order == 1:
        target_balls = balls[1:6:2]
    else:
        target_balls = balls[2:6:2]

    for targetBall in target_balls:
        targetBall_x, targetBall_y = targetBall

        # 가장 가까운 홀 찾기
        best_hole = find_best_hole(targetBall_x, targetBall_y)
        if best_hole is None:
            print("No suitable hole found for ball.")
            continue

        # 홀의 위치
        hole_x, hole_y = best_hole

        # 공을 홀로 보내기 위해 계산된 각도와 힘
        angle, power = calculate_angle_and_power(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
        
        # Debug 출력 추가
        print(f"Target Ball Position: ({targetBall_x}, {targetBall_y}), Hole Position: ({hole_x}, {hole_y})")
        print(f"Calculated Angle: {angle}, Calculated Power: {power}")

        merged_data = '%f/%f/' % (angle, power)
        sock.send(merged_data.encode('utf-8'))
        print('Data Sent: %s' % merged_data)

        # 흰 공의 새로운 위치 업데이트
        whiteBall_x = targetBall_x
        whiteBall_y = targetBall_y

    targetBall_x = balls[5][0]
    targetBall_y = balls[5][1]

    best_hole = find_best_hole(targetBall_x, targetBall_y)
    if best_hole is None:
        print("No suitable hole found for the 8-ball.")
        continue

    hole_x, hole_y = best_hole

    angle, power = calculate_angle_and_power(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)
    
    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
