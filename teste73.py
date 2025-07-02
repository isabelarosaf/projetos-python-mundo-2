soma_numero = 0
quantidade_numero = 0

while True:
    print('Para finalizar o programa, digite os números: 999')
    numero = int(input('Digite um número: '))
    
    if numero == 999:
        break

    soma_numero += numero
    quantidade_numero += 1

print('Programa finalizado.')
print(f'você digitou {quantidade_numero} número(s) e a soma entre eles é: {soma_numero}')

