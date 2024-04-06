from tkinter import *
from tkinter import ttk


def ATF():
    root.destroy()
    HPars_ATF.mainloop()

    def PARSING():
        pass

    class App1(Frame):
        def __init__(self, master1):
            super().__init__(self, master1)
            self.grid()
            self.ATF_PARSING_IMG = PhotoImage(file = "docs/IMG/ATF_PARSING.png")
            self.ATF_Run = Button(atf, image=self.ATF_PARSING_IMG, command=PARSING)
            self.ATF_Run.grid(row=1, column=1)
       

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.HPars_ATF_IMG = PhotoImage(file = "docs/IMG/HPars_ATF.png")
        self.atf_btn = ttk.Button(root, image=self.HPars_ATF_IMG, command=ATF)
        self.atf_btn.grid(column=2,row=1)

root = Tk()
root.title("HPars")
root.geometry("706x385") 
root.resizable(False, False) 
HPars = App(root)
HPars.mainloop()
atf = Tk()
atf.title("ATFbooru")
atf.geometry("706x385") 
atf.resizable(False, False) 
HPars_ATF = App_ATF(atf)

















