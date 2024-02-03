from tkinter import *
from PIL import Image, ImageTk 
from tkinter.font import BOLD
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")  # Set the background color to white

        #===icon
        self.logo_dash = Image.open("images/logo_p.png")  # Open the image
        self.logo_dash = self.logo_dash.resize((50, 50))  # Resize the image
        self.logo_dash = ImageTk.PhotoImage(self.logo_dash)  # Convert to PhotoImage
        
        #====title
        title = Label(self.root, text="Student Result Management System (Faculty Login)", 
                      compound=LEFT, image=self.logo_dash,
                      font=("goudy old style", 20, BOLD), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)  # Placing title label horizontally
        
        #====Menu
        M_frame = Label(self.root, text="MENU",compound=LEFT, font=("times new roman", 15, BOLD), bg="blue", fg="white")
        M_frame.place(x=0, y=50, width=1350, height=40)  # Adjusted position and dimensions
        
        # Rectangular Frame with outline
        frame_course = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        frame_course.place(x=10, y=90, width=1340, height=80)  # Adjusted position and dimensions
        
        # Course Button
        btn_course = Button(frame_course, text="Attandance", font=("goudy old style", 15, BOLD), bg="#0b5377", fg="white", cursor="hand2")
        btn_course.place(x=20, y=5, width=200, height=60)  # Adjusted position and dimensions
        
        btn_student = Button(frame_course, text="CIE-1 Marks", font=("goudy old style", 15, BOLD), bg="#0b5377", fg="white", cursor="hand2")
        btn_student.place(x=240, y=5, width=200, height=60)
        
        btn_result = Button(frame_course, text="CIE-2 Marks", font=("goudy old style", 15, BOLD), bg="#0b5377", fg="white", cursor="hand2")
        btn_result.place(x=460, y=5, width=200, height=60)
        
        btn_view = Button(frame_course, text=" Generate PDF ", font=("goudy old style", 15, BOLD), bg="#0b5377", fg="white", cursor="hand2")
        btn_view.place(x=680, y=5, width=200, height=60)
        
        btn_logout = Button(frame_course, text="LOGOUT", font=("goudy old style", 15, BOLD), bg="#0b5377", fg="white", cursor="hand2")
        btn_logout.place(x=900, y=5, width=200, height=60)
        
        btn_exit = Button(frame_course, text="EXIT ", font=("goudy old style", 15, BOLD), bg="#0b5377", fg="white", cursor="hand2")
        btn_exit.place(x=1120, y=5, width=200, height=60)


        #==== content window
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img)
        self.lbl_bg.place(x=400,y=180,width=920,height=350)
        
        
        #====update details
        self.lbl_course=Label(self.root, text="Total Courses\n[ 0 ]",font=("goudy old style ", 20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        
        self.lbl_student=Label(self.root, text="Total Studnets\n[ 0 ]",font=("goudy old style ", 20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root, text="Total Result\n[ 0 ]",font=("goudy old style ", 20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        
        
        #====FOOTER
        footer = Label(self.root, text="SRMS-Student Result Management System Contact US for any queries  212173314",font=("goudy old style", 15), bg="#262626", fg="white")
        footer.pack(side=BOTTOM,fill=X)  # Placing title label horizontally
    
    
    


root=Tk()
obj=Register(root)
root.mainloop()
