# -----------------------------------------------
#    EXERCÍCIO 37
# -----------------------------------------------
num = int(input('''Escreva um número inteiro para a conversão: '''))
base = int(input('''Informe a base de conversão:
[1] Binário
[2] Octagonal
[3] Hexadecimal
Sua escolha: '''))

if base == 1:
    print('O valor {} convertido para Binário é: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O valor {} convertido para Octagonal é: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O valor {} convertido para Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('A base de conversão escolhida é inexistente, por favor tente novamente')
