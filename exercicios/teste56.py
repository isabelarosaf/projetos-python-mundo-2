acumulador = 0
contador = 0

for c in range(1, 6 + 1):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        acumulador = acumulador + numero
        contador = contador + 1
        
print('Você informou {} numeros pares e sua soma é: {}'.format(contador, acumulador))
