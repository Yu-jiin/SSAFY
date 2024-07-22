import json


def best_book(books):
    
    # 여기에 코드를 작성합니다.
        answer1 = []
        for i in range(len(books)):
            bookids = books[i]['id']
            books_js = open(f'data/books/{bookids}.json', encoding='utf-8')
            books_list = json.load(books_js)
            answer1.append(float(books_list['customerReviewRank']))
            answer2=max(answer1)
            print(answer1)
            print(answer2)
        if float(books_list[i]['customerReviewRank']) == answer2:
            print(books_list['title'])

   
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
