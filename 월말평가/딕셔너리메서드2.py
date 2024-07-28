data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

for dic in data:
    # print(dic.keys())
    for key in key_list:
        value = dic.setdefault(key,'unknown')
        print(f'{key} 은/는 {value}입니다')





for dic in data:
    for key in key_list:
        value = dic.setdefault(key,'unknown')