# -----------------------------------------------
#    EXERCÍCIO 90
# -----------------------------------------------

dados = {}
nome = str(input('Nome do aluno: '))
media = float(input(f'Média de {nome}: '))
dados = {'Nome': nome, 'Média': media}
if media > 7:
    dados['Situação'] = 'Aprovado'
elif 5 <= media < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'
print('-='*20)
for k, v in dados.items():
    print(f'{k} é igual a {v}')
