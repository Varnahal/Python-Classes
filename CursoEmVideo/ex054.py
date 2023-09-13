from random import randint

ai = randint(1,10)
acertou = False
c = 0
while acertou == False:
    n = int(input('digite um numero de 1 a 10'))
    if n == ai:
        print('vc acertou')
        c +=1
        acertou = True
    else:
        c +=1
        print('errou')
print(f'tentativas: {c}')