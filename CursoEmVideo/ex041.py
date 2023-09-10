p = float(input('qual o preço'))
f = int(input('qual a forma de pagamento?\n1-Dinheiro/cheque\n2-cartão\n'))

if f == 1:
    print(f'O valor da compra é: {p - (p*0.10)}')
elif f == 2:
    v = int(input('em quantas vezes deseja? 1 à 12'))
    if v == 1:
        print(f'O valor da compra fica: {p - (p*0.05)}')
    elif v <= 2:
        print(f'O valor da compra fica: {p} em {v} vezes de {p/v}')
    elif v > 2:
        p = p + (p*0.20)
        print(f'O valor da compra fica: {p} em {v} vezes de {p/v}')
else:
    print('opção invalida')