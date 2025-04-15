# -----------------------------------------------
#    EXERCÍCIO 115
# -----------------------------------------------

# PROJETO FINAL DO CURSO EM VÍDEO
# SIMULA A MANIPULAÇÃO DE UM SISTEMA SIMPLES COM BANDO DE DADOS EM ARQUIVO .TXT

from Ex115.sistema.arquivo import *
from Ex115.sistema.interface import *

arq = 'bancoDeDados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Acessar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        # Acessando as pessoas cadastradas
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrando novas pessoas
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa... até logo!')
        break
    else:
        print(f'{vermelho}ERRO!! Essa opção não existe.{limpo}')
