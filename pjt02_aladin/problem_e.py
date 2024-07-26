import requests
from pprint import pprint


def get_users_books(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbjiin40831127001',
        'Query' : title,
        'QueryType': 'Title',
        'MaxResults': 1,
        'start': 1,
        'SearchTarget': 'Used',
        'output': 'js',
        'Version': '20131101',
    }
    
    response = requests.get(URL, params=params).json()
    isbn = [book['isbn'] for book in response['item']]
    
    
    URL1 = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx'

    params1 = {
        'TTBKey': 'ttbjiin40831127001',
        'ItemId' : isbn,
        # 'ItemIdType': 'itemId',
        'output': 'js',
        'Version': '20131101',
        'OptResult' : 'usedList'
    } 
    response1 = requests.get(URL1, params=params1).json()
    sub_info = response1['item'][0]['subInfo']
    for sub in sub_info['item']:
        print(sub)
    
    
    return 


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
    pprint(get_users_books('로미오와 줄리엣'))
    # pprint(get_users_books('*'))
