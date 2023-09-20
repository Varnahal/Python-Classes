from random import randint

n = int(input('Quantos jogos deseja? '))
jogos = []
jogo = []



for i in range(0,n):
    for j in range(0,6):
        jogo.append(randint(1,60))
    jogos.append(jogo[:])
    jogo.clear()

for i in range(0,n):
    print(f'Jogo {i+1}: {jogos[i]}')