itens = ('lapis',1.50,'borracha',2.25,'apontador',3.00,'mochila',249.99)

print('---------------------------------------')
print(f"{'LISTAGEM DE PREÇOS':^39}")
print('---------------------------------------')

for i in range(0,len(itens),2):
    palavra_formatada = f"{itens[i]:.<30}R${itens[i+1]:>7}"
    print(palavra_formatada)

print('---------------------------------------')


