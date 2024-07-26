import requests
from pprint import pprint
#  도서 20권 중 리뷰 평점이 9점 이상인 도서 목록 추출 

def get_best_review_books():
    
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
    
    review = [review['customerReviewRank'] for review in response['item']]
    
    book_list = []
    for data in response['item']:
        for r in review:
            if r >= 9:
                book_list.append(data)
                
        return book_list      

    
    



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_best_review_books())


# 
# 만약에 review 가 9이상
# 
# 
# 
