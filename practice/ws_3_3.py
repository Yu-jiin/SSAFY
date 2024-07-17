def rental_book(name, book):
    decrease_book(book)
    customer_info = {
        'name' : name,
        'book' : book
    }
    return customer_info
    
number_of_book = 100

def decrease_book(book):
    global number_of_book
    recent_book = number_of_book - book
    return recent_book

result_book = decrease_book(3)
print(f'남은 책의 수 : {result_book}')
customer = rental_book('홍길동',3)
name = customer['name']
book = customer['book']
print(f'{name}님이 {book}권의 책을 대여하였습니다.')