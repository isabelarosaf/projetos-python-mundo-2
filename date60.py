from datetime import date

ano_atual = date.today().year

pessoas_maioridade = 0
pessoas_menoridade = 0

for c in range(1, 7 + 1):
    ano = int(input('Digite o ano de nascimento: '))
    
    if ano_atual - ano >= 21:
        pessoas_maioridade = pessoas_maioridade + 1
        
    else:
        pessoas_menoridade = pessoas_menoridade + 1 
        

print('Ao todo, {} pessoas atingiram a maior idade.'.format(pessoas_maioridade))
print('E {} não atingiram a maior idade'.format(pessoas_menoridade))