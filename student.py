from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import re


class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        


        # ========TITLE========
        title = Label(self.root, text="Manage Student Details", font=("times new roman", 20, "bold"), bg="#033e3e", fg="white").place(x=10, y=15, width=1180, height=30)

        # ========variables========
        self.var_roll_no = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_admission = StringVar()
        self.var_gender = StringVar()
        self.var_course = StringVar()
        self.var_address = StringVar()
        # ========Widgets========
        lbl_roll_no = Label(self.root, text="Roll No", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=60, width=120, height=30)
        lbl_date_of_birth = Label(self.root, text="D.O.B (DD/MM/YYYY)", font=("times new roman", 11, "bold"), bg="white").place(x=350, y=60, width=160, height=30)
        lbl_name = Label(self.root, text="Name", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=110, width=120, height=30)
        lbl_contact = Label(self.root, text="Contact", font=("times new roman", 13, "bold"), bg="white").place(x=350, y=110, width=150, height=30)
        lbl_email = Label(self.root, text="Email", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=160, width=120, height=30)
        lbl_admission = Label(self.root, text="Admission", font=("times new roman", 13, "bold"), bg="white").place(x=350, y=160, width=150, height=30)
        lbl_gender = Label(self.root, text="Gender", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=210, width=120, height=30)
        lbl_course = Label(self.root, text="Course", font=("times new roman", 13, "bold"), bg="white").place(x=350, y=210, width=150, height=30)
        lbl_address = Label(self.root, text="Address", font=("times new roman", 13, "bold"), bg="white").place(x=10, y=260, width=120, height=30)

        # ========Entry Fields========
        self.txt_roll_no = Entry(self.root, textvariable=self.var_roll_no, font=("times new roman", 13), bg="lightyellow")
        self.txt_roll_no.place(x=140, y=60, width=180, height=30)
        self.txt_date_of_birth = Entry(self.root, textvariable=self.var_date_of_birth, font=("times new roman", 13), bg="lightyellow")
        self.txt_date_of_birth.place(x=510, y=60, width=180, height=30)
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("times new roman", 13), bg="lightyellow")
        self.txt_name.place(x=140, y=110, width=180, height=30)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("times new roman", 13), bg="lightyellow")
        self.txt_contact.place(x=510, y=110, width=180, height=30)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("times new roman", 13), bg="lightyellow")
        self.txt_email.place(x=140, y=160, width=200, height=30)
        self.txt_admission = Entry(self.root, textvariable=self.var_admission, font=("times new roman", 13), bg="lightyellow")
        self.txt_admission.place(x=510, y=160, width=180, height=30)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select Gender", "Male", "Female", "Other"), font=("times new roman", 13), background="lightyellow", state="readonly", justify=CENTER)
        self.txt_gender.place(x=140, y=210, width=200, height=30)
        self.txt_gender.current(0)
        self.course_list = []
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=("times new roman", 13), background="lightyellow", state="readonly", justify=CENTER)
        self.txt_course.place(x=510, y=210, width=180, height=30)
        self.txt_address = Text(self.root, font=("times new roman", 13), bg="lightyellow", wrap=WORD)
        self.txt_address.place(x=140, y=260, width=400, height=100)

        # ========Buttons========
        self.btn_add = Button(self.root, text="Save", command=self.add_student, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=140, y=380, width=110, height=35)
        self.btn_update = Button(self.root, text="Update", command=self.update_student, font=("times new roman", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2").place(x=260, y=380, width=110, height=35)
        self.btn_delete = Button(self.root, text="Delete", command=self.delete_student, font=("times new roman", 15, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=380, y=380, width=110, height=35)
        self.btn_clear = Button(self.root, text="Clear", command=self.clear_student, font=("times new roman", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2").place(x=500, y=380, width=110, height=35)

        # ======Search panel========
        lbl_search = Label(self.root, text="Search Student", font=("times new roman", 13, "bold"), bg="white").place(x=720, y=60)
        self.txt_search = Entry(self.root, font=("times new roman", 13), bg="lightyellow")
        self.txt_search.place(x=850, y=60, width=180, height=25)
        self.btn_search = Button(self.root, text="Search", command=self.search_student, font=("times new roman", 13, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=1040, y=60, width=80, height=25)

        # ======Student Content========
        self.S_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.S_Frame.place(x=720, y=100, width=470, height=340)

        self.S_Frame_title = Label(self.S_Frame, text="Student Details", font=("times new roman", 20, "bold"), bg="#033e3e", fg="white")
        self.S_Frame_title.pack(fill=X)

        self.StudentTable = ttk.Treeview(self.S_Frame, columns=("roll_no", "name", "email", "contact", "dob", "admission", "gender", "course", "address"), show="headings")
        scrolly = Scrollbar(self.S_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.S_Frame, orient=HORIZONTAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.StudentTable.configure(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.config(command=self.StudentTable.yview)
        scrollx.config(command=self.StudentTable.xview)
        
        self.StudentTable.heading("roll_no", text="Roll No")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("contact", text="Contact")
        self.StudentTable.heading("dob", text="DOB")
        self.StudentTable.heading("admission", text="Admission")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("course", text="Course")
        self.StudentTable.heading("address", text="Address")
        
        self.StudentTable["displaycolumns"] = ("roll_no", "name", "email", "contact", "dob", "admission", "gender", "course", "address")
        self.StudentTable["show"] = "headings"
        self.StudentTable.column("roll_no", width=80)
        self.StudentTable.column("name", width=100)
        self.StudentTable.column("email", width=120)
        self.StudentTable.column("contact", width=100)
        self.StudentTable.column("dob", width=100)
        self.StudentTable.column("admission", width=80)
        self.StudentTable.column("gender", width=70)
        self.StudentTable.column("course", width=100)
        self.StudentTable.column("address", width=120)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)
        self.fetch_courses()
        self.show_students()

    def show_students(self, event=None):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()

    def validate_email(self, email):
        """Validate email format using regex"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_contact(self, contact):
        """Validate contact number format (10-15 digits)"""
        pattern = r'^\d{10,15}$'
        return re.match(pattern, contact) is not None

    def validate_date_of_birth(self, dob):
        """Validate date of birth in DD/MM/YYYY format"""
        pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(pattern, dob) is not None

    def validate_roll_no(self, roll_no):
        """Validate roll number (alphanumeric characters only)"""
        pattern = r'^[a-zA-Z0-9]+$'
        return re.match(pattern, roll_no) is not None

    def validate_student_data(self):
        """Comprehensive validation of all student data"""
        errors = []
        
        # Check required fields
        if not self.var_roll_no.get().strip():
            errors.append("Roll number is required")
        elif not self.validate_roll_no(self.var_roll_no.get().strip()):
            errors.append("Roll number must contain only alphanumeric characters")
            
        if not self.var_name.get().strip():
            errors.append("Name is required")
            
        if not self.var_email.get().strip():
            errors.append("Email is required")
        elif not self.validate_email(self.var_email.get().strip()):
            errors.append("Please enter a valid email address")
            
        if not self.var_contact.get().strip():
            errors.append("Contact number is required")
        elif not self.validate_contact(self.var_contact.get().strip()):
            errors.append("Contact number must be 10-15 digits")
            
        if not self.var_date_of_birth.get().strip():
            errors.append("Date of birth is required")
        elif not self.validate_date_of_birth(self.var_date_of_birth.get().strip()):
            errors.append("Date of birth must be in DD/MM/YYYY format")
            
        if not self.var_admission.get().strip():
            errors.append("Admission date/year is required")
            
        if self.var_gender.get() == "Select Gender" or not self.var_gender.get():
            errors.append("Please select a gender")
            
        if not self.var_course.get() or self.var_course.get() == "Select Course":
            errors.append("Please select a course")
            
        return errors

    def fetch_courses(self):
        """Load available courses from database into dropdown"""
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT CourseName FROM course")
            courses = cur.fetchall()
            if courses:
                course_list = ["Select Course"] + [course[0] for course in courses]
            else:
                course_list = ["No courses available"]
            
            self.txt_course['values'] = course_list
            if len(course_list) > 0:
                self.txt_course.current(0)
                
        except Exception as e:
            messagebox.showerror("Error", f"Error loading courses: {str(e)}")
            self.txt_course['values'] = ["No courses available"]
            if len(self.txt_course['values']) > 0:
                self.txt_course.current(0)
        finally:
            conn.close()

    def add_student(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            # Validate all student data
            errors = self.validate_student_data()
            if errors:
                messagebox.showerror("Validation Error", "\n".join(errors), parent=self.root)
                return
            
            # Check if roll number already exists
            cur.execute("SELECT * FROM student WHERE roll_no=?", (self.var_roll_no.get().strip(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "This roll number already exists", parent=self.root)
                return
            
            # Insert new student record
            cur.execute("""INSERT INTO student 
                          (roll_no, name, email, contact, date_of_birth, admission, gender, course, address) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (self.var_roll_no.get().strip(),
                        self.var_name.get().strip(),
                        self.var_email.get().strip(),
                        self.var_contact.get().strip(),
                        self.var_date_of_birth.get().strip(),
                        self.var_admission.get().strip(),
                        self.var_gender.get(),
                        self.var_course.get(),
                        self.txt_address.get("1.0", END).strip()))
            
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully", parent=self.root)
            self.show_students()
            self.clear_student()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def update_student(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            # Validate all student data
            errors = self.validate_student_data()
            if errors:
                messagebox.showerror("Validation Error", "\n".join(errors), parent=self.root)
                return
            
            # Check if a student is selected
            if not self.var_roll_no.get().strip():
                messagebox.showerror("Error", "Please select a student from the list", parent=self.root)
                return
            
            # Check if the student exists in database
            cur.execute("SELECT * FROM student WHERE roll_no=?", (self.var_roll_no.get().strip(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Selected student not found in database", parent=self.root)
                return
            
            # Update student record
            cur.execute("""UPDATE student SET 
                          name=?, email=?, contact=?, date_of_birth=?, 
                          admission=?, gender=?, course=?, address=? 
                          WHERE roll_no=?""",
                       (self.var_name.get().strip(),
                        self.var_email.get().strip(),
                        self.var_contact.get().strip(),
                        self.var_date_of_birth.get().strip(),
                        self.var_admission.get().strip(),
                        self.var_gender.get(),
                        self.var_course.get(),
                        self.txt_address.get("1.0", END).strip(),
                        self.var_roll_no.get().strip()))
            
            conn.commit()
            messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
            self.show_students()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def delete_student(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            r = self.StudentTable.focus()
            content = self.StudentTable.item(r)
            row = content["values"]
            if not row:
                messagebox.showerror("Error", "Please select a student from the list", parent=self.root)
                return
            
            # Confirmation dialog
            result = messagebox.askyesno("Confirm Delete", 
                                       f"Are you sure you want to delete student {row[1]} (Roll No: {row[0]})?", 
                                       parent=self.root)
            if not result:
                return
            
            # Delete student record
            cur.execute("DELETE FROM student WHERE roll_no=?", (row[0],))
            conn.commit()
            messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
            self.show_students()
            self.clear_student()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def clear_student(self):
        self.var_roll_no.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_date_of_birth.set("")
        self.var_admission.set("")
        self.var_gender.set("Select Gender")
        self.var_course.set("Select Course")
        self.txt_address.delete("1.0", END)
        self.txt_search.delete(0, END)
        self.txt_roll_no.config(state='normal')
        self.txt_roll_no.focus()
        self.show_students()

    def search_student(self):
        conn = sqlite3.connect("rms.db")
        cur = conn.cursor()
        try:
            search_term = self.txt_search.get().strip()
            if not search_term:
                messagebox.showerror("Error", "Please enter a search term", parent=self.root)
                return
            
            # Search by name or roll number
            cur.execute("""SELECT * FROM student 
                          WHERE name LIKE ? OR roll_no LIKE ?""", 
                       ('%' + search_term + '%', '%' + search_term + '%'))
            rows = cur.fetchall()
            
            # Update table with search results
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert("", END, values=row)
                
            if not rows:
                messagebox.showinfo("Search Results", "No students found matching your search criteria", parent=self.root)
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
            conn.close()

    def get_data(self, event=None):
        self.txt_roll_no.config(state='readonly')
        r = self.StudentTable.focus()
        content = self.StudentTable.item(r)
        row = content["values"]
        if row:
            self.var_roll_no.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_contact.set(row[3])
            self.var_date_of_birth.set(row[4])
            self.var_admission.set(row[5])
            self.var_gender.set(row[6])
            self.var_course.set(row[7])
            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[8] if len(row) > 8 else "")





if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()