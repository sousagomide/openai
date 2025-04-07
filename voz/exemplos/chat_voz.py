from chatgpt.utils import client, arquivo
from pydub import AudioSegment
from pydub.playback import play
import sounddevice as sd
import soundfile as sf
import time
import re
import pygame


class Chat:

    def __init__(self):
        self.usuario_temp_file = arquivo.formatar_caminho_output('usuario_temp.mp3', nome_pasta='audio')
        self.assistente_temp_file = arquivo.formatar_caminho_output('assistente_temp.mp3', nome_pasta='audio')
        self.client = client
        self.historico = [
            {
                'role': 'system',
                'content': 'Você é um assistente útil'
            }
        ]

    def aviso(self, texto):
        print('\033[34m' + texto + '\033[0m')

    def gravar(self, duracao = 5):
        sample_rate = 44100
        total_samples = int(sample_rate * duracao)
        gravacao = sd.rec(total_samples, samplerate=sample_rate, channels=1)
        self.aviso('Seu audio acabe em...')
        for i in range(duracao, 0, -1):
            self.aviso(f'{i}...')
            time.sleep(1)
        sd.wait()
        sf.write(self.usuario_temp_file, gravacao, sample_rate)

    def transcrever(self):
        arquivo_audio = open(self.usuario_temp_file, 'rb')
        transcricao = self.client.audio.transcriptions.create(
            model='whisper-1',
            file = arquivo_audio,
            response_format='text'
        )
        return transcricao
    
    def buscar_resposta(self, texto):
        self.historico.append(
            {
                'role': 'user',
                'content': texto
            }
        )
        response = self.client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = self.historico
        )
        texto_resposta = response.choices[0].message.content
        self.historico.append(
            {
                'role': 'assistant',
                'content': texto_resposta
            }
        )
        return texto_resposta
    
    def falar_resposta(self, texto):
        response = self.client.audio.speech.create(
            model = 'tts-1',
            voice = 'onyx',
            input = texto
        )
        response.write_to_file(self.assistente_temp_file)
        
        pygame.mixer.init()
        pygame.mixer.music.load(self.assistente_temp_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    def iniciar(self):
        self.aviso('Iniciando...')
        while True:
            self.aviso('Prepare-se para falar. Aperte [ENTER] quando estiver pronto')
            input()
            self.gravar()
            self.aviso('Deseja enviar a mensagem? S/n')
            isSend = input()
            if(isSend.lower() == 'n'):
                continue
            self.aviso('Audio em processamento...')
            texto = self.transcrever()
            if re.search(r'sair.?', texto, re.IGNORECASE):
                break
            self.aviso('Processando resposta...')
            response = self.buscar_resposta(texto)
            self.falar_resposta(response)

Chat().iniciar()


