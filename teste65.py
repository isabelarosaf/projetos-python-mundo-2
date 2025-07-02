import random
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 0 

selecionar_numero_aleatorio = random.choice(numero)

jogo = 0
print('Sou seu computador .. Acabei de pensar em um número, tente adivinhar! 😏')
while selecionar_numero_aleatorio != jogo: 
    jogo = int(input('Digite um número de 1 a 10 até descobrir em qual eu pensei! '))
    contador += 1 
    if jogo < selecionar_numero_aleatorio:
        print('Mais... Continue tentando')
    elif jogo > selecionar_numero_aleatorio:
        print('Menos... Continue tentando')

print('Você conseguiu! Foi necessário {} tentativas.'.format(contador))
