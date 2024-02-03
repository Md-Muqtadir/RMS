from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

class reportclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+70")
        self.root.config(bg="white")  # Set the background color to white
        self.root.focus_force()

         #====title
        title = Label(self.root, text="View Student Results", 
                      
                      font=("goudy old style", 20, BOLD), bg="orange", fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)  # Placing title label horizontally
        #Search====
        self.var_search=StringVar()
        lbl_select=Label(self.root,text="Search by Rollno.",font=("goudy old style",15,BOLD),bg="white")
        lbl_select.place(x=300,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_search.place(x=500,y=100)
        btn_search = Button(self.root, text='Search', font=("goudy old style", 12, BOLD), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=750, y=100, width=100, height=35)
        btn_clear=Button(self.root,text='Clear',font=("times new roman",15,BOLD),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear)
        btn_clear.place(x=870,y=100,width=100,height=35)
        btn_delete=Button(self.root,text='Delete',font=("times new roman",15,BOLD),fg="white",bg="red",activebackground="red",cursor="hand2",command=self.delete)
        btn_delete.place(x=500,y=350,width=150,height=35)
        btn_pdf=Button(self.root,text='Share',font=("times new roman",15,BOLD),fg="white",bg="green",cursor="hand2")
        btn_pdf.place(x=750,y=350,width=150,height=35)
        
        #Result Labels=======
        lbl_rollno=Label(self.root,text="RollNo",font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        lbl_rollno.place(x=150,y=200,width=150,height=50)

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        lbl_name.place(x=300,y=200,width=150,height=50)

        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        lbl_course.place(x=450,y=200,width=150,height=50)

        lbl_cie=Label(self.root,text="CIE Marks",font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        lbl_cie.place(x=600,y=200,width=150,height=50)

        lbl_total=Label(self.root,text="Total Marks",font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        lbl_total.place(x=750,y=200,width=150,height=50)

        lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        lbl_percentage.place(x=900,y=200,width=150,height=50)
    
        self.rollno=Label(self.root,font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        self.rollno.place(x=150,y=250,width=150,height=50)

        self.name=Label(self.root,font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=250,width=150,height=50)

        self.course=Label(self.root,font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=250,width=150,height=50)

        self.cie=Label(self.root,font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        self.cie.place(x=600,y=250,width=150,height=50)

        self.total=Label(self.root,font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        self.total.place(x=750,y=250,width=150,height=50)

        self.percentage=Label(self.root,font=("goudy old style",15,BOLD),bg="white",bd=2,relief=GROOVE)
        self.percentage.place(x=900,y=250,width=150,height=50)
    
    
    
    
    
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Please Enter RollNo", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE Rollno=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row is not None:
                    if len(row) >= 6:
                        self.rollno.config(text=row[0])
                        self.name.config(text=row[1])
                        self.course.config(text=row[2])
                        self.cie.config(text=row[3])
                        self.total.config(text=row[4])
                        self.percentage.config(text=row[5])
                    else:
                        messagebox.showerror("Error", "Incomplete Data Returned", parent=self.root)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def clear(self):
        self.rollno.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.cie.config(text="")
        self.total.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")
    

    def delete(self):   
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Please Enter RollNo", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rollno=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("ERROR", "Please Enter Correct RollNo", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM result WHERE rollno=?", (self.var_search.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted", "Result deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



root = Tk()
obj = reportclass(root)
root.mainloop()
