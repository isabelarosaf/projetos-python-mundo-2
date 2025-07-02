peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

dobro_altura = altura * altura

imc = peso / dobro_altura
print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <=30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade Morbida.')
    