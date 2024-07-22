import json
from pprint import pprint

#  id, name, author, priceSales, description, cover, categoryId
def book_info(book):
    new_info = {
        'id' : book.get('id'),
        'author' : book.get('author'),
        'title' : book.get('title'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover' : book.get('cover'),
        'categoryId' : book.get('categoryId')
    }
    return new_info
    # 여기에 코드를 작성합니다.

    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
