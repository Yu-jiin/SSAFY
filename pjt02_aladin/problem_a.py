import requests
from pprint import pprint
#  저자 파울로 코엘료 의 도서검색, 최대 20개의 도서 제목 추출
#  요구사항 만족하는 함수 작성 

def get_author_books():
    
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
    titles = [book['title'] for book in response['item']]
    
    return titles


    # books = data.get('item',[])
    # titles = [book.get('title', '제목 없음') for book in books]
    # return titles
    


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_books())
