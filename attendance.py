from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk
import sqlite3
from tkinter import messagebox
#from PIL import ImageTk, Image

class attendanceclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+70")
        self.root.config(bg="white")  # Set the background color to white
        self.root.focus_force()

         #====title
        title = Label(self.root, text="MANAGE STUDENT ATTENDANCE", 
                      
                      font=("goudy old style", 20, BOLD), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)  # Placing title label horizontally

        #Labels=========
        lbl_Dept = Label(self.root, text="Department", font=("goudy old style", 20, BOLD), bg="white")
        lbl_Dept.place(x=10, y=60)

        lbl_yr = Label(self.root, text="Year", font=("goudy old style", 20, BOLD), bg="white")
        lbl_yr.place(x=200, y=60)

        lbl_Sem = Label(self.root, text="Semester", font=("goudy old style", 20, BOLD), bg="white")
        lbl_Sem.place(x=400, y=60)

        lbl_section = Label(self.root, text="Section", font=("goudy old style", 20, BOLD), bg="white")
        lbl_section.place(x=600, y=60)

        lbl_Course=Label(self.root,text="Courses ",font=("goudy old style",20,BOLD),bg="white")
        lbl_Course.place(x=800,y=60)


        lbl_classes = Label(self.root, text="Total Classes", font=("goudy old style", 20, BOLD), bg="white")
        lbl_classes.place(x=1000, y=60)



        #Variables========
        self.var_dept=StringVar()
        self.var_yr=StringVar()
        self.var_sem=StringVar()
        self.var_sec=StringVar()
        self.var_Course=StringVar()
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_present=StringVar()
        self.Course_list=[]
        self.stud_list=[]
        
        #Entry fields=======
        self.txt_dept=ttk.Combobox(self.root,textvariable=self.var_dept,values=("Select","CSE","CSM","AIML","CSD","ECE","EEE","CIVIL"),font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_dept.place(x=10, y=100, width=160)
        self.txt_dept.current(0)

        self.txt_yr=ttk.Combobox(self.root,textvariable=self.var_yr,values=("Select","Iˢᵗ", "IIⁿᵈ", "IIIʳᵈ", "IVᵗʰ"),font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_yr.place(x=200, y=100, width=160)
        self.txt_yr.current(0)

        self.txt_sem=ttk.Combobox(self.root,textvariable=self.var_sem,values=("Select","I", "II", "III", "IV","V","VI","VII","VIII"),font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_sem.place(x=400, y=100, width=160)
        self.txt_sem.current(0)

        self.txt_sec=ttk.Combobox(self.root,textvariable=self.var_sec,values=("Select","A","B","C"),font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_sec.place(x=600, y=100, width=160)
        self.txt_sec.current(0)

        self.fetch_course()
        self.txt_Course=ttk.Combobox(self.root,textvariable=self.var_Course,values=self.Course_list,font=("goudy old style",15,BOLD),state='readonly',justify=CENTER)
        self.txt_Course.place(x=800, y=100, width=160)
        self.txt_Course.set("Select")

        entry_total = Entry(self.root, font=("goudy old style", 15), bg="lightyellow")
        entry_total.place(x=1000, y=100, width=160)


         # Buttons
        btn_add = Button(self.root, text="Add Attendance", font=("goudy old style", 15, BOLD), bg="lightgreen", 
                         activebackground="lightgreen", cursor="hand2", command=self.add_attendance)
        btn_add.place(x=10, y=160, width=160, height=35)

        btn_view = Button(self.root, text="View Attendance", font=("goudy old style", 15, BOLD), bg="lightblue", 
                          activebackground="lightblue", cursor="hand2", command=self.view_attendance)
        btn_view.place(x=180, y=160, width=160, height=35)


         #Panel=======
         # Student Attendance Frame
        self.Student_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.Student_frame.place(x=10, y=210, width=1180, height=350)
        scrolly=Scrollbar(self.Student_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.Student_frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
       

        # Create a Treeview for displaying student attendance records               
        self.AttendanceTable = ttk.Treeview(self.Student_frame, columns=("rollno", "name", "class", "course_name", "days_present"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        self.AttendanceTable.heading("rollno", text="Roll No")
        self.AttendanceTable.heading("name", text="Name")
        self.AttendanceTable.heading("class", text="Class")
        self.AttendanceTable.heading("course_name", text="Subject")
        self.AttendanceTable.heading("days_present", text="Classes Present")
        self.AttendanceTable["show"] = "headings"
        self.AttendanceTable.column("rollno", width=100)
        self.AttendanceTable.column("name", width=200)
        self.AttendanceTable.column("class", width=100)
        self.AttendanceTable.column("course_name", width=200)
        self.AttendanceTable.column("days_present", width=100)
        scrollx.config(command=self.AttendanceTable.xview)
        scrolly.config(command=self.AttendanceTable.yview)

        self.AttendanceTable.pack(fill=BOTH, expand=1)


    def add_attendance(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get()== "":
                messagebox.showerror("ERROR", "Rollno  should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE dept=?,year=?,sem=?,sec=?,course=?", (self.var_rollno.get(),))
                row = cur.fetchall()
                if row is not None:
                    messagebox.showerror("ERROR", "Course ID already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO att(rollno,name, class,sub,present) VALUES (?, ?, ?, ?, ?)",
                                (self.var_rollno.get(),
                                self.var_name.get(),
                                self.var_sec.get(),
                                self.var_Course.get(),
                                self.var_present.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def view_attendance(self):
        # Add your code here to view attendance records from the database
        pass
    
    
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


                self.AttendanceTable.delete(*self.AttendanceTable.get_children())
                for row in rows:
                    self.AttendanceTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchallwwwww()

            if len(rows) > 0:
                for row in rows:
                    self.AttendanceTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
                cur.execute("SELECT roll, name, course,  FROM  student ")
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




        
if __name__ == "__main__":
    root = Tk()
    obj = attendanceclass(root)
    root.mainloop()
