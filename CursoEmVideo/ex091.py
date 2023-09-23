def contador(ini,fim,passo):
    if passo == 0:
        passo = 1
    
    if ini > fim:
        passo = -passo
    
    if fim > 0:
        fim +=1
    else:
        fim -=1
    
    for i in range(ini,fim,passo):
        print(i,end=' ')
    print()


contador(1,10,1)
contador(10,0,2)
contador(5,-5,0)