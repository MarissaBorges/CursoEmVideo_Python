# -----------------------------------------------
#    EXERCÍCIO 85
# -----------------------------------------------

numeros = [[], []]
for n in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Os valores pares são: {sorted(numeros[0])}')
print(f'E os valores ímpares são: {sorted(numeros[1])} ')
