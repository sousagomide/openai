from chatgpt.utils import client

mensagem = 'Seguinte, se você der uma X-9, você vai ver comigo'

response = client.moderations.create(input = mensagem)
resultado = response.results[0]
print(resultado.categories.to_json())
print('Impróprio? ', resultado.flagged)