from UltilidadesVarnahal import moeda,dado
#preco = 100.55
preco = dado.leiaDinheiro('Digite o preço: R$')
print(f'A metade de {preco} é: {moeda.metade(preco,True)}')
print(f'O dobro de {preco} é: {moeda.dobro(preco,True)}')
print(f'Aumentando 10% em {preco} temos: {moeda.aumentarpct(preco,10,True)}')
print(f'Diminuindo 13% em {preco} temos: {moeda.diminuirpct(preco,13,True)}')
print()
moeda.resumo(preco,10,13)