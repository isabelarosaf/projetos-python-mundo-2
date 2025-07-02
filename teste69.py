primeiro_termo = int(input('Digite o primeiro termo da sua progressão aritmética: '))
razao = int(input('Digite a razão da sua progressão aritmética: '))

print(primeiro_termo)
acumulador = 0

while acumulador < 10:
    primeiro_termo = primeiro_termo + razao 
    acumulador += 1
    print(primeiro_termo, end=' ')
    if acumulador == 10:
        usuario = int(input('Gostaria de ver mais quantos termos? ' ))
        acumulador = acumulador - usuario
    


