import math

def metade(valor,f=False):
    if f:
        return moeda(valor/2)
    else:
        return valor/2
    

def dobro(valor,f=False):
    if f:
        return moeda(valor*2)
    else:
        return valor*2

def aumentarpct(valor,pct,f=False):
    if f:
        return moeda(valor + (valor*(pct /100)))
    else:
        return valor + (valor*(pct /100))

def diminuirpct(valor,pct,f=False):
    if f:
        return moeda(valor - (valor*(pct /100)))
    else:
        return valor - (valor*(pct /100))

def moeda(valor):
    valorfmt = str(f'{valor:.2f}').replace('.',',')
    valorfmt = 'R$'+valorfmt
    return valorfmt

def resumo(valor,au,dim):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analisado:":<20}{moeda(valor):>20}')
    print(f'{"O dobro do preço:":<20}{dobro(valor,True):>20}')
    print(f'{f"{au}% de aumento:":<20}{aumentarpct(valor,au,True):>20}')
    print(f'{f"{dim}% de redução:":<20}{diminuirpct(valor,dim,True):>20}')