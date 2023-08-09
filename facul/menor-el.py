lista = [12,231,77,23,33,57,76]
def menorEl(l):
    num = l[0]
    for el in l:
        if num>el:
            num = el
    return num

print(menorEl(lista))