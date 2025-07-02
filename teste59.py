frase = input('Digite sua frase: ').split(" ")
juntar = ''.join(frase)

print(juntar)

frase_ao_contrario = []

for i in range(len(juntar) -1, -1, -1):
    frase_ao_contrario.append(juntar[i])

frase_contraria_junta = ''.join(frase_ao_contrario)

if frase_contraria_junta == juntar:
    print("É um palíndromo")
else:
    print("Nâo é um palíndromo")