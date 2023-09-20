pessoa = []
pessoas = []
maior = menor = 0
while True:
    pessoa.append(str(input('Qual o nome? ')))
    pessoa.append(int(input('Qual o peso? ')))

    pessoas.append(pessoa[:])

    pessoa.clear()
    
    sair = str(input('deseja sair? ')).upper()
    if sair == 'S':
        break

print(f'ao todo você cadastrou {len(pessoas)} pessoas')
print(pessoas)

print(f'O maior peso foi de ',end='')

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
        
menor = pessoas[0][1]
for p in pessoas:
    if p[1] < menor:
        menor = p[1]

for p in pessoas:
    if p[1] == maior:
        print(f' [{p[0]}] ',end='')

print(f'\nO menor peso foi de ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f' [{p[0]}] ',end='')