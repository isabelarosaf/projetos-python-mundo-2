primeiro_termo = int(input('Digite o primeiro termo da sua progressão aritmética: '))
razao = int(input('Digite a razão da sua progressão aritmética: '))

print(primeiro_termo)
for c in range(1, 10 + 1):
    primeiro_termo = primeiro_termo + razao
    print(primeiro_termo)