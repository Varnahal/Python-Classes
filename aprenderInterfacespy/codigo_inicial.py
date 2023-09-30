import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_eth = requisicao_dic['ETHBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar} Reais
    Euro: {cotacao_euro} Reais
    BTC: {cotacao_btc} Reais
    ETH: {cotacao_eth} Reais'''

    texto_resultado['text'] = texto



janela = Tk()#cria a janela principal

janela.geometry('400x400')


janela.title('Cotação das moedas')

texto_orientacao = Label(janela,text='Clique no botão para ver a cotação')
texto_orientacao.grid(column=0,row=0,padx=10,pady=10,)

botao = Button(janela,text='Clique aqui!',command=pegar_cotacoes)
botao.grid(column=0,row=1,padx=10,pady=10)

texto_resultado = Label(janela,text='')
texto_resultado.grid(column=0,row=2,padx=10,pady=10)



janela.mainloop()#mantem a janela aberta, sera sempre a ultima linha do tk