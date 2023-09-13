ctn = True
c = 0
soma = 0

while ctn == True:
    n = int(input('digite um numero: '))
    if n == 999:
        ctn = False
    else:
        c+=1
        soma +=n
    
print(c)
print(soma)
