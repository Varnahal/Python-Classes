n = []

for c in range(0,5):
    n.append(int(input(f'Digite um valor para a posição {c+1}: '))) 

print(f'Você digitou: {n}')

print(f'O menor valor digitado foi: {min(n)} nas posições:',end='')

for c,i in enumerate(n):
    if i == min(n):
        print(f' {c+1}',end='')

print(f'\nO maior valor digitado foi: {max(n)} nas posições:',end='')

for c,i in enumerate(n):
    if i == max(n):
        print(f' {c+1}',end='')