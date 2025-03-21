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
            'content': 'Quem descobriu o Brasil?'
        }
    ],
    logprobs=True, # Mostra a probabilidade que os tokens foram colocados na frase
    top_logprobs=3 # Apresenta diferentes opções de tokens
)
print(response.choices[0].message.content)
with open('resposta.json', 'w', encoding='utf-8') as f:
    f.write(response.choices[0].to_json())