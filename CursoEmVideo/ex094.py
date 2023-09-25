def voto(idade = 0):
    if idade < 16:
        return('Não vota')
    if idade < 18:
        return('Não Obrigatório')
    if idade < 65:
        return('Obrigatório')
    else:
        return('Não Obrigatório')


idade = int(input('Quantos anos você tem?'))
print(f'Com {idade} anos: {voto(idade)}')