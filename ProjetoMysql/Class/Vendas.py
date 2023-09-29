import mysql.connector
class vendas:
    def __init__(self,host,user,password,database):
        try:
            print ('\033[32m'+'CONECTANDO AO BANCO DE DADOS...'+'\033[0;0m')
            self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
            ) 
        except Exception as e:
            print ('\033[31m'+'ERRO AO ACESSAR BANCO DE DADOS'+'\033[0;0m' + e)
        else:
            print ('\033[32m'+'CONECTADO COM SUCESSO'+'\033[0;0m')
            self.cursor = self.conn.cursor()

    def listarTudo(self):
        cmd = 'SELECT * FROM pythoncourse.vendas'
        try:
            self.cursor.execute(cmd)#no primeiro parametro você coloca a query sql e no segundo coloca os valores que quer passar pra essa query
            vendas = self.cursor.fetchall()
            desc = self.cursor.description
        except:
            print ('\033[31m'+'ERRO AO EXECUTAR QUERY,CONFIRA AS INFORMAÇÔES'+'\033[0;0m')
        else:
            columns = [col[0] for col in desc]
            vendas_as_dicts = []
            for row in vendas:
                venda_dict = {columns[i]: row[i] for i in range(len(columns))}
                vendas_as_dicts.append(venda_dict)
            for venda in vendas_as_dicts:
                print(f"O produto {venda['nome_produto']} custa R${venda['valor_produto']}")
            print ('\033[32m'+f'PRODUTOS LISTADOS COM SUCESSO'+'\033[0;0m')


    def inserirVenda(self,nome,valor):
        cmd = 'INSERT INTO pythoncourse.vendas (nome_produto, valor_produto) VALUES(%s,%s)'
        values = (nome,valor)
        try:
            self.cursor.execute(cmd,values)#no primeiro parametro você coloca a query sql e no segundo coloca os valores que quer passar pra essa query
        except:
            print ('\033[31m'+'ERRO AO EXECUTAR QUERY,CONFIRA AS INFORMAÇÔES'+'\033[0;0m')
        else:
            print ('\033[32m'+f'O PRODUTO {nome} E VALOR {valor} FOI INSERIDO COM SUCESSO'+'\033[0;0m')

        self.conn.commit()#Apos executar tudo você roda esse comando de comitar
    

    def alteraValor(self,id,alterar,valor):
        cmd = 'UPDATE pythoncourse.vendas SET '+alterar+' = %s WHERE idVendas = %s'
        values = (valor,id)
        try:
            self.cursor.execute(cmd,values)#no primeiro parametro você coloca a query sql e no segundo coloca os valores que quer passar pra essa query
        except:
            print ('\033[31m'+'ERRO AO EXECUTAR QUERY,CONFIRA AS INFORMAÇÔES'+'\033[0;0m')
        else:
            print ('\033[32m'+f'O PRODUTO ALTERADO COM SUCESSO'+'\033[0;0m')

        self.conn.commit()#Apos executar tudo você roda esse comando de comitar
    

    def deletaVenda(self,id):
        cmd = 'DELETE FROM pythoncourse.vendas WHERE idVendas = %s'
        values = [id]
        try:
            self.cursor.execute(cmd,values)#no primeiro parametro você coloca a query sql e no segundo coloca os valores que quer passar pra essa query
        except:
            print ('\033[31m'+'ERRO AO EXECUTAR QUERY,CONFIRA AS INFORMAÇÔES'+'\033[0;0m')
        else:
            print ('\033[32m'+f'O PRODUTO FOI DELETADO COM SUCESSO'+'\033[0;0m')

        self.conn.commit()#Apos executar tudo você roda esse comando de comitar
    

    def fecharConn(self):
        try:
            self.cursor.close()
            self.conn.close()
        except:
            print('\033[31m'+'ERRO AO FECHAR BANCO DE DADOS,(VERIFIQUE SE FOI ABERTO CORRETAMENTE)'+'\033[0;0m')






