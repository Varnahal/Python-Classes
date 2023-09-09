valcasa = int(input('digite o valor da casa'))
sal = int(input('digite o valor de seu salário'))
anos = int(input('digite em quantos anos pretende pagar'))

parcelas = valcasa / anos

if parcelas < sal * 0.3:
    print(f'o valor da parcela é {parcelas} -- aprovado')
else:
    print(f'o valor da parcela é {parcelas} -- reprovado')