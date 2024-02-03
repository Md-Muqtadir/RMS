from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

class resultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+70")
        self.root.config(bg="white")  # Set the background color to white
        self.root.focus_force()

         #====title
        title = Label(self.root, text="Add Student Results", 
                      
                      font=("goudy old style", 20, BOLD), bg="orange", fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)  # Placing title label horizontally

        #Variables 
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_cie=StringVar()
        self.var_total=StringVar()
        self.roll_list=[]
        self.fetch_student()
        
        #widgets=====
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,BOLD),bg="white")
        lbl_select.place(x=50,y=100)
        
        
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,BOLD),bg="white")
        lbl_name.place(x=50,y=160)

        lbl_course =Label(self.root,text="Course ",font=("goudy old style",15,BOLD),bg="white")
        lbl_course.place(x=50,y=220)

        lbl_marks=Label(self.root,text="CIE marks",font=("goudy old style",15,BOLD),bg="white")
        lbl_marks.place(x=50,y=280)

        lbl_total=Label(self.root,text="Total Marks",font=("goudy old style",15,BOLD),bg="white")
        lbl_total.place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_rollno,values=self.roll_list,font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_search = Button(self.root, text='Search', font=("goudy old style", 12, BOLD), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=500, y=100, width=100, height=30)  # Adjusted coordinates and button size
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, BOLD), bg="lightyellow",state='readonly')
        txt_name.place(x=280, y=160, width=320)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, BOLD), bg="lightyellow",state='readonly'   )
        txt_course.place(x=280, y=220, width=320)
        txt_marks = Entry(self.root, textvariable=self.var_cie, font=("goudy old style", 20, BOLD), bg="lightyellow")
        txt_marks.place(x=280, y=280, width=320)
        txt_total = Entry(self.root, textvariable=self.var_total, font=("goudy old style", 20, BOLD), bg="lightyellow")
        txt_total.place(x=280, y=340, width=320)

        #Buttons======
        btn_add=Button(self.root,text='Submit',font=("times new roman",15,BOLD),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add)
        btn_add.place(x=300,y=420,width=120,height=35)

        btn_clear=Button(self.root,text='Clear',font=("times new roman",15,BOLD),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear)
        btn_clear.place(x=430,y=420,width=120,height=35)
        
        #Image=====
        self.bg_img=Image.open("images/res.png")
        self.bg_img=self.bg_img.resize((500,300))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img)
        self.lbl_bg.place(x=630,y=100)

        #Fetching student details===========
    def fetch_student (self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                    cur.execute("SELECT rollno,name FROM  student")
                    rows = cur.fetchall()
                    
                    if len(rows)>0:
                        for row in rows:
                            self.roll_list.append (row[0])
                   
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name,course FROM student WHERE Rollno LIKE ? OR name LIKE ?", ('%' + self.var_rollno.get() + '%', '%' + self.var_rollno.get() + '%'))
            rows = cur.fetchall()
            
            if rows:
                # At least one record found, update the variables
                self.var_name.set(rows[0][0])  # Access the name from the first record
                self.var_course.set(rows[0][1])  # Access the course from the first record
            else:
                messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()== "":
                messagebox.showerror("ERROR", "Please select a student ", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE rollno=? and course=?", (self.var_rollno.get(),self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("ERROR", "Result  already present", parent=self.root)
                else:
                    per=(float(self.var_cie.get())*100/float(self.var_total.get()))
                    cur.execute("INSERT INTO result (rollno, name, course, marks,total,per) VALUES (?, ?, ?, ?, ?, ?)",
                                (self.var_rollno.get(),
                                self.var_name.get(),
                                self.var_course.get(),
                                self.var_cie.get(),
                                self.var_total.get(),
                                str(per)
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def clear(self):
            
            self.var_rollno.set("Select")
            self.var_name.set("")
            self.var_course.set("")
            self.var_cie.set("")
            self.var_total.set("")
            

root = Tk()
obj = resultclass(root)
root.mainloop()