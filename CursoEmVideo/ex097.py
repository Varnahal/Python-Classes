def leiaint(n):
    if (n.isnumeric()):
        return n
    else:
        print('ERRO DIGITE UM NUMERO')
        return leiaint(input('digite um numero: '))
print(f"Você acabou de digitar o numero: {leiaint(input('digite um numero: '))}")