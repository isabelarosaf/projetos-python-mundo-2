lista_produtos = []
soma_preco = 0
produto_acima1000 = 0
produto_mais_barato = ''
preco_mais_barato = 1000

while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: '))
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    lista_produtos.append(preco)
    
    if preco_mais_barato > preco:
        preco_mais_barato = preco
        produto_mais_barato = produto
    
    if preco > 1000:
        produto_acima1000 += 1 

    if usuario == 'N':
        break
print('Programa Finalizado.')

for c in lista_produtos:
    soma_preco = soma_preco + c


print(f'O total da compra foi R${soma_preco}.')
print(f'Temos {produto_acima1000} produtos custando mais de R$1000.00 reais')
print(f'O produto mais barato foi {produto_mais_barato} que custa R${preco_mais_barato}')