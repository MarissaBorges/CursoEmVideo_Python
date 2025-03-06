# -----------------------------------------------
#    EXERCÍCIO 67
# -----------------------------------------------
while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'''{'-'*20}''')
    for c in range (1, 11):
        print(f'{n:2} x {c:2} = {n*c:2}')
    print(f'''{'-'*20}''')
print('PROGRAMA ENCERRADO COM SUCESSO! Volte sempre.')
