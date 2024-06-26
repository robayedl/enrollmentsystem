"""
READ ME
    Data stored in format --> 977834,Asim Santos,asimsantos@gmail.com,mypassword

    To use the functions from this class::
        # Import this the Database class from the database.py file
        from database import Database
        # Create an instance of the class
        db = Database()

        ### CRUD functions
        # To add a student
        db.add_student(email, password, name)
        # To change password
        db.update_password('332797', 'mypass2')
        # To find a student by id
        db.get_student_by_id('977834')
        # To view all students
        db.get_all_students()
        # To remove a student by id
        db.delete_student('332797')
        To remove all students
        db.clear_students_data()

        ### Subject operations
        # To add a subject
        set_subjects(student_id, subject_id, subject_name)
        # To display all Subject list by student ID
        get_subjects(student_id)
        # To remove a subject from the student's data
        remove_subject(student_id, subject_id)

"""

from utils import Utils

class Database:
    def __init__(self, filename='students.data'):
        self.filename = filename
        # Try opening the data file to see if it exists
        try:
            open(self.filename, 'r').close()  
        # If the file does not exist, this creates a new file
        except FileNotFoundError:
            open(self.filename, 'w').close() 
    
    # checked
    # Adds a new student to the database with a unique six-digit ID 
    def add_student(self, studentID, name, email, password):
        try:
            with open(self.filename, 'a') as file:
                file.write(f"{studentID},{name},{email},{password},\n")
        except Exception as e:
            print("Error:", e)


    # checked
    # Gets all students in the database.
    def get_all_students(self):
        try:
            students = []
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    if len(parts) < 4:
                        continue
                    student = {
                        'id': parts[0],
                        'name': parts[1],
                        'email': parts[2],
                        'password': parts[3],
                        'subjects': {item.split(':')[0]: {'name': item.split(':')[1], 'marks': int(item.split(':')[2])} for item in parts[4].split(';') if item}
                    }
                    students.append(student)
            return students
        except Exception as e:
            print("Error:", e)
    

    # Gets a student by ID.
    def get_student_by_id(self, student_id):
        try:
            students = self.get_all_students()
            for student in students:
                if student['id'] == student_id:
                    return student
            return None
        except Exception as e:
            print("Error:", e)


    # Deletes a student from the database.
    def delete_student(self, student_id):
        try: 
            students = self.get_all_students()
            with open(self.filename, 'w') as file:
                for student in students:
                    if student['id'] != student_id:
                        self.write_student(file, student)
            return len(students) > len(self.get_all_students())
        except Exception as e:
            print("Error:", e)

    # Deletes all student from the database.
    def clear_students_data(self):
        try:
            open(self.filename, 'w').close()
        except Exception as e:
            print("Error:", e)

    # need to test
    # Updates an existing student's password.
    def update_password(self, student_id, new_pw):
        try:
            students = self.get_all_students()
            updated = False
            with open(self.filename, 'w') as file:
                for student in students:
                    if student['id'] == student_id:
                        student['password'] = new_pw
                        updated = True
                    self.write_student(file, student)
            return updated
        except Exception as e:
            print("Error:", e)
                    
    # Adds subjects to the student's records
    def set_subjects(self, student_id, subject_id, subject_name, marks):
        students = self.get_all_students()
        updated = False
        with open(self.filename, 'w') as file:
            for student in students:
                if student['id'] == student_id:
                    student['subjects'][subject_id] = {'name': subject_name, 'marks': marks}
                    updated = True
                self.write_student(file, student)
        return updated
    
    # Gets all the subjects a student is enrolled to
    def get_subjects(self, student_id):
        try:
            student = self.get_student_by_id(student_id)
            return student['subjects'] if student else None
        except Exception as e:
            print("Error:", e)

    # Removes a subject(by ID) from the student's records
    def remove_subject(self, student_id, subject_id):
        try:
            students = self.get_all_students()
            updated = False
            with open(self.filename, 'w') as file:
                for student in students:
                    if student['id'] == student_id and subject_id in student['subjects']:
                        del student['subjects'][subject_id]
                        updated = True
                    self.write_student(file, student)
            return updated
        except Exception as e:
            print("Error:", e)

    # Helper function to write into the student.data in a uniform layout
    def write_student(self, file, student):
        subjects_str = ';'.join(f"{key}:{value['name']}:{value['marks']}" for key, value in student['subjects'].items())
        file.write(f"{student['id']},{student['name']},{student['email']},{student['password']},{subjects_str}\n")


# Testing
# db = Database()

# db.add_student('asimsantos@gmail.com', 'mypass', 'Asim Santos')
# db.add_student('teststu@gmail.com', 'testpass', 'Test Student')

# db.update_password('110571', 'asimsantos')

# db.delete_student('861984')

# db.clear_students_data()

# print(db.get_student_by_id('110571'))

# print(db.get_subjects('957916'))

# print(db.get_all_students())

# db.set_subjects('110571','501','Maths',90)
# db.set_subjects('853160','732','Science',99)