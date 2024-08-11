import math

# 두 점(x, y) 사이의 거리를 계산하는 함수
def calcul_distance(x, y):
    # math.hypot 함수는 직각삼각형의 빗변 길이를 계산하는 함수로,
    # 이는 두 점 사이의 유클리드 거리를 구하는데 사용됩니다.
    # (y[0] - x[0]): x좌표 차이, (y[1] - x[1]): y좌표 차이
    return math.hypot(y[0] - x[0], y[1] - x[1])

# 두 점(x, y) 사이의 각도를 계산하는 함수
def calcul_angle(x, y):
    # math.atan2 함수는 두 점 사이의 y좌표 차이와 x좌표 차이를 이용하여
    # 각도를 라디안 단위로 반환합니다. (y[1] - x[1]): y좌표 차이, (y[0] - x[0]): x좌표 차이
    return math.atan2(y[1] - x[1], y[0] - x[0])

# 목표구에서 각 홀까지의 거리와 각도를 계산하는 함수
def calcul_distances_and_angles(objball, holes):
    # 목표구(objball)에서 각 홀(hole)까지의 거리를 계산
    # 거리 계산 결과는 리스트로 저장됩니다.
    distances_to_holes = [calcul_distance(objball, hole) for hole in holes]
    
    # 목표구에서 각 홀까지의 각도를 계산
    # 각도 계산 결과도 리스트로 저장됩니다.
    angle_to_holes = [calcul_angle(objball, hole) for hole in holes]
    
    # 두 리스트(거리, 각도)를 반환합니다.
    return distances_to_holes, angle_to_holes

# 가장 가까운 홀을 찾는 함수
def best_hole(distance_to_holes, angle_to_holes):
    # 가장 짧은 거리를 가진 홀의 인덱스를 찾습니다.
    best_hole_idx = distance_to_holes.index(min(distance_to_holes))
    # 가장 가까운 홀의 인덱스와 해당 홀까지의 각도를 반환합니다.
    return best_hole_idx, angle_to_holes[best_hole_idx]

# 내 공의 위치 (임의의 위치로 설정됨)
myball = [127, 63.5]

# 목표구의 위치 (임의의 위치로 설정됨)
objball = [150, 90]

# 홀의 위치 정의 (전체 테이블 상의 위치를 약간 이동시켜 조정함)
r = 5.73  # 공의 직경
const = 0.3  # 상수 값
k = r * const  # 공 크기와 상수를 곱하여 오프셋을 계산
holes = [
    [0 + k, 0 + k],       # 왼쪽 아래 홀
    [127, 0 + k / 2],     # 가운데 아래 홀
    [254 - k, 0 + k],     # 오른쪽 아래 홀
    [0 + k, 127 - k],     # 왼쪽 위 홀
    [127, 127 - k / 2],   # 가운데 위 홀
    [254 - k, 127 - k]    # 오른쪽 위 홀
]

# 목표구에서 각 홀까지의 거리와 각도를 계산
distance_to_holes, angle_to_holes = calcul_distances_and_angles(objball, holes)

# 가장 가까운 홀을 선택 (가장 짧은 거리를 가지는 홀)
best_hole_idx, angle_to_best_hole = best_hole(distance_to_holes, angle_to_holes)

# 선택한 홀과 목표구 사이의 각도를 계산 (가장 가까운 홀의 각도)
best_hole_angle = angle_to_holes[best_hole_idx]

# 공의 반지름을 고려하여 목표구의 접점까지의 각도를 계산
# offset은 목표구와 홀 사이의 각도에 추가될 각도입니다.
offset = math.atan2(r / 2, distance_to_holes[best_hole_idx])

# 목표구와 홀 사이의 각도에 오프셋을 추가하여 최종 목표 각도를 계산
target_angle = best_hole_angle + offset

# 내 공이 목표구를 맞출 접점의 위치를 계산
final_position = [
    objball[0] - math.cos(target_angle) * (r / 2),
    objball[1] - math.sin(target_angle) * (r / 2)
]

# 내 공과 목표구의 접점 사이의 각도를 계산
final_angle = math.degrees(calcul_angle(myball, final_position))

# 타격력 (임의로 설정된 값)
power = 100
