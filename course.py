from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()


        # ========TITLE========
        title = Label(self.root, text="Manage Course Details", font=("times new roman", 25, "bold"), bg="#033e3e", fg="white").place(x=10, y=15, width=1180, height=35)

        # =========widgets========
        lbl_course_name = Label(self.root, text="Course Name", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_fee = Label(self.root, text="Fee", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("times new roman", 15, "bold"), bg="white").place(x=10, y=180)


        # ========Entry Fields========
        self.txt_course_name = Entry(self.root, font=("times new roman", 15), bg="lightyellow")
        self.txt_course_name.place(x=150, y=60, width=200, height=25)

        self.txt_duration = Entry(self.root, font=("times new roman", 15), bg="lightyellow").place(x=150, y=100, width=200, height=25)

        self.txt_fee = Entry(self.root, font=("times new roman", 15), bg="lightyellow").place(x=150, y=140, width=200, height=25)

        self.txt_description = Text(self.root, font=("times new roman", 15), bg="lightyellow").place(x=150, y=180, width=400, height=100)


        # ========Buttons========
        self.btn_add = Button(self.root, text="Save", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=150, y=350, width=110, height=35)
        self.btn_update = Button(self.root, text="Update", font=("times new roman", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2").place(x=270, y=350, width=110, height=35)
        self.btn_delete = Button(self.root, text="Delete", font=("times new roman", 15, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=390, y=350, width=110, height=35)
        self.btn_clear = Button(self.root, text="Clear", font=("times new roman", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2").place(x=510, y=350, width=110, height=35)


        # ======Search panael========
        lbl_search = Label(self.root, text="Search Course", font=("times new roman", 15, "bold"), bg="white").place(x=700, y=60)
        self.txt_search = Entry(self.root, font=("times new roman", 15), bg="lightyellow")
        self.txt_search.place(x=850, y=60, width=200, height= 25)
        self.btn_search = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=1050, y=60, width=100, height=25)

        # ======Course Content========

        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        self.C_Frame_title = Label(self.C_Frame, text="Course Details", font=("times new roman", 20, "bold"), bg="#033e3e", fg="white")
        self.C_Frame_title.pack(fill=X)



        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("CourseName", "Duration", "Fee", "Description"), show="headings")
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.CourseTable.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.config(command=self.CourseTable.yview)
        scrollx.config(command=self.CourseTable.xview)
        self.CourseTable.heading("CourseName", text="Course Name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable.heading("Fee", text="Fee")
        self.CourseTable.heading("Description", text="Description")
        self.CourseTable["displaycolumns"] = ("CourseName", "Duration", "Fee", "Description")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("CourseName", width=120)
        self.CourseTable.column("Duration", width=100)
        self.CourseTable.column("Fee", width=100)
        self.CourseTable.column("Description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)



if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()