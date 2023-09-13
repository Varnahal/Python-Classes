n = int(input('quantos numeros da sequencia de fibofodasse quer?'))

un = 0
res = 0
aux = 0
pt= 1
res = pt + un
print(res)

c = 0
while c <n-1:
    aux = res
    res = res + un
    un = aux
    print(res)
    c+=1


