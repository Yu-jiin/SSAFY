import json
from pprint import pprint


def book_info(book, categories):
   
    categoryName = []
    categoryId = book.get('categoryId')
    # categoryId = [15118, 1528]
    
    for id in categoryId:
        print(f'@@@@@@@{id}')
           
    for id in categoryId:
        for category in categories:
            if category['id'] == id:
                categoryName.append(category.get('name'))

                
    new_info = {
        'id' : book.get('id'),
        'author' : book.get('author'),
        'title' : book.get('title'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover' : book.get('cover'),
        'categoryName' : categoryName   
    }
    return new_info


    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
