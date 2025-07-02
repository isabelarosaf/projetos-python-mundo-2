contador = 0

numero = 0

soma = []
soma_numero = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break

    print('Caso queira sair, digite [999]')
    contador += 1 
    soma.append(numero)
    soma_numero = soma_numero + numero
    

print('Foram digitados ao todo {} números e a soma deles é: {} '.format(contador, soma_numero))