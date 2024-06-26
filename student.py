from utils import Utils
from database import Database
from subjects import Subjects
import re
class Student:
    def __init__(self):
        self.db=Database()
        self.sub=Subjects()

    def studentMenu(self,id):
        db=Database()
        while(1):
            opStd= input("\033[94m        Student Course Menu (c/e/r/s/x): \033[0m")
            if opStd == 'c':
                self.changePassword(id)
            elif opStd == 'e':
                self.enrollSubject(id)
            elif opStd == 'r':
                self.removeSubject(id)
            elif opStd == 's':
                self.viewEnrolment(id)
            else:
                return 
                
            

    #checked
    def enrollSubject(self,id):
        try:
            self.sub.enroll_subject(id)
        except Exception as e:
            print("Error:", e)

    #checked
    def removeSubject(self,id):
        try:
            sID= input('        Remove subject by ID: ')
            self.sub.drop_subject(id,sID)
        except Exception as e:
            print("Error:", e)

    #checked
    def viewEnrolment(self,id):
        try:
            subjects=self.db.get_subjects(id)
            Utils.print_yellow('        Showing '+str(len(subjects))+' subjects')
            for subject_id, subject_info in subjects.items():
                marks = subject_info['marks']
                print('        [ Subject::'+subject_id+' -- marks = '+str(marks)+' -- grade =  '+self.getGrade(marks)+' ]')
        except Exception as e:
            print("Error:", e)

     
    #checked     
    def changePassword(self,id): 
        try:
            Utils.print_yellow('        Updating Password')
            while 1:
                newPassword = input("        New Password: ")
                if(self.validatePassword(newPassword)):
                    break
                else:
                    Utils.print_red('        Incorrect password format')
            while 1:
                conPassword = input("        Confirm Password: ")
                if(conPassword==newPassword):
                    break
                else:
                    Utils.print_red('        Password does not match - try again')
            self.db.update_password(id,newPassword)
        except Exception as e:
            print("Error:", e)

    # checked   
    def login(self):
        try:
            Utils.print_green('    Student Sign In')
            while 1:
                email = input("    Email: ")
                password = input("    Password: ")
                if self.validateEmail(email) and self.validatePassword(password):
                    Utils.print_yellow('    email and password formats acceptable')
                    break
                else:
                    Utils.print_red("    Incorrect email or password format")
            id=self.verifyCredential(email,password)
            if(id):
                self.studentMenu(id)
            else: 
                Utils.print_red('    Student does not exist')
                return
        except Exception as e:
            print("Error:", e)

    # checked
    def verifyCredential(self,email,password):
        try:
            students=self.db.get_all_students()
            for s in students:
                if(s['email']==email):
                    if(s['password']==password):
                        return s['id']
            return False
        except Exception as e:
            print("Error:", e)

    # checked
    def register(self, studentID, name, email, password):
        try:
            self.db.add_student(studentID, name, email, password)
        except Exception as e:
            print("Error:", e)

    # checked
    def studentRegistration(self):
        try:
            while 1:
                email = input("    Email: ")
                password = input("    Password: ")
                if self.validateEmail(email) and self.validatePassword(password):
                    Utils.print_yellow('    email and password formats acceptable')
                    break
                else:
                    Utils.print_red("    Incorrect email or password format")
            students=self.db.get_all_students()
            for student in students:
                if(email == student['email']):
                    Utils.print_red('    Student ' +student['name']+' already exists')
                    return
            name = input("    Name: ")
            Utils.print_yellow('    Enrolling Student '+ name)
            id=self.generateStudentID()
            self.register(id,name,email,password)
        except Exception as e:
            print("Error:", e)

    # checked
    def validateEmail(self, email):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@university\.com$"
        if re.match(email_pattern, email):
            return True
        else:
            return False

    # checked
    def validatePassword(self, password):
        password_pattern = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"
        if re.match(password_pattern, password):
            return True
        else:
            return False

    # checked
    def generateStudentID(self):
        try: 
            students=self.db.get_all_students()
            students_ids = {student['id'] for student in students}
            while 1:            
                new_id=Utils.generate_random_student_id()
                if(new_id not in students_ids):
                    return new_id
            return
        except Exception as e:
            print("Error:", e)  
    
    #checked
    def getGrade(self,mark):
        try:
            score=int(mark)
            if score >= 85:
                return "HD"
            elif score >= 75:
                return "D"
            elif score >= 65:
                return "C"
            elif score >= 50:
                return "P"
            else:
                return "Z"
        except Exception as e:
            print("Error:", e)

# std = Student()
# std.viewEnrolment('957916')
# std.removeSubject('957916')
# std.changePassword('957916')
# std.studentRegistration()