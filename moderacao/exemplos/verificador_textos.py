from chatgpt.utils import client
import json

while True:
    mensagem = input('Mensagem: ')
    if mensagem.lower() == 'sair':
        break
    response = client.moderations.create(input = mensagem)
    improprio = response.results[0].flagged
    print(f'O texto {mensagem} é impróprio? {improprio}')
    if improprio:
        categorias = json.loads(response.results[0].categories.to_json())
        print('O texto é impróprio por: ', end = '')
        for chave, valor in categorias.items():
            if valor:
                print(f'{chave} ', end = '')
        print()