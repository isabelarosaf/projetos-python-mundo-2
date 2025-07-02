nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

calculo_media =  (nota1 + nota2) / 2
print('Sua média é {}.'.format(calculo_media))

if calculo_media >= 7:
    print('Aprovado')
elif calculo_media < 5:
    print('Reprovado')
elif calculo_media < 7:
    print('Recuperação')