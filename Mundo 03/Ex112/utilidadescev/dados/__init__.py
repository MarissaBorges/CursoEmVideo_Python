def LeiaDinheiro(msg):
    while True:
        num = input(msg).replace(',', '.').strip()
        if num.replace('.', '', 1).isdigit():
            valor = float(num)
            break
        else:
            print(f'\033[31mERRO: "{num}" é um preço inválido!!\033[m')
    return float(valor)

