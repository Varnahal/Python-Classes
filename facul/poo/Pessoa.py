class Pessoa:
    def __init__(self,name,adress):
        self.setNome(name)
        self.setEnder(adress)

#Setters
    def setNome(self,nome):
        self.nome = nome 

    def setEnder(self,ender):
        self.ender = ender 

# getters
    def getNome(self):
        return self.nome
    
    def getEnder(self):
        return self.ender