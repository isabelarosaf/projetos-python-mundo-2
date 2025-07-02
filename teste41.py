num = int(input('Digite um número inteiro: '))
print('Escolha sua base de conversão! Digite 1 para binário, 2 para octal e 3 para hexadecimal')
base = int(input('Agora digite o número da base: '))

if base == 1:
        print(bin(num))

elif base == 2:
    print(oct(num))

elif base == 3:
    print(hex(num))

else:
     print('Opção inválida.')