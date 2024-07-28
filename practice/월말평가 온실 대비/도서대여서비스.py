number_of_book = 100



def rental_book(name, book):
    decrease_book(book)
    person = {
        'name':name,
        'book':book
    }
    return person


def decrease_book(book):
    book = number_of_book-book
    return book


result_book = decrease_book(3)
print(f'남은 책의 수 : {result_book}')
person = rental_book('홍길동',3)
name = person['name']
book = person['book']
print(f'{name}님이 {book}권의 책을 대여하였습니다.')