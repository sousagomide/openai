from utils import client
from utils.arquivo import formatar_caminho_output

mensagem = input('O que você quer dizer no seu e-mail: ')

resposta = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{
        'role': 'system',
        'content': 'Você um especialista em criação de e-mails corporativos e se preocupa em escrever e-mails de uma forma agradável e educada, passando uma mensagem de forma clara e respeitosa. Seu objetivo é transformar uma mensagem do usuário em um e-mail que este usuário possa enviar para um dos seus colegas de trabalho. Retorne apenas o texto do e-mail e o assunto'
    },
    {
        'role': 'user',
        'content': mensagem
    }],
    n = 3
)

nome_arquivo_output = formatar_caminho_output('email.txt')
with open(nome_arquivo_output, 'w', encoding='utf-8') as arquivo:
    for opcao in resposta.choices:
        arquivo.write(f"{'='*50}\n")
        arquivo.write(opcao.message.content)
        arquivo.write(f"\n{'='*50}\n")
print(f'Os e-mails foram gerados. Cheque {nome_arquivo_output}')