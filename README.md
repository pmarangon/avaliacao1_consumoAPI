# avaliacao1_consumoAPI
Avaliação Pratica Disciplina Desenvolvimento Web III
#  Consumo da API GitHub Users
Foi utilizada a Api Github Users: https://api.github.com/users que retorna dados sobre os usuários cadastrados na plataforma quando passamos o nome de usuário


 A biblioteca requests foi utilizada para fazer requisições Http em python
  Import requests

  user_name = input('Qual é o nome do usuário? ') 
  No inicio do  codigo é solicitado ao usuario que passe o nome do usuário que deseja consultar, o nome é transformado em variável (user_name) para ser passada na url
  url = f'https://api.github.com/users/{user_name}'
  A variável url é criada utilizando f-strings para formatar a URL da API GitHub Users com o nome do usuário digitado.
  response = requests.get(url)

  A biblioteca requests é utilizada para realizar uma requisição GET à URL da API armazenada na variável url. A resposta da API é armazenada na variável response.
  data = response.json()
  O método json() da variável response é utilizado para extrair os dados da resposta em formato JSON e armazená-los na variável data.

  print( f' Nome completo: {data["name"]}')
  O valor da chave "name" do dicionário data é acessado e exibido na tela, junto com a mensagem "Nome completo:".

 #Resultados:

O código foi escrito com sucesso e é capaz de:

Solicitar ao usuário o nome do usuário que deseja consultar.
Compor a URL da API GitHub Users com o nome do usuário digitado.
Realizar uma requisição GET à API e armazenar a resposta.
Extrair os dados da resposta em formato JSON.
Exibir o nome completo do usuário na tela.
#Limitações:

O código exibe apenas o nome completo do usuário. Outras informações do dicionário data, como biografia, repositórios e seguidores, não são exibidas.

#Melhorias:

Exibir outras informações do dicionário data, como biografia, repositórios e seguidores.
Tratar erros de requisição à API.
Implementar funcionalidades adicionais, como a busca por repositórios e seguidores do usuário.
