food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

for food in food_list:
    name = food['이름']
    types = food['종류']
    if name == '토마토':
        food['종류'] = '과일'
    if name == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{name} 은/는 {types} (이)다.')
print(food_list)

################## while 문으로 변경
# 이거 지금 3번 반복해야하잖아
food_list2 = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

a = 0
while a < 3:
    if food_list2[a]['이름'] == '토마토':
        food_list2[a]['종류'] = '과일'
    if food_list2[a]['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f"{food_list2[a]['이름']} 은/는 {food_list2[a]['종류']} (이)다")
    a += 1
print(food_list2)