# def restructure_word(word,arr):
#     for item in word:
#         if item.isdecimal():
#             for _ in range(int(item)):
#                 if arr:
#                     arr.pop()
#         else:
#             while item in arr:
#                 arr.remove(item)
#     return arr

def restructure_word(word, arr):
    for i in word:
        if i.isdecimal():
            i = int(i) 
            for _ in range(i):
                arr.pop() 
        else :
            arr.remove(i)
            
    return arr
    

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

for origin in original_word:
    arr.append(origin)

print(arr)

result = restructure_word(word,arr)
print(result)

a = ''.join(result)
print(a)

# word 문자열의 각 문자를 순회 (for item in word:)
# item이 숫자인 경우 (if item.isdecimal():)
# 해당 숫자의 값만큼 arr 리스트의 마지막 요소를 제거 (for _ in range(int(item)):)
# 리스트가 비어 있지 않으면 (if arr:) arr.pop()
# item이 숫자가 아닌 경우
# arr 리스트에서 해당 문자가 존재할 때까지 모두 제거 (while item in arr:)


