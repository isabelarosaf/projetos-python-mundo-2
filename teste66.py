usuario = -1
print('Digite dois valores e selecione uma opção.')
print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))


while usuario != 0:
    usuario = int(input('Qual será a operação: '))
    maior_lista = [numero1, numero2]

    if usuario > 5:
        print('Operação inválida.')

    if usuario == 1:
        somar = numero1 + numero2
        print('A opção selecionada foi SOMAR e o resultado é: {} '.format(somar))

    if usuario == 2:
        multiplicar = numero1 * numero2
        print('A opção selecionada foi MULTIPLICAR e o resultado é: {} '.format(multiplicar))

    if usuario == 3:
        maior = max(maior_lista)
        print('A opção selecionada foi MAIOR e o maior número é: {} '.format(maior))

    if usuario == 4:
        print('Você escolheu a opção NOVOS NÚMEROS')
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
        
    if usuario == 5:
        print('Até logo.')
        break