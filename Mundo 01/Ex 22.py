# -----------------------------------------------
#    EXERCÍCIO 22
# -----------------------------------------------
nome = str(input('Qual o seu nome completo? ')).strip

print('O seu nome em maiúsculo é: {}'.format(nome.upper()))
print('O seu nome em minúsculo fica: {}'.format(nome.lower()))
dividido = nome.split()
print('O seu nome possui {} caracteres'.format(len(''.join(dividido))))
# print('Seu nome tem ao todo {} letras.format(len(nome) - nome.count(' ')))
print('E o seu primeiro nome possui {} caracteres'.format(len(dividido[0])))
# print('Seu primeiro nome tem {} letras.format(nome.finf(' ')))
