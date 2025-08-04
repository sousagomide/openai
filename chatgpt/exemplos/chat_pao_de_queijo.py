from ..utils import client
import sys

class Chat:
    def __init__(self):
        self.client = client
        self.historico = [
            {
                'role': 'system',
                'content': 'Você é um assistente útil apaixonado por pão de queijo, e em todas as suas interações você se preocupa em passar o seu amor por pão de queijo, muitas vezes falando apenas sobre pão de queijo e esquecendo a necessidade inicial do usuário.'
            }
        ]

    def print_assistente(self, texto):
        print('\033[94m' + texto + '\033[0m', end='')

    def input_usuario(self, texto):
        return input('\033[31m' + texto)

    def obter_resposta(self, texto):
        self.historico.append({'role': 'user', 'content': texto})
        stream = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages= self.historico,
            temperature=1.3,
            stream=True
        )
        texto_final = ''
        self.print_assistente('Assistente: ')
        for chunk in stream:
            conteudo = chunk.choices[0].delta.content
            if conteudo is not None:
                texto_final += conteudo
                self.print_assistente(conteudo)
                sys.stdout.flush()
        print()
        self.historico.append({'role': 'assistant', 'content': texto_final})

    def iniciar(self):
        print("Iniciando chat... Digite 'sair' para sair")
        while True:
            mensagem = self.input_usuario('Você: ')
            if mensagem.lower() == 'sair':
                break
            self.obter_resposta(mensagem)

Chat().iniciar()

    