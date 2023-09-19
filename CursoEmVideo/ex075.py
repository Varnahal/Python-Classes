n = []
cont = 0
while True:
    sair = 'N'
    number = int(input(f'Digite um valor: '))

    n.append(number) 
    cont+=1
    sair = str(input('Deseja continuar?[S/N]')).upper()

    if sair == 'N':
        break

print(f'o total de valores foi: {cont}')
n.sort(reverse=True)
print(f'{n}')
if 5 in n:
    print('tem o 5')