nome = str(input('digite seu nome'))
idade = int(input('digite sua idade'))

if idade < 18:
    print(f'ainda faltam {18 - idade} anos para alistar')
elif idade == 18:
    print(f'esta na hora de se alistar')
else:
    print(f'ainda faltam {idade - 18} anos para alistar')