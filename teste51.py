n = int(input('Digite um número: '))
for c in range (0, n + 1):   #o +1 serve p contar até o núm que o usuario pedir 
    print(c)
print('FIM')





i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))    #Pular de quantas em quantas casas?
for c in range(i, f+1, p):
    print(c)
print('FIM')





for c in range(0,3):                    #  < a variavel vai se repetir 3 vezes 
    n = int(input('Digite um valor:'))
print('FIM')


s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n     #    < pode ser escrito tb como    s+= n
print('O somatório de todos os valores foi {}'.format(s))