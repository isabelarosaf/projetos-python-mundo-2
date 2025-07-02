num = int(input('Digite um número: '))

acumulador = 0

for c in range(1, num + 1):
    if num % c == 0:
        acumulador += 1
      
print('O numero {} foi divisivel {} vezes'.format(num, acumulador))

if acumulador == 2:
    print('E por isso ele é primo')
else:
    print('e por isso ele não é primo')