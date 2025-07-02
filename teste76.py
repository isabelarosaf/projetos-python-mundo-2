print('Cadastre uma pessoa.')
contador_homens = 0
contador_mulheres_20anos = 0 
maior_dezoito = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if sexo == 'M':
         contador_homens += 1

    if sexo == 'F' and idade < 20:
        contador_mulheres_20anos += 1
        
    if idade >= 18:
        maior_dezoito +=1

    if usuario == 'N':
        break
print('Fim do programa.')
       
print(f'Ao todo, temos {contador_homens} homem(s) cadastrados.')
print(f'Temos {contador_mulheres_20anos} mulher(s) com menos de 20 anos.')
print(f'Total de pessoas com mais de 18 anos: {maior_dezoito}')
    