pessoas = []
pessoa = {}
media = 0
mulheres = []
acimamedia = []
while True:

    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo: ')).upper()
    idade = int(input('Digite sua idade: '))

    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade

    pessoas.append(pessoa.copy())
    pessoa.clear()


    continuar = str(input('Deseja continuar?[S/N]')).upper()
    if continuar == 'N':
        break
print('-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Foram cadastradas {len(pessoas)}')

for p in pessoas:
    media += p['idade'] / len(pessoas)
    if p['sexo'] == 'F':
        mulheres.append(p.copy())

for p in pessoas:
    if p['idade'] > media:
        acimamedia.append(p)


print(f'A media da idade das pessoas foi: {media:.2f}')
print(f'A mulheres foram:')

for m in mulheres:
    print(f'=> {m["nome"]}')
print(f'As pessoas com a idade acima da média foram:')
for ac in acimamedia:
    print(f'=> {ac["nome"]}')
print('-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')