maiores = 0
homens = 0
novinhas = 0

while True:
    idade = int(input('Digite a sua idade'))
    sexo = str(input('Digite o seu sexo:[H/M] ')).upper()
    while sexo != 'M' and sexo != 'H':
        sexo = str(input('Digite o seu sexo:[H/M] ')).upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'H':
        homens += 1
    elif sexo == 'M' and idade <= 20:
        novinhas += 1

    c = str(input('deseja continuar? [S/N]')).upper()
    while c != 'S' and c!= 'N':
        c = str(input('deseja continuar? [S/N]')).upper()
    if c == 'N':break

print(maiores)
print(homens)
print(novinhas)
