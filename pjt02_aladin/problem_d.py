import requests
from pprint import pprint


def get_author_other_books(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbjiin40831127001',
        'Query' : title,
        'QueryType': 'Title',
        'MaxResults': 1,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }
    
    response = requests.get(URL, params=params).json()
    try :
        author = response['item'][0]['author'].index(' (지은이)')
        main_author = response['item'][0]['author'][:author]
        title1 = [book['title'] for book in response['item']]
        
        
        params1 = {
            'ttbkey': 'ttbjiin40831127001',
            'Query' : main_author,
            'QueryType': 'Author',
            'MaxResults': 6,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
        }
        
        response1 = requests.get(URL, params=params1).json()
        title2 = [book['title'] for book in response1['item']]
        print(f'빼야할 책 : {title}')
        print(f'뽑아온 책 : {title2}')
        
        result_title = []
        for diff in title2:
            if title1 != diff: # is not 말고 != 같지 않을때를 써야해
                            # 문자열은 헷갈리잖아
                result_title.append(diff)
                if len(result_title) == 5:
                    break
        return result_title
    except IndexError:
        return None   
        
    
    
     

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_other_books('베니스의 상인'), width=120)
    pprint(get_author_other_books('죄와 벌'), width=120)
    pprint(get_author_other_books('*'), width=120)

