from chatgpt.utils import client, arquivo

mensagem = 'Vou na tua casa te bater novamente'

response_stable = client.moderations.create(input = mensagem, model = 'text-moderation-stable')
caminho_stable = arquivo.formatar_caminho_output('stable.json')
with open(caminho_stable, 'w', encoding='utf-8') as arq:
    arq.write(response_stable.to_json())

response_latest = client.moderations.create(input = mensagem, model = 'text-moderation-latest')
caminho_latest = arquivo.formatar_caminho_output('latest.json')
with open(caminho_latest, 'w', encoding='utf-8') as arq:
    arq.write(response_latest.to_json())
