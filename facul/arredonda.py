lista = [6.2324,3.0887,4.998632]
precisao = [2,2,3]

arruma = lambda item,prec:round(item,prec)

nova_lista = list(map(arruma,lista,precisao))

print(nova_lista)