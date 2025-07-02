import random
from time import sleep

print('-=-'*20)
print('{:^60}'.format('Vamos jogar Jokenpô!'))
print('-=-'*20)
print('Pressione [1] para papel ')
print('Pressione [2] para pedra ')
print('Pressione [3] para tesoura ')
jogador = int(input('Você joga pedra, papel ou tesoura?: '))

print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
sleep(1)

opçoes = [1, 2, 3]
opçoes_aleatorio = random.choice(opçoes)
print('Eu escolhi {}.'.format(opçoes_aleatorio))


if opçoes_aleatorio == jogador:
    print('Empatamos!')

elif opçoes_aleatorio == 2:
    if jogador == 1:
        print('Você ganhou.')
    elif jogador == 3:
        print('Você perdeu.')

elif opçoes_aleatorio == 1:
    if jogador == 2:
        print('Você perdeu')
    elif jogador == 3:
        print('Você ganhou.')

elif opçoes_aleatorio == 3:
    if jogador == 1:
        print('Você perdeu.')
    elif jogador == 2:
        print('Você ganhou.')
    else:
        print('[ERRO] JOGADA INVÁLIDA!')
