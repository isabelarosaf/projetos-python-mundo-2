n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
# ele vai ler os valores até aparecer um 0, ai o program para


r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer contiunuar? [S/N]')).upper()
print('FIM')
# aqui ele vai continuar até recerber N, ai ele para


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:  #    <isso é uma gambiarra para o teste debaixo funcionar
        if n % 2 == 0:
            par += 1
        else:
            impar += 1 
print('Você digitou {} números pares e {} números impares!'.format(par, impar))
# a gambiarra foi feita para o programa não retornar 0 como um numero par 