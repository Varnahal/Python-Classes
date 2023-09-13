ctn = True
maior = 0
menor = 0
primeira = True


while ctn == True:
    n = int(input('digite um numero: '))
    if primeira == True:
        menor = n
        primeira = False
    
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
    c = str(input('Deseja continuar? [S/N]')).upper()
    if c != 'S':
        ctn = False

print(maior)
print(menor)