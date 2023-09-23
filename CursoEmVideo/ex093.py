from random import randint

def sorteia(lista):
    for i in range(0,5):
        lista.append(randint(0,100))
    somapar(lista)

def somapar(lista):
    par = 0
    for i in lista:
        if i %2 == 0:
            par += i
    print(par)
    print(lista)

minhalista = []

sorteia(minhalista)