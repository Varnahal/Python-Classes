
class Extrato:
    def __init__(self,idConta):
        self.conta = idConta
        self.transacoes = []
    
    def addTransacao(self,transacao):
        self.transacoes.append(transacao)
    
    def mostrarExtrato(self):
        for t in self.transacoes:
            print(t)
