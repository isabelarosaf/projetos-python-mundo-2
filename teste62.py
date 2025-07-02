lista_idade = []
somas_idades = 0
maior_idadehomens = -1
nome_maior_idade_homens = ''
idade_mulheres = 20
mulheres_menos_vinte = 0


for c in range(1, 4 + 1):
    nome = str(input('Digite o nome: ')).strip().lower()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (f/m): ').strip().lower()
    lista_idade.append(idade)

    if sexo == 'm' and idade > maior_idadehomens:
     maior_idadehomens = idade
     nome_maior_idade_homens = nome

    if sexo == 'f' and idade <= idade_mulheres:
        mulheres_menos_vinte +=1
        
    print()

for idade in lista_idade:
     somas_idades = somas_idades + idade 

divisao_idade = somas_idades / 4
print('A média de todas as idades é: {}'.format(divisao_idade))


if maior_idadehomens != -1:
     print('A maior idade de um homem é {} e  seu nome é {}.'.format(maior_idadehomens, nome_maior_idade_homens))


print('Ao todo, {} mulheres tem vinte anos ou menos.'.format(mulheres_menos_vinte)) 