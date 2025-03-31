from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

# Mensagem de sistema (system) serve para configuração.
# No código a seguir a mensagem é usada para que a ferramenta entenda a
# linguagem que está sendo usada.
# Mensagem de usuário (user) serve para interagir com o ChatGPT.
response = client.chat.completions.create(
    model='gpt-4o-mini',
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
    # max_tokens = 20 # Limita a quantidade de tokens
    # stop = ['mundo'] # O chat para ao encontrar um texto
    # n = 3# Define a quantidade de elementos dentro de Choices
)
# print(response)
# print(response.choices[0].message.content)
print(response.choices)