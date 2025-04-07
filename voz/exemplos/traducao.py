from chatgpt.utils import client, arquivo

# Arquivos suportados: mp3, mp4, mpeg, mpga, m4a, ogg, wav, webm
caminho_input = arquivo.formatar_caminho_output('mensagem_voz.mp3', nome_pasta='audio')

arquivo_audio = open(caminho_input, 'rb')

traducao = client.audio.translations.create(
    model='whisper-1',
    file=arquivo_audio,
    response_format='text' # json, text, srt, vtt, verbose_json
)

print(traducao)