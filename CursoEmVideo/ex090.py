def escreva(msg):
    num = (len(msg)+4)
    print('~'*num)
    print(f'{msg:^{num}}')
    print('~'*num)

escreva('Meu pau')