from random import randint
ai = randint(1,3)
j = int(input('qual sua jogada?\n1-pedra\n2-papel\n3-tesoura\n'))

if ai == 1 and j == 3:
    print('você perdeu')
elif ai == 2 and j == 1:
    print('você perdeu')
elif ai == 3 and j == 2:
    print('você perdeu')
elif ai == j:
    print('empate')
elif j > 3:
    print('valor inválido')
else:
    print('você ganhou')

print(f'as jogadas foram: A.I({ai}) e Vc({j})')