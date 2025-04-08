# -----------------------------------------------
#    EXERCÍCIO 101
# -----------------------------------------------
from datetime import date

def voto(ano):
    hoje = date.today().year
    idade = hoje - ano
    if idade >= 18 and idade < 65:
        eleicao = 'VOTO OBRIGATÓRIO'
    elif idade < 16:
        eleicao = 'NÃO VOTA'
    else:
        eleicao = 'VOTO OPCIONAL'
    return f'Com {idade} anos: {eleicao}'

print('-'*30)
ano = int(input('Em que ano você nasceu? '))

print(voto(ano))