import requests
from pprint import pprint


def get_bestseller_books():

    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbjiin40831127001',
        'Query' : '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()
     
    point = [point['salesPoint'] for point in response['item']]
    # print(point)
    
    tmp = point.copy()
    tmp.sort()
    top_point = tmp[-5:]
    # print(top_point)
    
    
    
    for data in response['item']:
        for point in top_point:
            if data['salesPoint'] == point:
                title = data['title']
                print(f'제목 : {title}, 판매지수 : {point}')
        



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_bestseller_books())
