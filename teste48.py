preço = int(input('Qual é o valor do produto?: R$'))
print('Digite 1 paga pagar a vista no dinheiro') 
print('Digite 2 para pagar a vista no cartão') 
print('Digite 3 para parcelar 2x no cartão')
print('Digite 4 para parcelar em 3 ou mais vezes.')

opçao = int(input('Digite sua opção: '))

a_vista = preço - (preço * 10) / 100

a_vistacartao = preço - (preço * 5) / 100

parcelas_opcao4 = preço + (preço * 20) / 100


if opçao == 1:
    print('Você irá pagar R${}.'.format(a_vista))
elif opçao == 2:
    print('Você irá pagar R${}.'.format(a_vistacartao))
elif opçao == 3:
    print('Você irá pagar R#{}.'.format(preço))
elif opçao == 4:
    qnt_parcelas = int(input('Em quantas vezes será parcelado?: ')) 
    conta = parcelas_opcao4 / qnt_parcelas
    print('Suas parcelas ficaram no valor de R${:.2f} reais.'.format(conta))
    print('Você irá pagar R${} contando com os juros.'.format(parcelas_opcao4))
else:
    print('OPÇÃO INVÁLIDA')