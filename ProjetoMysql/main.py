from Class.Vendas import vendas
import tkinter as tk
venda = vendas('localhost','root','chuvachu','pythoncourse')


def inserir(nome,preco):
    print('ola')
    if(nome != None and preco != None):
        venda.inserirVenda(nome=nome,valor=preco)
        app.switch_frame(MainMenu)


def deletar(id):
    venda.deletaVenda(id)
    app.switch_frame(List)
    

def editar(id,master):
    master.id = id
    app.switch_frame(Edit)


def atualizar(id,alterar,valor = ''):
    if id != None and alterar != None and valor != None:
        if alterar == 'nome_produto' or alterar == 'valor_produto' and valor.isalpha() == False:
            venda.alteraValor(id,alterar,valor)
    app.switch_frame(List)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.id = None
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Listar vendas",
                  command=lambda: master.switch_frame(List)).pack()
        tk.Button(self, text="Adcionar vendas",
                  command=lambda: master.switch_frame(Add)).pack()

class List(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Listando todas as vendas: ").pack(side="top", fill="x", pady=10)
        v = venda.listarTudo()
        for vendas in v:
            tk.Label(self, text=f'id: {vendas["idVendas"]}//Nome: {vendas["nome_produto"]}//Preço: {vendas["valor_produto"]}').pack()
            tk.Button(self, text="Deletar",
                  command=lambda idVenda=vendas["idVendas"]: deletar(idVenda)).pack()
            tk.Button(self, text="editar",
                  command=lambda idVenda=vendas["idVendas"]: editar(idVenda,master)).pack()

        tk.Button(self, text="Voltar ao menu principal",
                  command=lambda: master.switch_frame(MainMenu)).pack()
    
class Add(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Inserir uma nova venda").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Nome").pack(side="top", fill="x", pady=10)
        nome = tk.Entry(self)
        nome.pack()
        tk.Label(self, text="Preco").pack(side="top", fill="x", pady=10)
        preco = tk.Entry(self)
        preco.pack()
        tk.Button(self, text="Inserir",
                  command=lambda: inserir(nome.get(),preco.get())).pack()
        tk.Button(self, text="Voltar ao menu principal",
                  command=lambda: master.switch_frame(MainMenu)).pack()

class Edit(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=f"O id é : {master.id}").pack(side="top", fill="x", pady=10)
        tk.Label(self, text=f"O que deseja alterar?[nome_produto/valor_produto]: ").pack(side="top", fill="x")
        alterar = tk.Entry(self)
        alterar.pack(side="top", pady=10)
        tk.Label(self, text=f"qual o novo valor?").pack(side="top", fill="x")
        valor = tk.Entry(self)
        valor.pack(side="top", pady=10)
        tk.Button(self, text="Atualizar",
                  command=lambda: atualizar(master.id,alterar.get(),valor.get())).pack(side="top")
        tk.Button(self, text="Voltar ao menu principal",
                  command=lambda: master.switch_frame(MainMenu)).pack(side="top")

if __name__ == "__main__":
    app = App()
    app.geometry("500x281")
    app.mainloop()
    venda.fecharConn()