data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}

# item 말고 items 다... 
print(data.items())
print(data.values())
print(data.get('without','unknown'))

data.update(plus_data)
print(data)