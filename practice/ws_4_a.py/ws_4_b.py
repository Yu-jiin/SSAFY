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

# 아래에 코드를 작성하시오.
for food in food_list:
    
   if(food['이름'] == '잡채'):
       print(f"{food['이름']} 은/는 {food['종류']} (이)다")
   if(food['이름'] == '토마토'):
       food['종류'] = '과일'
       print(f"{food['이름']} 은/는 {food['종류']} (이)다")
   elif(food['이름'] == '자장면'):
       print(f"{food['이름']}엔 고춧가루지 ")
       print(f"{food['이름']} 은/는 {food['종류']} (이)다")
   else:
       pass
print(food_list)

#### for 문 반복문으로 변경하기 
print('-----------------------')
a = 0
while a < 3:
    if(food_list[a]['이름']) == '토마토':
        food_list[a]['종류'] = '과일'
    if(food_list[a]['이름']) == '자장면':
        print(f"{food_list[a]['이름']}엔 고춧가루지")
    print(f"{food_list[a]['이름']} 은/는 {food_list[a]['종류']} (이)다")
    a += 1
    



    
    
    
print('---------------------')  
floors = [1,2,3,4,5]
rooms = [1,2,3,4]

for floor in floors:
    print(f'{floor}층')
    for room in rooms:
        print(floor, room)

for floor in range(0,2):
    print(f'{floor}층')
    for each in range(0,4):
        print(f'{each}호')

elements = [['A','B'],['c', 'd']]

# A c d B c d 
for element in elements[0]:
    print(element)
    for ele in elements[1]:
        print(ele)
        
# A c d B c d 
for i in range(0,2):
    print(elements[0][i])
    for j in range(0,2):
        print(elements[1][j])