from openai import OpenAI


# openai.api_key = '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'

cliente = OpenAI(api_key='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')

# Passo 1: Enviar a pergunta ao ChatGPT
response = cliente.chat.completions.create(
    model="gpt-4",  # ou "gpt-3.5-turbo" se preferir
    messages=[
        {"role": "user", "content": "Explique para o João o que é programação."}
    ]
)

resposta_texto = response.choices[0].message.content
print("Resposta:", resposta_texto)

# Passo 2: Gerar o áudio com a resposta
# audio_response = openai.audio.speech.create(
#     model="tts-1",  # Modelo de text-to-speech da OpenAI
#     voice="nova",   # Opções: "alloy", "echo", "fable", "onyx", "nova", "shimmer"
#     input=resposta_texto
# )

# # Salvar o áudio em um arquivo
# with open("resposta.mp3", "wb") as f:
#     f.write(audio_response.content)

# print("Áudio salvo como 'resposta.mp3'")
response = cliente.audio.speech.create(
    model='tts-1', # ou tts-1-hd
    voice='onyx',
    input='Explique a fórmula de baskara'
)

response.write_to_file('para_joao.mp3')