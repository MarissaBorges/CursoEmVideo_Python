# -----------------------------------------------
#    EXERCÍCIO 34
# -----------------------------------------------
sal = float(input('Qual o valor do seu salario? R$'))
aum1 = sal*0.15
aum2 = sal*0.1
if sal <= 1250.00:
    print('O valor do seu aumento é {:.2f} reais, e o seu novo salário é {:.2f} reais.',format(aum1, sal+aum1))
else:
    print('O valor do seu aumento é {:.2f} reais, e o seu novo salário é {:.2f} reais.'.format(aum2, sal+aum2))
