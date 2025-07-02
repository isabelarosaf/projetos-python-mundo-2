from datetime import date

ano_atual = date.today().year
ano = int(input('Digite o ano de nascimento do atlteta: '))

comparativo_ano =  ano_atual - ano
print('O atleta tem {} anos.'.format(comparativo_ano))

if comparativo_ano <= 9:
    print('Mirim')
elif comparativo_ano <= 14:
    print('Infantil')
elif comparativo_ano <= 19:
    print('Junior')
elif comparativo_ano <= 25:
    print('Sênior')
elif comparativo_ano > 25:
    print('Master')
