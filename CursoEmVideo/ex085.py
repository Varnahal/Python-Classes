from random import randint
from time import sleep

jogadores = []

for cont in range(0,4):
    jogadores.append({'jogador': cont, 'dado': randint(1,6)} )
    print(f'Jogador{jogadores[cont]["jogador"]+1} Tirou {jogadores[cont]["dado"]} ')
    sleep(0.3)

jogadores.sort(key=lambda dicionario: dicionario['dado'],reverse= True)

print("\n===RANKING===\n")

for i in range(0,4):
    print(f'{i+1}° Lugar: Jogador{jogadores[i]["jogador"]} com {jogadores[i]["dado"]} ')
    sleep(0.3)