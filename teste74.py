tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    numero = int(input('Você gostaria de ver a tabuada de qual número: '))
    if numero < -1:
        break
    for c in tabuada:
        print(f'{numero} x {c} = {numero*c}')
print('Programa finalizado.')
    