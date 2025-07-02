lado1 = int(input('Digite o valor do lado um: '))
lado2 = int(input('Digite o valor do lado dois: '))
lado3 = int(input('Digite o valor do lado três: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar um triângulo.', end='')
    if lado1 == lado2 == lado3:
        print('Equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Esse triângulo é isóceles.')
    else:
        print('Esse triângulo é escaleno.')

else:
    print('Os segmentos não podem formar um triângulo.')

