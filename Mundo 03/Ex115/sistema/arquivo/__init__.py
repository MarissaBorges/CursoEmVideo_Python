from Ex115.sistema.interface import *

def definir_caminho(nome):
    import os
    # Obtém o caminho absoluto da pasta onde este arquivo (__init__.py) está localizado
    pasta_base = os.path.dirname(os.path.abspath(__file__))
    # Junta o caminho da pasta 'arquivo' com o nome do arquivo
    caminho = os.path.join(pasta_base, nome)
    return caminho

def arquivoExiste(nome):
    caminho = definir_caminho(nome)
    try:
        a = open(caminho, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    caminho = definir_caminho(nome)
    try:
        a = open(caminho, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo!!')
    else:
        print(f'Arquivo {nome} criado com sucesso!!')

def lerArquivo(nome):
    caminho = definir_caminho(nome)
    try:
        a = open(caminho, 'rt')
    except:
        print('Erro ao abrir o arquivo!!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
        print()
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    caminho = definir_caminho(arq)
    try:
        a = open(caminho, 'at')
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um erro ao cadastrar uma nova pessoa')
        else:
            print(f'Novo registro de {nome} foi adicionado')
    finally:
        a.close()

