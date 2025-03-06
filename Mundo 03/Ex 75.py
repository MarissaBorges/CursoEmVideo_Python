# -----------------------------------------------
#    EXERCÍCIO 75
# -----------------------------------------------
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
num4 = int(input('Quarto número: '))
list = (num1, num2, num3, num4)

print(f'\nOs números escolhidos foram {list}')
print(f'\nO número 9 foi digitado {list.count(9)} vezes')
if 3 not in list:
    print('O número 3 não esta na lista')
else:
    print(f'O número 3 foi digitado na posicão {list.index(3)}')

cont = 0
for c in range(0, 4):
    if list[c] % 2 == 0:
        cont += 1

print(f'Foram digitados {cont} números pares:', end = ' ')

for c in range(0, 4):
    if list[c] % 2 == 0:
        print(list[c], end = ' ')
