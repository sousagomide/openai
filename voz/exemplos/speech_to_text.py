from chatgpt.utils import client, arquivo

caminho_input = arquivo.formatar_caminho_output('mensagem_voz.mp3', nome_pasta='audio')

arquivo_audio = open(caminho_input, 'rb')

transcricao = client.audio.transcriptions.create(
    model='gpt-4o-transcribe',
    file=arquivo_audio,
    response_format='text',
    language='pt'
)

print(transcricao)