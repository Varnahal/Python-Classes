n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
n4 = int(input('digite um numero: '))

tupla = (n1,n2,n3,n4)


print(tupla.count(9))
if (tupla.count(3) != 0): 
    print(tupla.index(3)+1)
else:
    print(0)
print('os numeros pares foram: ',end='')
for n in tupla:
    if(n%2==0):
        print(f' {n} ',end='')