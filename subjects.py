import random
from database import Database
from utils import Utils

class Subjects:

    def __init__(self):
        self.db = Database()
        self.subjects = [
                {'id': '501', 'name': 'Mathematics'},
                {'id': '401', 'name': 'Science'},
                {'id': '390', 'name': 'Computer Science'},
                {'id': '302', 'name': 'History'},
                {'id': '303', 'name': 'Geography'}
            ]

    # def display_subjects(self):
    #     print("Available Courses:")
    #     for subject in self.subjects:
    #         print(f"ID: {subject['id']}, Name: {subject['name']}")

    #checked
    def enroll_subject(self, student_id):
        try:
            enrolled_subjects = self.db.get_subjects(student_id)
            if enrolled_subjects and len(enrolled_subjects) >= 4:
                Utils.print_red('        Students are allowed to enrol in 4 subjects only')
                return
            if enrolled_subjects:
                available_courses = [subject for subject in self.subjects if subject['id'] not in enrolled_subjects]
            else:
                available_courses= self.subjects
            subject_to_enroll = random.choice(available_courses)
            self.db.set_subjects(student_id, subject_to_enroll['id'], subject_to_enroll['name'], random.randint(25, 100))
            Utils.print_yellow('        Enrolling in Subject-'+subject_to_enroll['id'])
            if enrolled_subjects:
                c=len(enrolled_subjects)+1
            else:
                c=1
            Utils.print_yellow('        You are now enrolled in '+str(c)+' out of 4 subjects')
        except Exception as e:
            print("Error: {e}")

    #checked
    def drop_subject(self, student_id, subject_id):
        try:
            enrolled_subjects = self.db.get_subjects(student_id)
            if subject_id in enrolled_subjects:
                self.db.remove_subject(student_id, subject_id)
                Utils.print_yellow("        Dropping Subject-"+subject_id)
                Utils.print_yellow('        You are now enrolled in '+str(len(enrolled_subjects)-1)+' out of 4 subjects')
            else:
                Utils.print_red("        Subject not found or already dropped.")
        except Exception as e:
            print("Error: {e}")
        

# Testing
# sub = Subjects()

# sub.display_subjects()

# sub.enroll_subject('110571')

# sub.drop_subject('957916', '303')