def leiaint():
    try:
        n = input('digite um numero inteiro: ')
        int(n)
    except (ValueError,TypeError):
        print('ERRO DIGITE UM NUMERO INTEIRO')
        return leiaint(input('digite um numero: '))
    except (KeyboardInterrupt):
        print(f'O USUARIO PREFERIU SAIR')
        return 0
    else:
        return int(n)


def leiafloat():
    try:
        n = input('digite um numero float: ')
        float(n)
    except KeyboardInterrupt:
        print(f'O USUARIO PREFERIU SAIR')
        return 0.00
    except:
        print('ERRO DIGITE UM NUMERO FLOAT')
        return leiaint(input('digite um numero: '))
    else:
        return float(n)


n = leiaint()
nf = leiafloat()
print(f"Você acabou de digitar o numero: {n} e {nf:.2f}")
