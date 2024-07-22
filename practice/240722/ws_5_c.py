def restructure_word(word, arr):
    for item in word:
        if item.isdecimal():
            for _ in range(int(item)):
                if arr:
                    arr.pop()
        else: 
            while item in arr:
                arr.remove(item)    
    return arr  


original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
    
for work in original_word:
    arr.extend(work)
print(arr)


result = restructure_word(word, arr)
print(result)

text = ''.join(result)
print(text)