n1 = 0
n2 = 0
for i in range(0,7):
    n = int(input('digite a idade: '))
    if n >= 21:
        n1 += 1
    else:
        n2 +=1

print(f'o numero de pessoas que são maiores de 21 são: {n1} e que são menores: {n2}')