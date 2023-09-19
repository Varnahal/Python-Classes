n = []
par = []
impar = []
while True:
    sair = 'N'
    number = int(input(f'Digite um valor: '))

    n.append(number) 
    sair = str(input('Deseja continuar?[S/N]')).upper()

    if sair == 'N':
        break

for numero in n:
    if numero%2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(n)
print(par)
print(impar)