nome = str(input('Nome do jogador: '))
npartidas = int(input(f'quantas partidas {nome} jogou? '))
gols = []
soma = 0

for i in range(0,npartidas):
    gols.append(int(input(f'quantas gols fez na partida {i+1}? ')))

for gol in gols:
    soma +=gol

jogador = {'nome':nome,'gols':gols,'total':soma}

for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=--=---=-=-=-=-=-=-=-=-=-')
print(f' o jogador {jogador["nome"]} jogou {npartidas}')

for i in range(0,npartidas):
    print(f'=> Na partida {i+1},fez {jogador["gols"][i]}')

print(f'Foi um total de {jogador["total"]}')