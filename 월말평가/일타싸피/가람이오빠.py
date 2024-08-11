import math

# 두 점 사이의 거리 계산 함수
def calcul_distance(x, y):
    return math.hypot(y[0] - x[0], y[1] - x[1])

# 두 점 사이의 각도 계산 함수
def calcul_angle(x, y):
    return math.atan2(y[1] - x[1], y[0] - x[0])

# 목표구에서 각 홀까지의 거리와 각도를 계산하는 함수
def calcul_distances_and_angles(objball, holes):
    # 목표구(objball)에서 각 홀(hole)까지의 거리 계산
    distances_to_holes = [calcul_distance(objball, hole) for hole in holes]
    # 목표구에서 각 홀까지의 각도 계산
    angle_to_holes = [calcul_angle(objball, hole) for hole in holes]
    return distances_to_holes, angle_to_holes

# 가장 가까운 홀을 찾는 함수
def best_hole(distance_to_holes, angle_to_holes):
    # 가장 짧은 거리의 인덱스
    best_hole_idx = distance_to_holes.index(min(distance_to_holes))
    # 가장 가까운 홀의 인덱스와 각도를 반환
    return best_hole_idx, angle_to_holes[best_hole_idx]

# 내 공의 위치(랜덤)
myball = [127, 63.5]
# 목표구의 위치(랜덤)
objball = [150, 90]
# 홀의 위치
# holes = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
# 홀 잡아당기기
r = 5.73
const = 0.3
k = r * const
holes = [[0 + k, 0 + k], [127, 0 + k / 2], [254 - k, 0 + k], [0 + k, 127 - k], [127, 127 - k / 2], [254 - k, 127 - k]]
# 공의 직경

# 목표구에서 각 홀까지의 거리와 각도를 계산
distance_to_holes, angle_to_holes = calcul_distances_and_angles(objball, holes)

# 가장 가까운 홀을 선택
best_hole_idx, angle_to_best_hole = best_hole(distance_to_holes, angle_to_holes)

# 선택한 홀과 목표구 사이의 각도를 계산
best_hole_angle = angle_to_holes[best_hole_idx]

# 공의 반지름을 고려하여 목표구의 접점까지의 각도를 계산
offset = math.atan2(r / 2, distance_to_holes[best_hole_idx])
# 목표구와 홀 사이의 각도에 오프셋을 추가하여 최종 목표 각도를 계산
target_angle = best_hole_angle + offset


# 내 공을 맞출 접점의 위치
final_position = [
    objball[0] - math.cos(target_angle) * (r / 2),
    objball[1] - math.sin(target_angle) * (r / 2)
]
# 내 공과 목표구의 접점 사이의 각도를 계산
final_angle = math.degrees(calcul_angle(myball, final_position))

power = 100
