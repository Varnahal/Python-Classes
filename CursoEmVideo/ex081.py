matrix = [[],[],[]]
somapar = somasc = maiorsl = 0
for i  in range(0,3):
    for j  in range(0,3):
        matrix[i].insert(j,int(input(f'digite um numero, posição[{i},{j}]: ')))


for i  in range(0,3):
    for j  in range(0,3):
        print(f'[{matrix[i][j]}]',end='')
        if matrix[i][j] % 2 == 0:
            somapar += matrix[i][j]
        if j == 2:
            somasc += matrix[i][j]
        if i == 1 and matrix[i][j] > maiorsl:
            maiorsl = matrix[i][j]
    print('\n')

print(somapar)
print(somasc)
print(maiorsl)