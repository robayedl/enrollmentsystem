from database import Database
from utils import Utils
from student import Student
class Admin:
    def __init__(self):
        self.db = Database()
        self.stu = Student()

    #checked
    def viewAllStudents(self):
        try:
            students = self.db.get_all_students()
            if students:
                for student in students:
                    print('    '+student['name']+' :: '+student['id']+' --> EMAIL: '+student['email'])
            else:
                print('        < Nothing to Display >')
        except Exception as e:
            print("Error: {e}")

    #checked
    def groupStudentsByGrade(self):
        try:
            students = self.db.get_all_students()
            if not students:                
                print('        < Nothing to Display >')
                return
            students_by_grade = {}
            for student in students:
                total_marks = sum(subject['marks'] for subject in student['subjects'].values())
                num_subjects = len(student['subjects'])
                if num_subjects==0:
                    continue
                average_marks = total_marks / num_subjects
                grade = self.stu.getGrade(average_marks)
                if grade not in students_by_grade:
                    students_by_grade[grade] = []
                students_by_grade[grade].append(student)
            grade_order = ["HD", "D", "C", "P", "Z"]
            for grade in grade_order:
                if grade in students_by_grade:
                    print('    '+grade,end=' --> [')
                    student_list = []
                    for student in students_by_grade[grade]:
                        average_marks = sum(subject['marks'] for subject in student['subjects'].values()) / len(student['subjects'])
                        student_list.append(f"{student['name']} :: {student['id']} --> GRADE: {grade} - MARK: {average_marks}")
                    print(', '.join(student_list), end='')
                    print(']')
        except Exception as e:
            print(f"Error: {e}")


    #checked
    def partitionStudentsByPassFail(self):
        try:
            students = self.db.get_all_students()
            pass_students = []
            fail_students = []            
            for student in students:
                total_marks = sum(subject['marks'] for subject in student['subjects'].values())
                num_subjects = len(student['subjects'])
                if num_subjects==0:
                    continue
                average_marks = total_marks / num_subjects
                grade = self.stu.getGrade(average_marks)                
                if grade == "Z":
                    fail_students.append(student)
                else:
                    pass_students.append(student)
            
            print('    FAIL --> [', end='')
            for i, student in enumerate(fail_students):
                average_marks = sum(subject['marks'] for subject in student['subjects'].values()) / len(student['subjects'])
                print(f"{student['name']} :: {student['id']} --> GRADE: Z - MARK: {average_marks}", end='')
                if i < len(fail_students) - 1:
                    print(', ', end='')
            print(']')

            # Print Pass students
            print('    PASS --> [', end='')
            for i, student in enumerate(pass_students):
                average_marks = sum(subject['marks'] for subject in student['subjects'].values()) / len(student['subjects'])
                grade = self.stu.getGrade(average_marks)
                print(f"{student['name']} :: {student['id']} --> GRADE: {grade} - MARK: {average_marks}", end='')
                if i < len(pass_students) - 1:
                    print(', ', end='')
            print(']')
        
        except Exception as e:
            print(f"Error: {e}")\

    #checked
    def removeStudent(self):
        try:
            id= input('    Remove by ID: ')
            flag=self.db.delete_student(id)
            if flag:
                Utils.print_yellow(f'    Removing Student {id} Account')
            else:
                Utils.print_red(f'    Student {id} does not exist')
        except Exception as e:
            print(f"Error: {e}")

    def clearAllData(self):
        try:
            confirmation = input("\033[91m    Are you sure you want to clear the database (Y)ES/(N)O: \033[0m")
            if confirmation.lower() == 'y':
                self.db.clear_students_data()
                Utils.print_yellow('    Student data cleared')
        except Exception as e:
            print(f"Error: {e}")

            

# db = Database()
# admin = Admin()
# admin.viewAllStudents()
# admin.groupStudentsByGrade()
# admin.partitionStudentsByPassFail()
# admin.removeStudent()
# admin.clearAllData()
