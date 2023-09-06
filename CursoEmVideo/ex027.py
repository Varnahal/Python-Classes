from random import randint

n = randint(0,5)

n1 = int(input('qual tu acha que éra o numero?'))

if n == n1:
    print("você acertou")
else:
    print(f'você errou o valor era {n} e você digitou {n1}')