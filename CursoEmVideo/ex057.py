qtt=1
pi = True
while qtt !=0:
    if pi == True:
        pt = int(input('digite o primeiro termo: '))
        ptv = pt
        r = int(input('digite a razão: '))
        pi = False
    qtt = int(input('diga quantos termos quer'))
    pt = ptv
    ut = pt+(qtt-1) * r
    print(pt)
    while pt < ut:
        pt = pt+r
        print(pt)


