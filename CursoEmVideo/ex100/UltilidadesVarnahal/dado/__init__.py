def leiaDinheiro(texto):
    while True:
        valor = str(input(texto)).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print('ERRO VALOR INVÁLIDO') 
        else:
            return(float(valor))