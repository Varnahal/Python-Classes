n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))

md = (n1+n2) / 2

if md < 5:
    print(f'reprovado média: {md}')
elif md < 6.9:
    print(f'recuperação média: {md}')
else:
    print(f'aprovado média: {md}')