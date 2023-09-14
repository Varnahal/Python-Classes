maisbarato = nome = str(input('Digite o nome do produto: '))
total = maisbaraton = preco = float(input('Digite o preço do produto: '))
maisde1000 = 0

while True:
    c = str(input('deseja continuar? [S/N]')).upper()
    while c != 'S' and c!= 'N':
        c = str(input('deseja continuar? [S/N]')).upper()
    if c == 'N':break


    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    if maisbaraton >= preco:
        maisbaraton = preco
        maisbarato = nome
    if preco >= 1000:
        maisde1000 +=1

    total +=preco

print(f'O total da compra foi: {total}')
print(f'teve {maisde1000} produtos com o valor igual ou acima de 1000 reais')
print(f'O produto mais barato da compra foi: {maisbarato}')

