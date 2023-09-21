import time
#print(time.localtime().tm_year)

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = time.localtime().tm_year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano da contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] =(35 - (time.localtime().tm_year - pessoa['contratação'])) +pessoa['idade']
print(f'{"-":-<80}')

for k,v in pessoa.items():
    if k == 'ctps' and v == 0:
        continue
    print(f'{k} tem o valor {v}')









