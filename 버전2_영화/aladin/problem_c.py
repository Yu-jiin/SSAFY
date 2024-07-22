import json
from pprint import pprint


def books_info(books, categories):
    
    book_list = []
    j = (len(books))
    i = 1
    while i < j:
        categoryName = []
        categoryId = books[i]['categoryId']
        for id in categoryId:
            for category in categories:
                if category['id'] == id:
                    categoryName.append(category.get('name'))
        new_info = {
            'id' : books[i]['id'],
            'title' : books[i]['title'],
            'author' : books[i]['author'],
            'priceSales' : books[i]['priceSales'],
            'description' : books[i]['description'],
            'cover' : books[i]['cover'],
            'categoryName' : categoryName   
        }
        book_list.append(new_info)
        i += 1
        
        
    return book_list
        
   
    



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))


