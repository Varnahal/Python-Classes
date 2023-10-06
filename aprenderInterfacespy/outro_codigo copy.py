# Multi-frame tkinter application v2.3
import tkinter as tk
from aprenderInterfacespy.login_page.login_page import login

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
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
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self,text='Login',bg='#333333',fg='#ffffff',font=('arial',30))
        usarname_label = tk.Label(self,text='Username',bg='#333333',fg='#ffffff',font=('arial',16))
        Username_entry = tk.Entry(self,font=('arial',16))
        password_label = tk.Label(self,text='Password',bg='#333333',fg='#ffffff',font=('arial',16))
        password_entry = tk.Entry(self,show='*',font=('arial',16))
        login_button = tk.Button(self,text='Login',font=('arial',16),command= lambda :login(Username_entry,password_entry))


        label.grid(row=0,column=1,columnspan=2,sticky='news',pady=30)
        usarname_label.grid(row=1,column=0,pady=5)
        Username_entry.grid(row=1,column=1)
        password_label.grid(row=2,column=0,pady=5)
        password_entry.grid(row=2,column=1)
        login_button.grid(row=3,column=1,columnspan=2,pady=30)

        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).grid()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()