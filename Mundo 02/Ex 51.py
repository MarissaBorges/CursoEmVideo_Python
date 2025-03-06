# -----------------------------------------------
#    EXERCÍCIO 51
# -----------------------------------------------
num = int(input('Informe o primeiro termo da PA: '))
raz = int(input('Informe a razão da PA: '))
fim = num + (10 - 1) * raz #Formula da Progressão Aritmética

print('Os 10 primeiros termos dessa progreção são:')
for c in range(num, fim + raz, raz):
    print(c, end= ' -> ')
print('Fim')
