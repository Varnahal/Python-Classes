from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "C:/Users/danie/Documents/GitHub/Python-Classes/CursoEmVideo/ex103/pessoas.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)



while True:
    res = menu(['Ver Pessoas Cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if res == 1:
        #Vai ler o arquivo e listar tudo
        lerArquivo(arq)
    elif res == 2:
        #Cadastrar a pessoa
        nome = str(input('Digite o nome:'))
        idade = int(input('Digite a idade:'))
        cadastrar(arq, nome, idade)
    elif res == 3:
        cabecalho ('Saindo do sistema...')
        break
    else:
        print('Erro valor inválido')
    sleep(1)
    