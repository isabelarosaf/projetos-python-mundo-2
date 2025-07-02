acumulador = 0
contador = 0

for c in range(1, 500 + 1):
    if c % 3 == 0 and c % 2 != 0:
        acumulador = acumulador + c
        contador = contador + 1

print('A soma de todos os {} valores solicitados é {}.'.format(contador, acumulador))
