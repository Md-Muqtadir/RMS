from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
import sqlite3
from tkinter import messagebox
#from PIL import ImageTk, Image

class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+70")
        self.root.config(bg="white")  # Set the background color to white
        self.root.focus_force()
        
        
 
         #====title
        title = Label(self.root, text="MANAGE STUDENT DETAILS", 
                      
                      font=("goudy old style", 20, BOLD), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)  # Placing title label horizontally
        
        
        #====Variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_Gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_department=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_State=StringVar()
        self.var_Course=StringVar()
        
        #=====widgets
        #======column1
        
        lbl_sid=Label(self.root,text="Student Roll No ",font=("goudy old style",15,BOLD),bg="white")
        lbl_sid.place(x=10,y=60)
        
        
        lbl_name=Label(self.root,text="Student Name",font=("goudy old style",15,BOLD),bg="white")
        lbl_name.place(x=10,y=100)

        lbl_email=Label(self.root,text="Parent's E-mail",font=("goudy old style",15,BOLD),bg="white")
        lbl_email.place(x=10,y=140)

        lbl_Gender=Label(self.root,text="Student Gender",font=("goudy old style",15,BOLD),bg="white")
        lbl_Gender.place(x=10,y=180)
        
        lbl_State=Label(self.root,text="State",font=("goudy old style",15,BOLD),bg="white")
        lbl_State.place(x=10,y=220)

        lbl_city=Label(self.root,text="City",font=("goudy old style",15,BOLD),bg="white")
        lbl_city.place(x=320,y=220)

        lbl_pin=Label(self.root,text="PIN",font=("goudy old style",15,BOLD),bg="white")
        lbl_pin.place(x=500,y=220)

        lbl_Address=Label(self.root,text="Student Address ",font=("goudy old style",15,BOLD),bg="white")
        lbl_Address.place(x=10,y=250)

        #======Entry fields 1
        self.txt_sid=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_sid.place(x=170,y=60,width=200)

        
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_name.place(x=170,y=100,width=200)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_email.place(x=170,y=140, width=200)
        
        self.txt_Gender=ttk.Combobox(self.root,textvariable=self.var_Gender,values=("Select","Male","Female","Others"),font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_Gender.place(x=170,y=180,width=200)
        self.txt_Gender.current(0)
        
        txt_State=Entry(self.root,textvariable=self.var_State,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_State.place(x=170,y=220, width=150)
        
        txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_city.place(x=380,y=220, width=100)

        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_pin.place(x=560,y=220, width=120)


        self.txt_Address=Text(self.root,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_Address.place(x=180,y=260,width=500,height=150)

        #=============Column 2
        self.lbl_dob=Label(self.root,text="D.O.B ",font=("goudy old style",15,BOLD),bg="white")
        self.lbl_dob.place(x=370,y=60)
        
        
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,BOLD),bg="white")
        lbl_contact.place(x=370,y=100)

        lbl_Department=Label(self.root,text="Department ",font=("goudy old style",15,BOLD),bg="white")
        lbl_Department.place(x=370,y=140)

        lbl_Course=Label(self.root,text="Courses ",font=("goudy old style",15,BOLD),bg="white")
        lbl_Course.place(x=370,y=180)

          #======Entry fields 2
        self.Course_list=[]
        #==========function call to update list
        self.fetch_course()
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_dob.place(x=490,y=60,width=200)

        
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_contact.place(x=490,y=100,width=200)

        txt_Department=Entry(self.root,textvariable=self.var_department,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_Department.place(x=490,y=140, width=200)

        self.txt_Course=ttk.Combobox(self.root,textvariable=self.var_Course,values=self.Course_list,font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_Course.place(x=490,y=180,width=200)
        self.txt_Course.set("Select")
        
        #===Buttons
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,BOLD),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=420,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,BOLD),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=420,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,BOLD),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=420,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,BOLD),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=420,width=110,height=40)

        # ===search panel
        self.var_search = StringVar()
        lbl_search_Rollno = Label(self.root, text="Search Rollno", font=("goudy old style", 15, BOLD), bg="white")
        lbl_search_Rollno.place(x=720, y=60)
        txt_Search_Rollno = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, BOLD), bg="lightyellow")
        txt_Search_Rollno.place(x=870, y=60, width=180)
        btn_search = Button(self.root, text='Search', font=("goudy old style", 12, BOLD), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1055, y=60, width=100, height=30)  # Adjusted coordinates and button size

        #=====content
        self.C_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        self.CourseTable= ttk.Treeview(self.C_frame,columns=("Rollno","name","email","Gender","dob","contact","Department","Course","State","city","pin","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        self.CourseTable.heading("Rollno",text="Rollno")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("Gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("Department",text="Department")
        self.CourseTable.heading("Course",text="Courses")
        self.CourseTable.heading("State",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("Address",text="Address")
       
        self.CourseTable["show"]='headings'
        self.CourseTable.column("Rollno",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100)
        self.CourseTable.column("Gender",width=100)
        self.CourseTable.column("dob", width=100)
        self.CourseTable.column("contact", width=100)
        self.CourseTable.column("Department", width=100)
        self.CourseTable.column("Course", width=100)
        self.CourseTable.column("State", width=100)
        self.CourseTable.column("city", width=100)
        self.CourseTable.column("pin", width=100)
        self.CourseTable.column("Address", width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#=================================================
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_Gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_department.set(""),
        self.var_Course.set("Select"),
        self.var_State.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.var_search.set(""),
        self.txt_Address.get("1.0", END)
   
   
    def delete(self):   
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("ERROR", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE Rollno=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("ERROR", "Please select a student from the list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM student WHERE Rollno=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted", "Student deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    
    def get_data(self, ev):
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

    # Check if row contains at least 12 elements
        if len(row) >= 12:
         self.var_roll.set(row[0])
         self.var_name.set(row[1])
         self.var_email.set(row[2])
         self.var_Gender.set(row[3])
         self.var_dob.set(row[4])
         self.var_contact.set(row[5])
         self.var_department.set(row[6])
         self.var_Course.set(row[7])
         self.var_State.set(row[8])
         self.var_city.set(row[9])
         self.var_pin.set(row[10])
         self.txt_Address.delete("1.0", END)
         self.txt_Address.insert(END, row[11])
        else:
            messagebox.showerror("Error", "Invalid row data", parent=self.root)

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get()== "":
                messagebox.showerror("ERROR", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE Rollno=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("ERROR", "Roll Number already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO student (Rollno,name,email,Gender,dob,contact,Department,Course,State,city,pin,Address ) VALUES (?, ?, ?, ?, ?, ?, ? , ? , ? , ? , ? , ? )",
                                (self.var_roll.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_Gender.get(),
                                self.var_dob.get(),
                                self.var_contact.get(),
                                self.var_department.get(),
                                self.var_Course.get(),
                                self.var_State.get(),
                                self.var_city.get(),
                                self.var_pin.get(),
                                self.txt_Address.get("1.0", END)
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("ERROR", "Roll Number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE Rollno=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("ERROR", "Select a Student from the list", parent=self.root)
                else:
                    cur.execute("UPDATE student SET name=?,email=?,Gender=?,dob=?,contact=?,Department=?,Course=?,State=?,city=?,pin=?,Address=? WHERE Rollno=?",
                                (
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_Gender.get(),
                                self.var_dob.get(),
                                self.var_contact.get(),
                                self.var_department.get(),
                                self.var_Course.get(),
                                self.var_State.get(),
                                self.var_city.get(),
                                self.var_pin.get(),
                                self.txt_Address.get("1.0", END),
                                self.var_roll.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Details updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("SELECT * FROM  student ")
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("SELECT name FROM  course ")
                rows = cur.fetchall()
                
                if len(rows)>0:
                    for row in rows:
                        self.Course_list.append (row[0])
                #print(v)


                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("SELECT * FROM student WHERE Rollno LIKE ? OR name LIKE ?", ('%' + self.var_search.get() + '%', '%' + self.var_search.get() + '%'))
                rows = cur.fetchall()
                if rows!= None:
                    self.CourseTable.delete(*self.CourseTable.get_children())
                    for row in rows:
                        self.CourseTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = studentclass(root)
    root.mainloop()
