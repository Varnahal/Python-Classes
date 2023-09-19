n = []

while True:
    sair = 'N'
    number = int(input(f'Digite um valor: '))

    if number not in n:
        n.append(number) 
    else:
        print('numero já cadastrado digite outro')

    
    sair = str(input('Deseja continuar?[S/N]')).upper()



    if sair == 'N':
        break

print(sorted(n))