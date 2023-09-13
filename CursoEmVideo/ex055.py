denovo = True
sair = False
while sair == False:
    if denovo == True:
        denovo = False
        n1 = int(input('digite o primeiro numero: '))
        n2 = int(input('digite o segundo numero: '))

    e = 0
    e = int(input('[1]-Somar\n[2]-Multiplicar\n[3]-Maior\n[4]-Novos numeros\n[5]-Sair\n'))
    if e == 1:
        print(f'o resultado da soma é: {n1+n2}')
    elif e == 2:
        print(f'o resultado da multiplicação é: {n1*n2}')
    elif e == 3:
        if n1>n2:
            print(f'O maior numero é:{n1}')
        else:
            print(f'O maior numero é{n2}')
    elif e == 4:
        print('digite novos numeros: ')
        denovo = True
    elif e == 5:
        print('Finalizando...')
        sair = True
print('Programa finalizado!')