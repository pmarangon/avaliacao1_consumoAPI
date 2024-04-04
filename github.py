import requests
print('Github Users')
user_name = input('Qual é o nome do usuário? ')
print(user_name)
url = f'https://api.github.com/users/{user_name}'
response = requests.get(url)
data = response.json()
print( f' Nome completo: {data["name"]}')