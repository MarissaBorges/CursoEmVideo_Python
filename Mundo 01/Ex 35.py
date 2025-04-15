# -----------------------------------------------
#    EXERCÍCIO 35
# -----------------------------------------------

# PROJETO QUE ANALISA SEGMENTOS DE RETAS E INFORMA SE É POSSÍVEL FORMAR UM TRIÂNGULO E QUAL SEU TIPO

r1 = float(input('informe o comprimento 1: '))
r2 = float(input('Informe o comprimento 2: '))
r3 = float(input('Informe o último comprimento: '))

con1 = bool((r2+r3) > r1)
con2 = bool((r1+r3) > r2)
con3 = bool((r1+r2) > r3)

err = 'Elas não podem formar um triângulo'

if con1 == True:
    if con2 == True:
        if con3 == True:
            print('As três retas podem formar um triângulo.')
        else:
            print(err)
    else:
        print(err)
else:
    print(err)

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Eles podem formar um triângulo')
# else:
#     print('Eles não podem formar um triângulo')
