# -----------------------------------------------
#    EXERCÍCIO 72
# -----------------------------------------------
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte', '') 
num = int(input('Informe um número de 0 a 20: '))
while num > 20 or num < 0:
    num = int(input('Número inválido!! Informe um número de 0 a 20: '))
print(f'Você digitou o número "{extenso[num]}"')
