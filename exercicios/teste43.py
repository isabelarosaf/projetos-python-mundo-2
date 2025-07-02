from datetime import date 

ano_atual = date.today().year

ano_nascimento = int(input('Informe seu ano de nascimento: '))

comparativo_ano = ano_atual - ano_nascimento

if comparativo_ano < 18:
    tempo_falta = 18 - comparativo_ano
    print('Você ainda não chegou na idade de se alistar e deve se alistar em {} anos.'.format(tempo_falta))
elif comparativo_ano > 18:
    tempo_falta1 = comparativo_ano - 18
    print('Já se passou {} anos do seu tempo de alistamento.'.format(tempo_falta1))
elif comparativo_ano == 18:
    print('Você deve se alistar.')

