c = s = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    c+=1
    s+=n
print(f'teve {c} numeros')
print(f'A soma entre os numeros digitados foi:  {s}')