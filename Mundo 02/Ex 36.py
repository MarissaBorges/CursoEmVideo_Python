# -----------------------------------------------
#    EXERCÍCIO 36
# -----------------------------------------------
vlrCasa = float(input('Qual o valor da casa? '))
sal = float(input('Informe o salário: '))
anos = int(input('Quantos anos pretente pagar? '))
tempo = int(anos * 12)
prest = vlrCasa / tempo
parcsal = sal*0.30

if prest > parcsal:
    print('A compra de sua casa foi NEGADA!! Pois você excedeu o valor de 30% do seu salário')
else:
    print('A compra da sua casa foi APROVADA!! Você tera que pagar {:.2f} por mês'.format(prest))
