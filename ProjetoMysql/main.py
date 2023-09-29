import mysql.connector
from Class.Vendas import vendas

venda = vendas('localhost','root','chuvachu','pythoncourse')
venda.listarTudo()
venda.fecharConn()