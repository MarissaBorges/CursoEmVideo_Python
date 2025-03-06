# -----------------------------------------------
#    EXERCÍCIO 44
# -----------------------------------------------
preco = float(input('Informe o valor do produto: '))
pag = int(input("""Escolha qual a condição de pagamento:
À vista dinheiro/cheque = 1
À vista no cartão = 2
Em até 2x no cartão = 3
3x ou mais no cartão = 4
Sua escolha: """))

if pag >= 5:
    print('Não existe essa condição, por favor tente novamente')
elif pag == 1:
    preco = preco - (preco*0.10)
    print('O valor do produto com 10% de desconto é {:.2f} reais'.format(preco))
elif pag ==2:
    preco = preco - (preco*0.05)
    print('O valor do produto com 5% de desconto é {:.2f} reais'.format(preco))
elif pag == 3:
    print('Você não ganhou desconto, o preço do produto é {:.2f} reais'.format(preco))
elif pag ==4:
    preco = preco + (preco*0.20)
    print('''Você terá que pagar 20% de juros sobre o valor do produto
O valor ficou em {:.2f} reais.'''.format(preco))
else:
    print('{}Opção inválida de pagamento{}'.format('\033[32m', '\033[m'))
