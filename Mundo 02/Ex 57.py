# -----------------------------------------------
#    EXERCÍCIO 57
# -----------------------------------------------
sexo = str(input('Qual o seu sexo? ')).upper().strip()[0]

while sexo != 'F' and sexo != 'M':
    sexo = str(input('O valor digitado esta incorreto, digite novamente o sexo correto: ')).upper().strip()[0]
print('Dados registrados')
