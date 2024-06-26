import tkinter as tk
from tkinter import messagebox, font
from database import Database
import random

# Hardcoded list of all subjects
available_subjects = {
    '501': 'Mathematics',
    '401': 'Science',
    '390': 'Computer Science',
    '302': 'History',
    '303': 'Geography'
}

class GUIUniApp:
    def __init__(self, master, db):
        self.master = master
        self.db = db  # Database class instance
        self.master.title("GUIUniApp - Login")
        self.master.geometry("500x500")
        self.master.configure(bg='#607b8d')

        # Styling
        self.heading_font = font.Font(size=16, weight='bold')
        self.standard_font = font.Font(size=12)

        # Initialize Login Frame
        self.frame_login = tk.Frame(self.master, bg='light blue')
        self.frame_login.pack(fill=tk.BOTH, expand=True)

        # Login Widgets
        tk.Label(self.frame_login, text="Login to student account", font=self.heading_font, bg='light blue').pack()
        tk.Label(self.frame_login, text="Email:", font=self.standard_font, bg='light blue').pack()
        self.email_entry = tk.Entry(self.frame_login, font=self.standard_font)
        self.email_entry.pack(padx=20, pady=10)
        tk.Label(self.frame_login, text="Password:", font=self.standard_font, bg='light blue').pack()
        self.password_entry = tk.Entry(self.frame_login, font=self.standard_font, show="*")
        self.password_entry.pack(padx=20, pady=10)
        self.login_button = tk.Button(self.frame_login, text="Login", font=self.standard_font, command=self.login)
        self.login_button.pack(pady=20)

        self.enrollment_window = None

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Email and password cannot be empty.")
            return
        
        students = self.db.get_all_students()
        student = next((s for s in students if s['email'] == email and s['password'] == password), None)
        if student:
            self.student_id = student['id']
            self.open_enrollment_window()
        else:
            messagebox.showerror("Error", "Invalid credentials or account does not exist.")

    def open_enrollment_window(self):
        self.master.withdraw()  # Hide the main window
        self.enrollment_window = tk.Toplevel(self.master)
        self.enrollment_window.title("Enrollment")
        self.enrollment_window.geometry("600x600")
        self.enrollment_window.configure(bg='light green')

        tk.Label(self.enrollment_window, text="Currently Enrolled", font=self.heading_font, bg='light green').pack()
        self.current_subjects_listbox = tk.Listbox(self.enrollment_window, font=self.standard_font)
        self.current_subjects_listbox.pack(padx=20, pady=10)

        tk.Label(self.enrollment_window, text="Available Subjects", font=self.heading_font, bg='light green').pack()
        self.subject_listbox = tk.Listbox(self.enrollment_window, font=self.standard_font)
        self.subject_listbox.pack(padx=20, pady=10)

        self.enroll_button = tk.Button(self.enrollment_window, text="Enroll", font=self.standard_font, command=self.enroll_subject)
        self.enroll_button.pack(side=tk.LEFT, padx=10)

        self.logout_button = tk.Button(self.enrollment_window, text="Logout", font=self.standard_font, command=self.logout)
        self.logout_button.pack(side=tk.RIGHT, padx=10)

        self.update_subject_listboxes()

    def logout(self):
        self.enrollment_window.destroy()  # Close the enrollment window
        self.master.deiconify()  # Show the main window again
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def update_subject_listboxes(self):
        self.current_subjects_listbox.delete(0, tk.END)
        self.subject_listbox.delete(0, tk.END)
        subjects = self.db.get_subjects(self.student_id)

        for sub_id, details in subjects.items():
            self.current_subjects_listbox.insert(tk.END, f"{sub_id} - {details['name']}")

        for sub_id, sub_name in available_subjects.items():
            if sub_id not in subjects:
                self.subject_listbox.insert(tk.END, f"{sub_id} - {sub_name}")

    def enroll_subject(self):
        selection = self.subject_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No subject selected.")
            return
        
        subject_id, subject_name = self.subject_listbox.get(selection[0]).split(' - ')
        subjects = self.db.get_subjects(self.student_id)
        if len(subjects) >= 4:
            messagebox.showerror("Error", "Cannot enroll in more than 4 subjects.")
        else:
            self.db.set_subjects(self.student_id, subject_id, subject_name, random.randint(0, 100))
            messagebox.showinfo("Success", f"Enrolled in {subject_name}.")
            self.update_subject_listboxes()

if __name__ == "__main__":
    db = Database('students.data')
    root = tk.Tk()
    app = GUIUniApp(root, db)
    root.mainloop()