numero = 0
escolha = 'S'
lista_numero = []
soma_dos_numero = 0
divisao_da_soma = 0
contador = 0

while escolha == 'S':
    numero = int(input('Digite um número: '))
    escolha = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
    lista_numero.append(numero)
       
for c in lista_numero:
    soma_dos_numero = soma_dos_numero + c
    contador += 1  

divisao_da_soma = soma_dos_numero / contador
print('A média de todos os números digitados é: {}'.format(divisao_da_soma))

maior = max(lista_numero)
menor = min(lista_numero)

print('O menor número digitado foi {} e o maior foi {}.'.format(menor, maior))

print('FIM')