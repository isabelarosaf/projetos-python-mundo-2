import random

print('-'*27)
print('VAMOS JOGAR PAR OU IMPAR.')
print('-'*27)

numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 0

while True:
    numero_jogador = int(input('Digite um valor: '))
    numero_computador = random.choice(numero)
    par_impar = str(input('Par ou Ímpar: [P/I] ')).upper().strip()[0]
    if (par_impar != 'P' and par_impar != 'I'):
        continue
    conta = numero_computador + numero_jogador
    
    print(f'Você jogou {numero_jogador} e o computador {numero_computador}. O total deu {conta}.')
    
    if conta % 2 == 0:
        if par_impar == 'P':
            contador += 1 
            print('Você ganhou. Vamos jogar novamente!')
        else:
            print(f'GAME OVER. Você venceu {contador} vezes.')
            break
                
    else:
        if par_impar == 'I':
            contador += 1 
            print('Você ganhou. Vamos jogar novamente!')
        else:
            print(f'GAME OVER. Você venceu {contador} vezes.')
            break
            


        