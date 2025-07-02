numero = int(input('Quantos elementos você gostaria de ver na sequência fibonacci: '))

contador = 0 

primeiro_numero = 0
segundo_numero = 1

while contador < numero:
    print(primeiro_numero, end=' ') 

    temporario_valor = primeiro_numero
    primeiro_numero = segundo_numero
    segundo_numero = temporario_valor + segundo_numero

    contador +=1
    

 #   n = int(input('Quantos termos você quer mostrar?'))
 #   t1 = 0
 #   t2 = 1
 #   print('{]  {}'.format (t1, t2))
 #   cont = 3        o contador começa no 3 pq ele ja mostra o primeiro e segundo termo 
 #   while cont <= n:
 #      t3 = t1 + t2
 #       print('{}'.format(t3), end=' ')
 #      t1 = t2
 #      t2 = t3
 #      cont += 1 
 #   print(fim) 