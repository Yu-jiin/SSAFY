pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject,day,title=None):
    global pro_num
    pro_num += 1
    data = {
        'subject' : subject,
        'day' : day,
        'title' : title,
        '문제 번호' : pro_num
    }
    return data

result1 = create_data('python',3)
result2 = create_data(subject='web', day=1, title='web 연습하기')
result3 = create_data(**global_data)


print(result1)
print(result2)
print(result3)
