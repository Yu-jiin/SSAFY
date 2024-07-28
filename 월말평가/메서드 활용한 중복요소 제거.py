lists = [1,1,2,3,45,6,5,8,4,5,6,1]


result = []
def remove_duplicates(lists):
    for l in lists:
        if l not in result:
            result.append(l)
    return result

answer = remove_duplicates(lists)
print(answer)

# 빈 튜플 만들기 new_tuple = ()
def sort_tuple(tuple):
    new_tuple = ()
    # 튜플 정렬하려면 list로 만들어야하잖아 지인아
    a = list(tuple)
    a.sort()
    return a



result = sort_tuple((5, 2, 8, 1, 3))
print(result)
