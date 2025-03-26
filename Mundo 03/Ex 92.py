#------------------------------------------------
#    EXERCÍCIO 92
# -----------------------------------------------
# 35 anos de contribuição
from datetime import date

dados = {}
dados['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Informe o ano de nascimento: '))
dados['Idade'] = date.today().year - ano_nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = int(input('Salário: R$ '))
    resto_apose = 35 - (date.today().year - dados['Contratação'])
    dados['Aposentadoria'] = dados['Idade'] + resto_apose

print('-=' * 20)
for k, v in dados.items():
    print(f'    {k} tem o valor {v}')
