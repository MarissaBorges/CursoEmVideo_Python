# -----------------------------------------------
#    EXERCÍCIO 25
# -----------------------------------------------
nome = str(input('Qual o seu nome completo? ')).strip()
v = 'SILVA' in nome.upper()
if v == True :
    print('Você possui "SILVA" no nome')
else :
    print('Você não possui "SILVA" no nome')
