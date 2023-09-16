palavras = ('macarrao','carro','melao','varnahal','roberto','jooj','penio','morto','computador','ram','processador','placa de video')

vogais = ('a','e','i','o','u')

for i  in palavras:
    print(f'A palavra {i.upper()} tem as vogais: ',end='')
    for l in i:
        for v in vogais:
            if v == l:
                print(f' {v}',end= '')
    print('')