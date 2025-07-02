numero1 = int(input('Digite seu primeiro número inteiro: '))
numero2 = int(input('Digite seu segundo número inteiro: '))

if numero1 > numero2:
    print('O primeiro número é o maior')
elif numero2 > numero1:
    print('O segundo número é o maior')
elif numero1 == numero2:
    print('Não existe número maior, os dois são iguais.')