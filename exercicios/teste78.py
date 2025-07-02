cedula1= 50
cedula2 = 20
cedula3 = 10
cedula4 = 1
quantid_cedula1 = 0
quantid_cedula2 = 0
quantid_cedula3 = 0
quantid_cedula4 = 0

while True: 
    valor = int(input('Qual valor você quer sacar? R$'))
    quantid_cedula1 = valor // cedula1
    resto = valor % cedula1
    print(f'Total de {quantid_cedula1} cédulas de 50 reais usada')
    
    quantid_cedula2 = resto // cedula2
    resto = resto % cedula2
    print(f'Total de {quantid_cedula2} cédulas de 20 reais usada')

    quantid_cedula3 = resto // cedula3
    resto = resto % cedula3
    print(f'Total de {quantid_cedula3} cédulas de 10 reais usada')

    quantid_cedula4 = resto // cedula4
    resto = resto % cedula4
    print(f'Total de {quantid_cedula4} cédulas de 01 reais usada')