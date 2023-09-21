pessoa = {}

pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input('media: '))

print(f'O nome é igual a {pessoa["nome"]}')
print(f'A média é igual a {pessoa["media"]}')

print('A situação é igual a ',end='')
if pessoa['media'] <6:
    print('reprovado')
elif pessoa['media'] <8:
    print('recuperação')
else:
    print('Aprovado')