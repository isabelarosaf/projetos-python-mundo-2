primeiro_termo = int(input('Digite o primeiro termo da sua progressão aritmética: '))
razao = int(input('Digite a razão da sua progressão aritmética: '))

print(primeiro_termo)
acumulador = 1

while acumulador < 10:
    primeiro_termo = primeiro_termo + razao 
    acumulador += 1
    print(primeiro_termo, end=' ')