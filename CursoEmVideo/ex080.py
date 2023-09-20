matrix = [[],[],[]]

for i  in range(0,3):
    for j  in range(0,3):
        matrix[i].insert(j,int(input(f'digite um numero, posição[{i},{j}]: ')))


for i  in range(0,3):
    for j  in range(0,3):
        print(f'[{matrix[i][j]}]',end='')
    print('\n')
