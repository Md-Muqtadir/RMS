from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
import sqlite3
from tkinter import messagebox
#from PIL import ImageTk, Image

class courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+70")
        self.root.config(bg="white")  # Set the background color to white
        self.root.focus_force()

         #====title
        title = Label(self.root, text="MANAGE COURSE DETAILS", 
                      
                      font=("goudy old style", 20, BOLD), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)  # Placing title label horizontally
        
        
        #====Variables
        self.var_courseid=StringVar()
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_credits=StringVar()
        
        
        
        #=====widgets
        lbl_cid=Label(self.root,text="Course ID",font=("goudy old style",15,BOLD),bg="white")
        lbl_cid.place(x=10,y=60)
        
        
        lbl_name=Label(self.root,text="Course Name",font=("goudy old style",15,BOLD),bg="white")
        lbl_name.place(x=10,y=100)

        lbl_duration=Label(self.root,text="Course Duration",font=("goudy old style",15,BOLD),bg="white")
        lbl_duration.place(x=10,y=140)

        lbl_credits=Label(self.root,text="Course Credit",font=("goudy old style",15,BOLD),bg="white")
        lbl_credits.place(x=10,y=180)

        lbl_faculty=Label(self.root,text="Course Faculty ",font=("goudy old style",15,BOLD),bg="white")
        lbl_faculty.place(x=10,y=220)

        #======Entry fields
        self.txt_cid=Entry(self.root,textvariable=self.var_courseid,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_cid.place(x=170,y=60,width=200)

        
        self.txt_name=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_name.place(x=170,y=100,width=200)

        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_duration.place(x=170,y=140, width=200)

        txt_credits=Entry(self.root,textvariable=self.var_credits,font=("goudy old style",15,BOLD),bg="lightyellow")
        txt_credits.place(x=170,y=180,width=200)

        self.txt_faculty=Text(self.root,font=("goudy old style",15,BOLD),bg="lightyellow")
        self.txt_faculty.place(x=170,y=220,width=500,height=150)

        #===Buttons
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,BOLD),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,BOLD),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,BOLD),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,BOLD),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        # ===search panel
        self.var_search = StringVar()
        lbl_search_name = Label(self.root, text="Search Course Name", font=("goudy old style", 15, BOLD), bg="white")
        lbl_search_name.place(x=720, y=60)
        txt_Search_coursename = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, BOLD), bg="lightyellow")
        txt_Search_coursename.place(x=870, y=60, width=180)
        btn_search = Button(self.root, text='Search', font=("goudy old style", 12, BOLD), bg="#03a9f4", fg="white", cursor="hand2",command=self.search)
        btn_search.place(x=1055, y=60, width=100, height=30)  # Adjusted coordinates and button size

        #=====content
        self.C_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        self.CourseTable= ttk.Treeview(self.C_frame,columns=("cid","name","duration","credits","Faculty"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("credits",text="Credits")
        self.CourseTable.heading("Faculty",text="Faculty")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("credits",width=100)
        self.CourseTable.column("Faculty", width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=================================================
    def clear(self):
        self.show()
        self.var_courseid.set("")
        self.var_course.set("")
        self.var_duration.set("")
        self.var_credits.set("")
        self.var_search.set("")
        self.txt_faculty.delete('1.0',END)
        self.txt_cid.config(state=NORMAL)
    
    def delete(self):   
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_courseid.get() == "":
                messagebox.showerror("ERROR", "Course ID should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE cid=?", (self.var_courseid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("ERROR", "Please select a course from the list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM course WHERE cid=?", (self.var_courseid.get(),))
                        con.commit()
                        messagebox.showinfo("Deleted", "Course deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    
    def get_data(self,ev):
        self.txt_cid.config(state='readonly')
        self.txt_cid
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content=content["values"]
        #print(row)
        self.var_courseid.set(row[0])
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_credits.set(row[3])
        #self.var_course.set(row[4])
        self.txt_faculty.delete('1.0',END)
        self.txt_faculty.insert(END,row[4])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_courseid.get()== "":
                messagebox.showerror("ERROR", "Course ID  should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE cid=?", (self.var_courseid.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("ERROR", "Course ID already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (cid, name, duration, credits, faculty) VALUES (?, ?, ?, ?, ?)",
                                (self.var_courseid.get(),
                                self.var_course.get(),
                                self.var_duration.get(),
                                self.var_credits.get(),
                                self.txt_faculty.get("1.0", END)
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("ERROR", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE cid=?", (self.var_courseid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("ERROR", "Select a course from the list", parent=self.root)
                else:
                    cur.execute("UPDATE course SET name=?, duration=?, credits=?, faculty=? WHERE cid=?",
                                (
                                self.var_course.get(),
                                self.var_duration.get(),
                                self.var_credits.get(),
                                self.txt_faculty.get("1.0", END),
                                self.var_courseid.get()
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("SELECT * FROM  course ")
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("SELECT * FROM course WHERE cid LIKE ? OR name LIKE ?", ('%' + self.var_search.get() + '%', '%' + self.var_search.get() + '%'))
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



if __name__ == "__main__":
    root = Tk()
    obj = courseclass(root)
    root.mainloop()
