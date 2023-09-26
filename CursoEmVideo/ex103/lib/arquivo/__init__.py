from lib.interface import *

def arquivoExiste(arq):
    try:
        a = open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except :
        print('erro ao criar arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho("PESSOAS CADASTRADAS")
        pessoas = a.readlines()
        for pessoa in pessoas:
            pessoa = pessoa.split(';')
            pessoa[1] = pessoa[1][:-1]
            print(f"{pessoa[0]:<20}{f'{pessoa[1]} Anos':>20}")
    finally:
        a.close()

def cadastrar(arq,nome = 'Desconhecido',idade = 0):
    try:
        a = open(arq,'at',encoding='utf-8')
    except:
        print('Erro ao abrir arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('erro ao escrever os dados')
    finally:
        a.close()