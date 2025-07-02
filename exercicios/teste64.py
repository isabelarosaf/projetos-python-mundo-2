sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0] 
    if sexo == 'F':
        print('Sexo F registrado com sucesso')
    elif sexo == 'M':
        print('Sexo M registrado com sucesso')
print('fim')
    