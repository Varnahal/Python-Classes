def notas(*notas, sit = False):
    maior = 0
    menor = notas[0]
    qtd = len(notas)
    media = 0
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        media += nota / len(notas)
    if sit:
        if media < 6 :
            situacao = 'Ruim'
        else:
            situacao = 'Boa'
        return {'quantidade':qtd,'maior':maior,'menor':menor,'media':media,'situacao':situacao}
    else:
        return {'quantidade':qtd,'maior':maior,'menor':menor,'media':media}
    
    
print(notas(7.5,10,9.5,sit=True))