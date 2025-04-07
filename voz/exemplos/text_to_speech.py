from chatgpt.utils import client, arquivo

caminho_output = arquivo.formatar_caminho_output('fala_02.mp3', nome_pasta='audio')

response = client.audio.speech.create(
    model='tts-1', # ou tts-1-hd
    voice='onyx',
    input='Esse é um ótimo texto de teste, com várias palavras legais e interessantes'
)

response.write_to_file(caminho_output)