
print('Qual valor deseja sacar? ')
n = int(input(''))

c50 = n//50
n = n%50
c20 = n//20
n = n%20
c10 = n//10
n = n%10
c1 = n//1

print(f'cedula de 50: {c50}')
print(f'cedula de 20: {c20}')
print(f'cedula de 10: {c10}')
print(f'cedula de 1: {c1}')