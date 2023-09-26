def leiaint(msg):
    try:
        n = input(msg)
        int(n)
    except (ValueError,TypeError):
        print('ERRO DIGITE UM NUMERO INTEIRO')
        return leiaint(input('digite um numero: '))
    except (KeyboardInterrupt):
        print(f'O USUARIO PREFERIU SAIR')
        exit()
    else:
        return int(n)


def linha(tam = 42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(f"{txt:^42}")
    print(linha())


def menu(lista):
    cabecalho('Menu principal')
    for k,opc in enumerate(lista):
        print(f"{k+1} - {opc}")
    print(linha())
    opc = leiaint('Digite a opção: ')
    return opc
    