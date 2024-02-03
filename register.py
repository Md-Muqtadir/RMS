from tkinter import *
from PIL import Image, ImageTk 
class Register:
    def __init__(self,root) :
        self.root=root 
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #BG IMG====

        self.bg=ImageTk.PhotoImage(file="images/reg.png")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

root=Tk()
obj=Register(root)
root.mainloop()
