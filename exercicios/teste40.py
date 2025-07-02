casa = int(input('Qual é o preço da casa?: '))
salario = int(input('Quanto você ganha por mês?: '))
anos = int(input('Em quantos anos será pago?: '))

tempo_prestacao = anos * 12 
valor_prestacao = casa / tempo_prestacao
um_terco_salario = (30 * salario) / 100

print('Você levará {} meses para pagar.'.format(tempo_prestacao))
print('O valor da prestação será de R${:.2f}.'.format(valor_prestacao))
print('Trinta por cento do seu salário é R${}.'.format(um_terco_salario))

if valor_prestacao > um_terco_salario:
    print('Seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado.')
