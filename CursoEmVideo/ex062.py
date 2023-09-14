while True: 
    n = int(input('Digite a tabuada que deseja sabero valor: '))
    if n <0:
        break
    print(f'''
    ---------------------------------/n
    1 X {n} = {n*1}\n
    2 X {n} = {n*2}\n
    3 X {n} = {n*3}\n
    4 X {n} = {n*4}\n
    5 X {n} = {n*5}\n
    6 X {n} = {n*6}\n
    7 X {n} = {n*7}\n
    8 X {n} = {n*8}\n
    9 X {n} = {n*9}\n
    10 X {n} = {n*10}\n
    ---------------------------------/n
    ''')
print('Programa encerrado!!!')