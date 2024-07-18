
import requests
from pprint import pprint as print

a = 0
while a < 11:
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+a
    response = requests.get(API_URL)
    parsed_data = response.json()
    print(parsed_data[a]['name'])
    a += 1

# # 정보 경로 요청
# API_URL = 'https://jsonplaceholder.typicode.com/users/'+a

# # API 요청 
# response = requests.get(API_URL)

# parsed_data = response.json()

# print(f'response : {response}')
# print('----------------------------------')
# print(f'parsed_data : {parsed_data}')
# print('-----------------------------------')


# a = 0
# while a < 11:
#     print(parsed_data[a]['name'])
#     a += 1