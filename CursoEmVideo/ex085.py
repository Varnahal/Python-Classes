from random import randint

j1 = {'jogador':'1','dado':randint(1,6)} 
j2 = randint(1,6)
j3 = randint(1,6)
j4 = randint(1,6)

jogadores = [j1,{'jogador':'2','dado':j2},{'jogador':'3','dado':j3},{'jogador':'4','dado':j4}]

jogadores.sort(key=lambda dicionario: dicionario['dado'],reverse= True)

for i in range(0,4):
    print(f'{i+1}° Lugar: Jogador{jogadores[i]["jogador"]} com {jogadores[i]["dado"]} ')