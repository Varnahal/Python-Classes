lista = [1,2,3,4,5,6,7,8,9,0,10]
    
par = lambda item:item%2==0

nova_lista = list(filter(par,lista))
print(lista)
print(nova_lista)