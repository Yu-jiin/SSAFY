pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(day,title,subject=None):
    global pro_num
    data = {
        'day' : day,
        'title' : title,
        'pro_num' : pro_num + 1
    }
    return data

result_1 = create_data('python',3)
result_2 = create_data()
result_3 = create_data()
