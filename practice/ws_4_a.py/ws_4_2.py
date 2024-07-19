
import requests
from pprint import pprint as print

dummy_data = []

API_URL = 'https://jsonplaceholder.typicode.com/users/{}'

for i in range(1,11):
    response = requests.get(API_URL.format(i))
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])
    
print(dummy_data)

   

# # 정보 경로 요청
# API_URL = 'https://jsonplaceholder.typicode.com/users/'+a

# # API 요청 
# response = requests.get(API_URL)

# parsed_data = response.json()

# print(f'response : {response}')
# print('----------------------------------')
# print(f'parsed_data : {parsed_data}')
# print('-----------------------------------')