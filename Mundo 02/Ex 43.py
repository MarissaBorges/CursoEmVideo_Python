# -----------------------------------------------
#    EXERCÍCIO 43
# -----------------------------------------------
peso = float(input('Qual o seu peso em kg? '))
altu = float(input('Qual a sua altura em metros? '))
imc = peso / (altu**2)

print('O seu IMC é de {}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc < 25:
    print('Você esta com o peso ideal')
elif imc < 30:
    print('Você esta com sobrepeso')
elif imc < 40:
    print('Você esta com obesidade')
else:
    print('Você esta com obesidade mórbida')
