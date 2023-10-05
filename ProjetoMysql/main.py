from Class.Vendas import vendas

venda = vendas('localhost','root','chuvachu','pythoncourse')





# Multi-frame tkinter application v2.3
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.id = None
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Listar vendas",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Adcionar vendas",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Listando todas as vendas: ").pack(side="top", fill="x", pady=10)
        v = venda.listarTudo()
        for vendas in v:
            tk.Label(self,text=f'id: {vendas["idVendas"]}//Nome: {vendas["nome_produto"]}//Preço: {vendas["valor_produto"]}').pack()
            tk.Button(self, text="Deletar",
                  command=lambda: deletar(vendas["idVendas"])).pack()
            tk.Button(self, text="editar",
                  command=lambda: master.switch_frame(PageThree)).pack()

        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
def inserir(nome,preco,inserido):
    print('ola')
    if(nome != None and preco != None):
        venda.inserirVenda(nome=nome,valor=preco)
        inserido['text'] = 'Inserido'
        app.switch_frame(StartPage)


def deletar(id):
    venda.deletaVenda(id)
    app.switch_frame(PageOne)

    
class PageTwo(tk.Frame):
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
                  command=lambda: inserir(nome.get(),preco.get(),inserido)).pack()
        inserido = tk.Label(self, text="Ainda não inserido")
        inserido.pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text=f"O id é : {master.id}").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    venda.fecharConn()