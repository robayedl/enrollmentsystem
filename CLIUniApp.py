from subjects import Subjects
from student import Student
from admin import Admin
from database import Database
from utils import Utils

class CLIUniApp:
    def __init__(self):
        self.db = Database()
        self.std=Student()
        self.ad=Admin()

    def main(self):
        db=Database()
        while(1):
            opMain= input("\033[94mUniversity System: (A)dmin, (S)tudent, or X : \033[0m")
            if opMain == 'A' or opMain == 'a':
                while 1:
                    opAdmin= input("\033[94m    Admin System: (c/g/p/r/s/x): \033[0m")
                    if opAdmin == 'c':                        
                        Utils.print_yellow('    Clearing student database')
                        self.ad.clearAllData()
                    elif opAdmin == 'g':
                        Utils.print_yellow('    Grade Grouping')
                        self.ad.groupStudentsByGrade()
                    elif opAdmin == 'p':
                        Utils.print_yellow('    PASS/FAIL Partition')
                        self.ad.partitionStudentsByPassFail()
                    elif opAdmin == 'r':
                        self.ad.removeStudent()
                    elif opAdmin == 's':
                        Utils.print_yellow('    Student List')
                        self.ad.viewAllStudents()
                    else:
                        break 
                
            elif opMain == 'S' or opMain =='s':
                while 1:
                    opStudent= input("\033[94m    Student System (l/r/x): \033[0m")
                    if opStudent == 'l':
                        self.std.login()
                    elif opStudent == 'r':
                        Utils.print_green('    Student Sign Up')
                        self.std.studentRegistration()
                    else:
                        break 
            else:
                Utils.print_yellow('Thank You')
                break

if __name__ == "__main__":
    cli_app = CLIUniApp()
    cli_app.main()