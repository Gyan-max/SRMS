from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

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

        # ========Variables========
        self.var_course_name = StringVar()
        self.var_duration = StringVar()
        self.var_fee = StringVar()
        # self.var_description = StringVar()


        # ========Entry Fields========
        self.txt_course_name = Entry(self.root, font=("times new roman", 15), bg="lightyellow", textvariable=self.var_course_name)
        self.txt_course_name.place(x=150, y=60, width=200, height=25)

        self.txt_duration = Entry(self.root, font=("times new roman", 15), bg="lightyellow", textvariable=self.var_duration)
        self.txt_duration.place(x=150, y=100, width=200, height=25)

        self.txt_fee = Entry(self.root, font=("times new roman", 15), bg="lightyellow", textvariable=self.var_fee)
        self.txt_fee.place(x=150, y=140, width=200, height=25)

        self.txt_description = Text(self.root, font=("times new roman", 15), bg="lightyellow", wrap=WORD)
        self.txt_description.place(x=150, y=180, width=400, height=100)


        # ========Buttons========
        self.btn_add = Button(self.root, text="Save",command=self.add_course, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=150, y=350, width=110, height=35)
        self.btn_update = Button(self.root, text="Update",command=self.update_course, font=("times new roman", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2").place(x=270, y=350, width=110, height=35)
        self.btn_delete = Button(self.root, text="Delete",command=self.delete_course, font=("times new roman", 15, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=390, y=350, width=110, height=35)
        self.btn_clear = Button(self.root, text="Clear",command=self.clear_course, font=("times new roman", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2").place(x=510, y=350, width=110, height=35)


        # ======Search panael========
        lbl_search = Label(self.root, text="Search Course", font=("times new roman", 15, "bold"), bg="white").place(x=700, y=60)
        self.txt_search = Entry(self.root, font=("times new roman", 15), bg="lightyellow")
        self.txt_search.place(x=850, y=60, width=200, height= 25)
        self.btn_search = Button(self.root, text="Search", command=self.search_course, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=1050, y=60, width=100, height=25)

        # ======Course Content========

        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        self.C_Frame_title = Label(self.C_Frame, text="Course Details", font=("times new roman", 20, "bold"), bg="#033e3e", fg="white")
        self.C_Frame_title.pack(fill=X)



        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "CourseName", "Duration", "Fee", "Description"), show="headings")
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.CourseTable.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.config(command=self.CourseTable.yview)
        scrollx.config(command=self.CourseTable.xview)
        self.CourseTable.heading("cid", text="ID")
        self.CourseTable.heading("CourseName", text="Course Name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable.heading("Fee", text="Fee")
        self.CourseTable.heading("Description", text="Description")
        self.CourseTable["displaycolumns"] = ("cid", "CourseName", "Duration", "Fee", "Description")
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("cid", width=50)
        self.CourseTable.column("CourseName", width=120)
        self.CourseTable.column("Duration", width=100)
        self.CourseTable.column("Fee", width=100)
        self.CourseTable.column("Description", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show_course()


    def clear_course(self):
        self.var_course_name.set("")
        self.var_duration.set("")
        self.var_fee.set("")
        self.txt_description.delete("1.0", END)
        self.txt_search.delete(0, END)
        self.txt_course_name.config(state='normal')
        self.txt_course_name.focus()
        self.show_course()

    def delete_course(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            r = self.CourseTable.focus()
            content = self.CourseTable.item(r)
            row = content["values"]
            if row == "":
                messagebox.showerror("Error", "Select Course from List", parent=self.root)
            else:
                cur.execute("DELETE FROM course WHERE CourseName=?", (row[1],))
                conn.commit()
                messagebox.showinfo("Success", "Course deleted successfully", parent=self.root)
                self.show_course()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()
    def get_data(self, event=None):
        self.txt_course_name.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        # print(row)  # Debugging line to check the row data
        self.var_course_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_fee.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])
    def add_course(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Please enter the course name", parent=self.root)
            else:
                cur.execute("select * from course where CourseName=?", (self.var_course_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This course already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (CourseName, Duration, Fee, Description) VALUES (?, ?, ?, ?)",
                                (self.var_course_name.get(), self.var_duration.get(), self.var_fee.get(), self.txt_description.get("1.0", END)))
                    conn.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show_course()

                    conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def update_course(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            if self.var_course_name.get() == "":
                messagebox.showerror("Error", "Please enter the course name", parent=self.root)
            else:
                cur.execute("select * from course where CourseName=?", (self.var_course_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Course from List", parent=self.root)
                else:
                    cur.execute("UPDATE course SET CourseName=?, Duration=?, Fee=?, Description=? WHERE CourseName=?",
                                (self.var_course_name.get(),
                                self.var_duration.get(), 
                                self.var_fee.get(), 
                                self.txt_description.get("1.0", END), 
                                self.var_course_name.get(),))
                    conn.commit()
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show_course()

                    conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def show_course(self, event=None):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()   

    def search_course(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            if self.txt_search.get() == "":
                messagebox.showerror("Error", "Please enter a course name to search", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE CourseName LIKE ?", ('%' + self.txt_search.get() + '%',))
                rows = cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert("", END, values=row)
                    
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()