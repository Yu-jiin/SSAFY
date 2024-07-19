import requests


url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()
# json() 딕서녀리 결과를 반환해줌 
print(response)
