#------------------------------------------------
#    EXERCÍCIO 92
# -----------------------------------------------
# 35 anos de contribuição
from datetime import date

dados = {}
nome = str(input('Nome: '))
dados['Nome'] = nome
ano_nasc = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano_nasc
dados['Idade'] = idade
ctps = int(input('Carteira de Trabalho (0 não tem): '))
dados['CTPS'] = ctps
if ctps != 0:
    ano_contra = int(input('Ano de Contratação: '))
    dados['Contratação'] = ano_contra
    salario = int(input('Salário: R$ '))
    dados['Salário'] = salario
    resto_apose = 35 - (date.today().year - ano_contra)
    aposentadoria = idade + resto_apose
    dados['Aposentadoria'] = aposentadoria

print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')