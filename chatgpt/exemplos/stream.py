from openai import OpenAI
from dotenv import load_dotenv
import sys
import time


load_dotenv()
client = OpenAI()

# Mensagem de sistema (system) serve para configuração.
# No código a seguir a mensagem é usada para que a ferramenta entenda a
# linguagem que está sendo usada.
# Mensagem de usuário (user) serve para interagir com o ChatGPT.
stream = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role':'system',
            'content': 'Você é um assistente útil'
        },
        {
            'role': 'user',
            'content': 'Cite as 5 linguagens de programação mais usadas no mundo.'
        }
    ],
    stream=True
)

for chunck in stream:
    conteudo = chunck.choices[0].delta.content
    if conteudo is not None:
        print(conteudo, end='')
        sys.stdout.flush()
        time.sleep(0.2)