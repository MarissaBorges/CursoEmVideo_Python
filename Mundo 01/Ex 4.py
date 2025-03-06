# -----------------------------------------------
#    EXERCÍCIO 04
# -----------------------------------------------

n = input('Digite algo: ')
print(type(n))
print('É numérico?', n.isnumeric())
print('É letra?', n.isalpha())
print('Pode ser printado?', n.isprintable())
print('Só tem espaços?', n.isspace())
print('É alpha numérico?', n.isalnum())
print('Esta em maiúsculas?', n.isupper())
print('Esta em minúsculas?', n.islower())
print('Esta capitalizada?', n.istitle())
