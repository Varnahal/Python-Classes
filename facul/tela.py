from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="José")
texto.pack()

try:
    # Open the image using PIL
    img = Image.open(r"C:\Users\danie\Documents\GitHub\Python-Classes\facul\jose.png")
    img.thumbnail((300, 300))  # Resize the image if needed
    pic = ImageTk.PhotoImage(img)
    logo = Label(master=janelaPrincipal, image=pic)
    logo.pack()
except Exception as e:
    messagebox.showerror("Error", f"Error loading image: {e}")

botao = Button(master=janelaPrincipal, text='Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()
