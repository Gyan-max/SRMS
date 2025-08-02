from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")

        # ========ICON========

        self.logo = ImageTk.PhotoImage(file="images/logo_p.png")
        self.logo_label = Label(self.root, image=self.logo, bd=0, bg="white", fg="white")

        # ========TITLE========

        title = Label(self.root, text="Student Result Management System",padx=10, compound=LEFT, image=self.logo, bd=10, relief=GROOVE, font=("times new roman", 25, "bold"), bg="#033e3e", fg="white").place(x=0, y=0, relwidth=1, height=70)

        # =======MENU========

        M_Frame = LabelFrame(self.root, text="Menu", font = ("times new roman",15, "bold"), bd=5, relief=GROOVE, bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        btn_course = Button(M_Frame, text = "Courses", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white", bd=0, cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text = "Students", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white", bd=0, cursor="hand2").place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text = "Results", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white", bd=0, cursor="hand2").place(x=460, y=5, width=200, height=40)
        btn_student_result = Button(M_Frame, text = "View Student Results", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white", bd=0, cursor="hand2").place(x=680, y=5, width=200, height=40)
        btn_Logout = Button(M_Frame, text = "Logout", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white", bd=0, cursor="hand2").place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text = "Exit", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white", bd=0, cursor="hand2").place(x=1120, y=5, width=200, height=40)

        # ========CONTENT========

        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg = Label(self.root, image = self.bg_img).place(x=400, y=180, width=920, height=350)

        # ======update details=======

        self.lbl_course = Label(self.root, text = "Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief= RIDGE, bg="orange", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text = "Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief= RIDGE, bg="blue", fg="white")
        self.lbl_student.place(x=720, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text = "Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief= RIDGE, bg="green", fg="white")
        self.lbl_result.place(x=1040, y=530, width=300, height=100)

        

        # ========footer========

        footer = Label(self.root, text="SRMS - Student Result Management System", font=("times new roman", 15, "bold"), bg="#033e3e", fg="white")
        footer.place(x=0, y=650, relwidth=1, height=50)
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = RMS(root)
    root.mainloop()