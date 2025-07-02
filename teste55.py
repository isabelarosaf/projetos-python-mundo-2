numero = int(input('Digite o número que você gostaria de ver a tabuada: '))

for c in range(1, 10 + 1 ):
    print('{} x {} = {}'.format(numero, c, numero*c))