import inspect
import os

def formatar_caminho_output(nome_arquivo='output.txt', nome_pasta='output', posicao_stack=1):
    # Encontra o arquivo onde a função foi chamada
    quem_chamou = inspect.stack()[posicao_stack].filename
    pasta_exemplos = os.path.dirname(quem_chamou)
    pasta_principal = os.path.dirname(pasta_exemplos)
    caminho_final = os.path.join(pasta_principal, nome_pasta, nome_arquivo)
    return caminho_final