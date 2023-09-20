numeros = []

for i in range(0,7):
    numeros.append(int(input('digite um numero')))

numeros.sort()
print('Os valores pares digitados foram: [',end='')
for n in numeros:
    if n % 2 == 0:
        print(f' {n} ',end='')


print(']\nOs valores inpares digitados foram: [',end='')
for n in numeros:
    if n % 2 != 0:
        print(f' {n} ',end='')
print(']')