from chatgpt.utils import client, arquivo

caminho_output = arquivo.formatar_caminho_output('fala_params_02.mp3', nome_pasta='audio')

response = client.audio.speech.create(
    model='tts-1', # ou tts-1-hd
    voice='onyx',
    input='Olá, bom dia. Na aula de hoje veremos um pouco mais sobre orientação a objetos com Javascript.',
    speed=1,
    response_format='mp3'
)

response.write_to_file(caminho_output)