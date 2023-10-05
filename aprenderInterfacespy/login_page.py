from tkinter import *
from tkinter import messagebox



def login(Username_entry,password_entry):
    username = 'varnahal'
    password = '12345'

    if Username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title='Logged successifuly',message='you are logged')
        return True
    
    messagebox.showerror(title='ERROR',message='Invalid credencials')
    return False





window = Tk()
window.title('Login Page')
window.geometry('500x300')
window.configure(bg='#333333')


frame = Frame(bg='#333333')

label = Label(frame,text='Login',bg='#333333',fg='#ffffff',font=('arial',30))
usarname_label = Label(frame,text='Username',bg='#333333',fg='#ffffff',font=('arial',16))
Username_entry = Entry(frame,font=('arial',16))
password_label = Label(frame,text='Password',bg='#333333',fg='#ffffff',font=('arial',16))
password_entry = Entry(frame,show='*',font=('arial',16))
login_button = Button(frame,text='Login',font=('arial',16),command=login)


label.grid(row=0,column=1,columnspan=2,sticky='news',pady=30)
usarname_label.grid(row=1,column=0,pady=5)
Username_entry.grid(row=1,column=1)
password_label.grid(row=2,column=0,pady=5)
password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=1,columnspan=2,pady=30)


frame.pack()


window.mainloop()
