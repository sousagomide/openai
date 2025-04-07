from utils import client
import json
import random

historico = [
        {
            'role':'system',
            'content': 'Você é um assistente útil'
        },
        {
            'role': 'user',
            'content': 'Qual é a avaliação do filme Rock 3?'
        }
]

def enviar():
    funcao = {
        'name': 'pegar_nota',
        'description': 'Obtém a nota de um filme',
        'parameters': {
            'type': 'object',
            'properties': {
                'titulo': {
                    'type': 'string',
                    'description': 'Título do filme'
                }
            }
        }
    }
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=historico,
        functions = [funcao]
    )
    return response.choices[0].message

def pegar_nota(titulo):
    resultado = len(titulo) * random.random()
    nota = min(resultado%11,10)
    return round(nota, 2)


resultado = enviar()

# Execução da função
fn_call = resultado.function_call
params = json.loads(fn_call.arguments)
nome_funcao = eval(fn_call.name)
resultado_exec = nome_funcao(**params)

# Enviando para o modelo
historico.append({
    'role': 'function', 'name': fn_call.name, 'content': f'{resultado_exec}'
})
resultado = enviar()
print(resultado.content)